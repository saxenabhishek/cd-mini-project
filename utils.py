import os


def get_text_from_file(file_path: str) -> str:
    cwd = os.getcwd()
    with open(os.path.join(cwd, file_path), "r") as f:
        return f.read()
