from PIL import Image
import os


def convert_image(input_path: str, output_format: str) -> str:
    img = Image.open(input_path)

    base = os.path.splitext(input_path)[0]
    output_path = f"{base}.{output_format.lower()}"

    img.save(output_path, output_format)
    return output_path
