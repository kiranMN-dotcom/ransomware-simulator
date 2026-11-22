Safe Ransomware Simulation Lab

Project Overview

This is a beginner-friendly cybersecurity learning project built with Python 3.12 and Visual Studio Code.

It demonstrates a reversible toy text transformation, backup recovery, and basic detection using simulated events. It uses dummy text files and is designed for educational purposes only.

Project Structure

- "originals/" — Original dummy text files.
- "backup/" — Copies of the original dummy files.
- "transformed/" — Separate copies containing toy-transformed text.
- "recovered/" — Files restored from backups.
- "logs/" — Detection log output.
- "main.py" — Performs the reversible toy text transformation.
- "recover.py" — Copies backup files into the recovery folder.
- "detect.py" — Demonstrates basic detection using simulated events.

How to Run

Open the project folder in VS Code and use the terminal.

Run the toy transformation:

py -3.12 main.py

Run backup recovery:

py -3.12 recover.py

Run simulated detection:

py -3.12 detect.py

View the detection log:

Get-Content .\logs\detection.log

Testing and Verification

- Confirmed that the toy transformation creates separate output files.
- Confirmed that the original dummy text files remain readable.
- Restored copies from the backup folder.
- Compared recovered files with originals using PowerShell "Compare-Object".
- Tested simulated event counts above and below the detection threshold.

Safety Boundaries

- Uses dummy text files only.
- Uses a reversible character-shift transformation, not secure encryption.
- Detection uses simulated events and does not monitor real file activity.
- Does not intentionally delete or overwrite original or backup files.
- Intended for local educational use only.

Skills Learned

- Python file handling and "pathlib"
- Text transformation and reversal
- Backup and recovery concepts
- Basic event counting and threshold-based detection
- Logging and verification with PowerShell
- Project documentation in Markdown

Conclusion

This project demonstrates basic defensive cybersecurity concepts through a controlled, beginner-friendly simulation. It is a learning exercise, not a real ransomware tool or production security detector.