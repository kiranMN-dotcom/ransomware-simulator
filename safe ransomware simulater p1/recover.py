from pathlib import Path
import shutil

lab_folder = Path(__file__).parent
backup_folder = lab_folder / "backup"
recovered_folder = lab_folder / "recovered"

recovered_folder.mkdir(exist_ok=True)
if not backup_folder.is_dir():
    print("ERROR: Backup folder not found.")
    raise SystemExit(1)

for file_path in backup_folder.glob("*.txt"):
    output_path = recovered_folder / file_path.name
    shutil.copy2(file_path, output_path)
    print(f"Recovered copy: {file_path.name}")

print("Recovery completed!")