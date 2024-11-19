import os


def get_text(file_path: str) -> str:
    """Get text from file."""
    with open(file_path) as file:
        return file.read()


def get_text_format(file_path: str) -> str:
    """Get format of the file."""
    _, format = os.path.splitext(file_path)
    return format[1:].lower()
