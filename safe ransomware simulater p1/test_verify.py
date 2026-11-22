
from pathlib import Path
from tempfile import TemporaryDirectory
from verify import sha256_file
import unittest
import hashlib

def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class TestSHA256(unittest.TestCase):

    def test_missing_file(self):
        with TemporaryDirectory() as folder:
            missing_file = Path(folder) / "missing.txt"

            self.assertFalse(missing_file.exists())

    def test_different_text_has_different_hash(self):
        with TemporaryDirectory() as folder:
            file1 = Path(folder) / "file1.txt"
            file2 = Path(folder) / "file2.txt"

            file1.write_text("First text", encoding="utf-8")
            file2.write_text("Different text", encoding="utf-8")

            self.assertNotEqual(
                sha256_file(file1),
                sha256_file(file2)
            )

    def test_different_text_has_different_hash(self):
        self.assertNotEqual(
            sha256_text("Safe test content"),
            sha256_text("Different content")
        )
    def test_missing_file(self):
        with TemporaryDirectory() as folder:
            missing_file = Path(folder) / "missing.txt"
            self.assertFalse(missing_file.exists())

if __name__ == "__main__":
    unittest.main()