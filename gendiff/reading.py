import os


def read(file_path: str) -> str:
    """Read the file"""
    try:
        with open(file_path) as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(
            "Files are not found. Check paths and names of the files."
        )


def get_text_format(file_path: str) -> str:
    """Get format of the file."""
    _, format = os.path.splitext(file_path)
    return format
