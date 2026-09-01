"""Small local validator for participant and reference T-S-F-D codebooks."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys


REQUIRED_COLUMNS = {
    "code_id",
    "parent_code_id",
    "code_name",
    "code_level",
    "definition",
    "inclusion_criteria",
    "exclusion_criteria",
    "example_quote",
    "text_unit_id",
    "source_file",
    "review_status",
}
EXPECTED_PARENT_PREFIX = {
    "descriptive": "F",
    "focused": "S",
    "synthetic": "T",
}


def clean(value: object) -> str:
    return str(value or "").strip()


def read_rows(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        return rows, set(reader.fieldnames or [])


def find_cycle(parent_by_id: dict[str, str]) -> list[str]:
    for start in parent_by_id:
        seen: list[str] = []
        current = start
        while current:
            if current in seen:
                index = seen.index(current)
                return seen[index:] + [current]
            seen.append(current)
            current = parent_by_id.get(current, "")
    return []


def find_unmapped_candidate_codes(rows: list[dict[str, str]]) -> list[str]:
    """Return candidate D/F/S identifiers that lack a parent.

    Warsztatowy punkt rozszerzenia dla Codexa. Funkcja ma tylko wskazywac
    rekordy do przegladu; nie moze przypisywac rodzica ani zmieniac statusu.
    """
    raise NotImplementedError("Zaimplementuj z Codexem na podstawie testu akceptacyjnego.")


def validate(path: Path) -> list[str]:
    rows, columns = read_rows(path)
    errors: list[str] = []
    missing = sorted(REQUIRED_COLUMNS - columns)
    if missing:
        return [f"Missing columns: {', '.join(missing)}"]
    if not rows:
        return ["Codebook has no rows."]

    ids = [clean(row["code_id"]) for row in rows]
    if any(not code_id for code_id in ids):
        errors.append("Empty code_id found.")
    duplicates = sorted({code_id for code_id in ids if ids.count(code_id) > 1})
    if duplicates:
        errors.append(f"Duplicate code_id: {', '.join(duplicates[:10])}")

    id_set = set(ids)
    parent_by_id = {clean(row["code_id"]): clean(row["parent_code_id"]) for row in rows}
    for row in rows:
        code_id = clean(row["code_id"])
        level = clean(row["code_level"])
        parent = clean(row["parent_code_id"])
        status = clean(row["review_status"])

        if level not in {"descriptive", "focused", "synthetic", "theoretical"}:
            errors.append(f"{code_id}: unsupported code_level {level!r}.")

        if parent and parent not in id_set:
            errors.append(f"{code_id}: missing parent {parent}.")
        if level == "theoretical" and parent:
            errors.append(f"{code_id}: theoretical code must not have a parent.")
        expected_prefix = EXPECTED_PARENT_PREFIX.get(level)
        if expected_prefix and status != "needs_review":
            if not parent.startswith(expected_prefix):
                errors.append(
                    f"{code_id}: {level} must have parent {expected_prefix}..."
                )

        if level == "descriptive":
            forbidden = ("definition", "inclusion_criteria", "exclusion_criteria")
            if any(clean(row[field]) for field in forbidden):
                errors.append(f"{code_id}: descriptive D must not define category fields.")
        if level == "synthetic":
            required = ("definition", "inclusion_criteria", "exclusion_criteria")
            if any(not clean(row[field]) for field in required):
                errors.append(f"{code_id}: synthetic S needs definition and both criteria.")

        if status == "accepted":
            evidence = ("example_quote", "text_unit_id", "source_file")
            if any(not clean(row[field]) for field in evidence):
                errors.append(f"{code_id}: accepted entry has incomplete evidence trace.")

    cycle = find_cycle(parent_by_id)
    if cycle:
        errors.append(f"Hierarchy cycle: {' -> '.join(cycle)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a T-S-F-D codebook CSV.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"FAIL: file does not exist: {args.path}")
        return 1
    errors = validate(args.path)
    if errors:
        print(f"FAIL: {args.path}")
        for error in errors:
            print(f"- {error}")
        return 1
    rows, _ = read_rows(args.path)
    counts: dict[str, int] = {}
    for row in rows:
        level = clean(row["code_level"])
        counts[level] = counts.get(level, 0) + 1
    summary = ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    print(f"PASS: {args.path} ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
