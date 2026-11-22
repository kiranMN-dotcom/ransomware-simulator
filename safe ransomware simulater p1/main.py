from pathlib import Path

def toy_transform(text):
    result = ""
    for character in text:
        result += chr(ord(character) + 1)
    return result


lab_folder = Path(__file__).parent
originals_folder = lab_folder / "originals"
transformed_folder = lab_folder / "transformed"

transformed_folder.mkdir(exist_ok=True)

for file_path in originals_folder.glob("*.txt"):
    original_text = file_path.read_text(encoding="utf-8")
    transformed_text = toy_transform(original_text)

    output_path = transformed_folder / file_path.name
    output_path.write_text(transformed_text, encoding="utf-8")

    print(f"Created transformed copy: {file_path.name}")

print("Toy transformation completed!")