from pathlib import Path
import hashlib


def sha256_file(file_path):
    """Return the SHA-256 hash of a file."""
    digest = hashlib.sha256()

    try:
        with file_path.open("rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                digest.update(chunk)

        return digest.hexdigest()

    except OSError as error:
        print(f"ERROR reading {file_path.name}: {error}")
        return None


def main():
    lab_folder = Path(__file__).parent
    originals = lab_folder / "originals"
    recovered = lab_folder / "recovered"
    logs_folder = lab_folder / "logs"

    logs_folder.mkdir(exist_ok=True)

    report_file = logs_folder / "verification_report.txt"
    report_lines = []

    if not originals.is_dir():
        print("ERROR: originals folder not found.")
        return

    if not recovered.is_dir():
        print("ERROR: recovered folder not found.")
        return

    logs_folder.mkdir(exist_ok=True)
    report_file = logs_folder / "verification_report.txt"
    report_lines = []

    for original in sorted(originals.glob("*.txt")):
        restored = recovered / original.name

        if not restored.is_file():
            result = f"MISSING: {original.name}"
            print(result)
            report_lines.append(result)
            continue

        original_hash = sha256_file(original)
        recovered_hash = sha256_file(restored)

        if original_hash is None or recovered_hash is None:
            result = f"ERROR: Could not verify {original.name}"
        elif original_hash == recovered_hash:
            result = f"PASS: {original.name} matches"
        else:
            result = f"FAIL: {original.name} does not match"

        print(result)
        report_lines.append(result)

    if not report_lines:
        report_lines.append("No original .txt files found.")

    report_file.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"Verification report saved to: {report_file}")


if __name__ == "__main__":
    main()