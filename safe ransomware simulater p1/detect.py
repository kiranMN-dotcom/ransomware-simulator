from pathlib import Path
from datetime import datetime

lab_folder = Path(__file__).parent
logs_folder = lab_folder / "logs"
logs_folder.mkdir(exist_ok=True)

log_file = logs_folder / "detection.log"

# These are simulated events, not real file activity.
simulated_events = [
    "change",
    "change",
]

threshold = 3
change_count = 0

for event in simulated_events:
    print(f"Simulated event: {event}")

    if event == "change":
        change_count += 1

if change_count >= threshold:
    alert = (
        f"{datetime.now().isoformat(timespec='seconds')} "
        f"ALERT: {change_count} simulated changes detected.\n"
    )
    print(alert.strip())
    with log_file.open("a", encoding="utf-8") as file:
        file.write(alert)
else:
    print("No alert: activity below threshold.")