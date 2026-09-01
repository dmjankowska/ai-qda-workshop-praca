"""Minimal infrastructure for the participant-facing AI_QDA notebooks.

The module handles a bounded evidence packet, provider calls, logs and files.
It deliberately contains no tuned prompts and no D/F/S/T construction logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from typing import Any

import pandas as pd


PACKET_ROWS = [
    {
        "text_unit_id": "PREWORK_01_U0107",
        "case_id": "PREWORK_01",
        "source_file": "PREWORK_01_trans.docx",
        "sequence": 107,
        "speaker": "J",
        "text": (
            "A nawet samo to, że ona potrafi obrazić pracownika w obecności ludzi. "
            "Czyli na przykład, jak ja sprzedawałam wędliny, potrafiła do mnie "
            "podejść, naubliżać mi i wyjść. I tak, jakby jej to sprawiało radość, "
            "że ona ma tę władzę nad ludźmi."
        ),
    },
    {
        "text_unit_id": "PREWORK_01_U0119",
        "case_id": "PREWORK_01",
        "source_file": "PREWORK_01_trans.docx",
        "sequence": 119,
        "speaker": "J",
        "text": (
            "Zamykałam drzwi, żebym go nie słyszała. Albo kiedyś, jak tak mnie "
            "bardzo zdenerwowała, po prostu wyszłam przez tylne drzwi. Wiedziałam, "
            "że wrócę, bo nie wzięłam ani torebki, ani kurtki. Obeszłam sobie T. "
            "w fartuszku i wróciłam zapytać, czy szefowa już ochłonęła."
        ),
    },
    {
        "text_unit_id": "PREWORK_02_U0088",
        "case_id": "PREWORK_02",
        "source_file": "PREWORK_02_trans.docx",
        "sequence": 88,
        "speaker": "A",
        "text": (
            "Myślę, że znajomości odgrywają rolę, bo dostałam obie prace przez "
            "polecenie. To jest dość zamknięta strefa. Staram się nie palić za "
            "sobą mostów, bo kolejna szkoła najpierw dzwoni do dyrektora tej, "
            "w której pracowałam."
        ),
    },
    {
        "text_unit_id": "PREWORK_02_U0123",
        "case_id": "PREWORK_02",
        "source_file": "PREWORK_02_trans.docx",
        "sequence": 123,
        "speaker": "A",
        "text": (
            "Warunki to słabe. To, co robię i odpowiedzialność za dzieci powinny "
            "się przekładać na pensję, a zarabiamy po prostu tysiąc siedemset "
            "złotych niecałe."
        ),
    },
    {
        "text_unit_id": "PREWORK_03_U0023",
        "case_id": "PREWORK_03",
        "source_file": "PREWORK_03_trans.docx",
        "sequence": 23,
        "speaker": "A",
        "text": (
            "Nie mogę się zdecydować, czy wolałabym jeździć do pracy na osiem "
            "godzin i zapominać, czy pracować w domu. Dochodzą myśli o przyszłym "
            "macierzyństwie, a umowa o pracę mogłaby zapewnić pewien byt."
        ),
    },
    {
        "text_unit_id": "PREWORK_03_U0136",
        "case_id": "PREWORK_03",
        "source_file": "PREWORK_03_trans.docx",
        "sequence": 136,
        "speaker": "A",
        "text": (
            "Umowy zlecenia utrudniają mi dostanie kredytu. Gdyby nie to, że mąż "
            "ma umowę o pracę i przyzwoite wynagrodzenie, kredytu byśmy nie "
            "dostali. Sama szukałabym jakiejkolwiek pracy na umowę o pracę."
        ),
    },
]


def load_workshop_packet() -> pd.DataFrame:
    """Return a fresh copy of the bounded, real PREWORK evidence packet."""
    return pd.DataFrame(PACKET_ROWS).copy(deep=True)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def save_json(path: str | Path, payload: Any) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return destination


def save_dataframe(path: str | Path, frame: pd.DataFrame) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(destination, index=False)
    return destination


def load_dataframe(path: str | Path, required: list[str] | None = None) -> pd.DataFrame:
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(f"Brak artefaktu z poprzedniego bloku: {source}")
    frame = pd.read_csv(source).fillna("")
    missing = sorted(set(required or []) - set(frame.columns))
    if missing:
        raise ValueError(f"Brak wymaganych kolumn w {source.name}: {missing}")
    return frame


def read_secret(name: str) -> str:
    """Read a secret from Colab or the local environment without printing it."""
    value = os.environ.get(name, "").strip()
    if value:
        return value
    try:
        from google.colab import userdata

        return str(userdata.get(name) or "").strip()
    except Exception:
        return ""


PUBLIC_WORKSHOP_REPOSITORY = "caqdastm/ai_qda-workshop-1u"
GITHUB_REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
PUBLISHABLE_SUFFIXES = {".csv", ".json", ".jsonl", ".md"}
SECRET_PATTERNS = (
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AIza[A-Za-z0-9_-]{20,}"),
)


def normalize_github_repository(value: str) -> str:
    """Return owner/repository while rejecting arbitrary Git URLs."""
    repository = str(value or "").strip().rstrip("/")
    for prefix in (
        "https://github.com/",
        "http://github.com/",
        "git@github.com:",
    ):
        if repository.startswith(prefix):
            repository = repository[len(prefix):]
            break
    if repository.endswith(".git"):
        repository = repository[:-4]
    if not GITHUB_REPOSITORY_PATTERN.fullmatch(repository):
        raise ValueError(
            "Repozytorium podaj jako login/nazwa, np. "
            "anna/ai-qda-workshop-praca."
        )
    return repository


def github_repository_url(value: str) -> str:
    return f"https://github.com/{normalize_github_repository(value)}.git"


def _git_auth_environment(token: str | None) -> dict[str, str]:
    """Pass a token through process environment, never a command or URL."""
    environment = os.environ.copy()
    if token:
        encoded = base64.b64encode(
            f"x-access-token:{token}".encode("utf-8")
        ).decode("ascii")
        environment["GIT_CONFIG_COUNT"] = "1"
        environment["GIT_CONFIG_KEY_0"] = "http.extraHeader"
        environment["GIT_CONFIG_VALUE_0"] = f"AUTHORIZATION: basic {encoded}"
    return environment


def _run_git(
    repository_dir: str | Path,
    *arguments: str,
    token: str | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=Path(repository_dir),
        env=_git_auth_environment(token),
        capture_output=True,
        text=True,
    )
    if check and completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip()
        if token:
            detail = detail.replace(token, "[UKRYTY_TOKEN]")
        raise RuntimeError(
            "Operacja Git nie powiodła się. Sprawdź nazwę repozytorium, "
            "dostęp sekretu GITHUB_TOKEN i uprawnienie Contents: Read and write. "
            f"Szczegóły Git: {detail or 'brak komunikatu'}"
        )
    return completed


def collect_publishable_outputs(
    repository_dir: str | Path,
    output_roots: list[str | Path],
    *,
    include_api_logs: bool = False,
) -> list[Path]:
    """Select reviewed workshop artifacts from outputs directories only."""
    repository = Path(repository_dir).resolve()
    selected: list[Path] = []
    for root in output_roots:
        candidate = Path(root)
        output_root = (
            candidate.resolve()
            if candidate.is_absolute()
            else (repository / candidate).resolve()
        )
        if not output_root.is_relative_to(repository):
            raise ValueError("Katalog wyników musi znajdować się w repozytorium.")
        relative_root = output_root.relative_to(repository)
        if "outputs" not in relative_root.parts:
            raise ValueError("Publikować można wyłącznie pliki z katalogów outputs/.")
        if not output_root.is_dir():
            continue
        for path in sorted(output_root.rglob("*")):
            if not path.is_file() or path.name == "README.md":
                continue
            if path.suffix.lower() not in PUBLISHABLE_SUFFIXES:
                continue
            if path.suffix.lower() == ".jsonl" and not include_api_logs:
                continue
            selected.append(path.relative_to(repository))
    return sorted(set(selected), key=lambda path: path.as_posix())


def _assert_no_secrets(repository: Path, relative_paths: list[Path]) -> None:
    for relative_path in relative_paths:
        text = (repository / relative_path).read_text(
            encoding="utf-8", errors="replace"
        )
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            raise ValueError(
                f"Zapis zatrzymany: {relative_path.as_posix()} może zawierać sekret."
            )


def publish_outputs_to_github(
    repository_dir: str | Path,
    output_roots: list[str | Path],
    *,
    message: str,
    participant_repository: str | None = None,
    token: str | None = None,
    branch: str = "main",
    include_api_logs: bool = False,
) -> dict[str, Any]:
    """Commit and push selected outputs from a participant-owned workspace."""
    repository = Path(repository_dir).resolve()
    if not (repository / ".git").exists():
        raise ValueError(f"To nie jest robocza kopia Git: {repository}")

    origin = _run_git(repository, "remote", "get-url", "origin").stdout.strip()
    if participant_repository:
        expected = normalize_github_repository(participant_repository)
        if expected.lower() == PUBLIC_WORKSHOP_REPOSITORY.lower():
            raise ValueError(
                "Nie zapisuj wyników w repozytorium prowadzących. "
                "Wskaż własne prywatne repo utworzone z szablonu."
            )
        if "github.com" in origin.lower():
            actual = normalize_github_repository(origin)
            if actual.lower() != expected.lower():
                raise ValueError(
                    f"Sklonowano {actual}, ale sekret AI_QDA_REPOSITORY "
                    f"wskazuje {expected}."
                )

    selected = collect_publishable_outputs(
        repository,
        output_roots,
        include_api_logs=include_api_logs,
    )
    if not selected:
        return {"status": "no_files", "paths": [], "origin": origin}
    _assert_no_secrets(repository, selected)
    if "github.com" in origin.lower() and not token:
        raise RuntimeError(
            "Brak sekretu GITHUB_TOKEN. Niczego nie zatwierdzono ani nie "
            "wysłano. Dodaj sekret, włącz jego dostęp i spróbuj ponownie."
        )

    _run_git(repository, "config", "user.name", "AI QDA workshop participant")
    _run_git(
        repository,
        "config",
        "user.email",
        "ai-qda-workshop@users.noreply.github.com",
    )
    _run_git(repository, "add", "-f", "--", *(path.as_posix() for path in selected))
    staged = _run_git(
        repository, "diff", "--cached", "--name-only"
    ).stdout.splitlines()
    if not staged:
        _run_git(repository, "push", "origin", f"HEAD:{branch}", token=token)
        return {
            "status": "up_to_date",
            "paths": [path.as_posix() for path in selected],
            "origin": origin,
        }

    safe_message = " ".join(str(message).split())[:120] or "Zapisz wyniki warsztatu"
    _run_git(repository, "commit", "-m", safe_message)
    _run_git(repository, "push", "origin", f"HEAD:{branch}", token=token)
    commit = _run_git(repository, "rev-parse", "HEAD").stdout.strip()
    return {
        "status": "pushed",
        "paths": staged,
        "origin": origin,
        "commit": commit,
    }


def procedure_prompt(card: dict[str, str], technical_appendix: str) -> str:
    research_part = "\n".join(
        [
            "CZĘŚĆ BADAWCZA — intencja i granice procedury",
            f"Cel etapu: {card['goal']}",
            f"Wejście: {card['input']}",
            f"Widoczny rezultat: {card['observable_result']}",
            f"Kontrola techniczna: {card['automatic_check']}",
            f"Decyzja badacza: {card['researcher_decision']}",
        ]
    )
    return research_part + "\n\nDODATEK TECHNICZNY — infrastruktura notebooka\n" + technical_appendix


@dataclass
class AnalysisAPI:
    """Provider-neutral API used only for analytic calls on the corpus."""

    provider: str = "mock"
    gemini_model: str = "gemini-3.6-flash"
    openai_model: str = "gpt-5.4-mini"
    openai_store: bool = True
    authorize_api_calls: bool = False
    max_api_calls: int = 2
    runs: list[dict[str, Any]] = field(default_factory=list)
    api_call_count: int = 0

    def __post_init__(self) -> None:
        self.provider = self.provider.strip().lower()
        if self.provider not in {"mock", "gemini", "openai"}:
            raise ValueError("Wybierz provider='mock', 'gemini' albo 'openai'.")

    @property
    def model(self) -> str:
        return {
            "mock": "mock",
            "gemini": self.gemini_model,
            "openai": self.openai_model,
        }[self.provider]

    def _secret(self, name: str) -> str:
        key = os.getenv(name, "").strip()
        if key:
            return key
        try:
            from google.colab import userdata

            return str(userdata.get(name) or "").strip()
        except Exception:
            return ""

    def _mock_response(self, task_kind: str, task_label: str) -> str:
        return (
            f"MOCK — {task_kind}/{task_label}. Przepływ działa, ale ten tekst nie "
            "jest propozycją kodowania. Włącz API, aby porównywać odpowiedzi "
            "modelu, albo przejdź dalej na podstawie własnej lektury materiału."
        )

    def _call_gemini(self, prompt: str) -> tuple[str, str]:
        key = self._secret("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("Dodaj GEMINI_API_KEY do Colab Secrets.")
        from google import genai

        response = genai.Client(api_key=key).models.generate_content(
            model=self.gemini_model,
            contents=prompt,
        )
        text = str(getattr(response, "text", "") or "").strip()
        response_id = str(
            getattr(response, "response_id", "") or getattr(response, "id", "") or ""
        )
        return text, response_id

    def _call_openai(self, prompt: str) -> tuple[str, str]:
        key = self._secret("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("Dodaj OPENAI_API_KEY do Colab Secrets.")
        from openai import OpenAI

        response = OpenAI(api_key=key).responses.create(
            model=self.openai_model,
            input=prompt,
            store=self.openai_store,
        )
        return str(response.output_text or "").strip(), str(response.id or "")

    def run_analysis(self, prompt: str, *, task_label: str) -> str:
        provider_response_id = ""
        if self.provider == "mock":
            response_text = self._mock_response("analytic_comparison", task_label)
        else:
            if not self.authorize_api_calls:
                raise PermissionError(
                    "Wywołania API są wyłączone. Ustaw zgodę dopiero po decyzji o danych i koszcie."
                )
            if self.api_call_count >= self.max_api_calls:
                raise RuntimeError("Osiągnięto limit wywołań API dla notebooka.")
            if self.provider == "gemini":
                response_text, provider_response_id = self._call_gemini(prompt)
            else:
                response_text, provider_response_id = self._call_openai(prompt)
            self.api_call_count += 1

        self.runs.append(
            {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "task_kind": "analytic_comparison",
                "task_label": task_label,
                "provider": self.provider,
                "model": self.model,
                "prompt": prompt,
                "prompt_hash": sha256_text(prompt),
                "response": response_text,
                "provider_response_id": provider_response_id,
                "store_requested": self.openai_store if self.provider == "openai" else None,
            }
        )
        return response_text

    def export_runs(self, path: str | Path) -> Path:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8") as stream:
            for row in self.runs:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        return destination
