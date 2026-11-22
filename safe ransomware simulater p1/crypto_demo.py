from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

# All demo files stay inside this dedicated folder.
LAB = Path(__file__).parent / "crypto_lab"
LAB.mkdir(exist_ok=True)

sample = LAB / "sample.txt"
key_file = LAB / "demo.key"
encrypted = LAB / "sample.txt.fernet"
decrypted = LAB / "decrypted_sample.txt"

# Create a disposable sample only if it does not exist.
if not sample.exists():
    sample.write_text(
        "This is a disposable encryption demonstration file.",
        encoding="utf-8"
    )

# Generate and save a key only once.
if not key_file.exists():
    key_file.write_bytes(Fernet.generate_key())

key = key_file.read_bytes()
cipher = Fernet(key)

# Encrypt into a separate output file; never overwrite.
if not encrypted.exists():
    encrypted.write_bytes(cipher.encrypt(sample.read_bytes()))
    print("Encryption successful:", encrypted.name)
else:
    print("Encrypted output already exists; left unchanged.")

# Decrypt into another separate output file; never overwrite.
if not decrypted.exists():
    try:
        decrypted.write_bytes(
            Fernet(key).decrypt(encrypted.read_bytes())
        )
    except InvalidToken:
        print("Decryption failed: invalid key or data.")
    else:
        print(f"Decryption successful: {decrypted.name}")
else:
    print("Decrypted output already exists; left unchanged.")

# Test that a wrong key is rejected
try:
    wrong_key = Fernet.generate_key()
    Fernet(wrong_key).decrypt(encrypted.read_bytes())
except InvalidToken:
    print("PASS: Wrong key was rejected safely.")
else:
    print("WARNING: Unexpected result.")

print("Demo completed. Original sample and key were preserved.")