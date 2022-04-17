"""
Parse input text and return
"""

from typing import Optional
from lark.lark import Lark
from utils import get_text_from_file

def_gram = "tutle_grammer.txt"


class Parser:
    def __init__(self, input_file_path: str, turtle_grammar: Optional[str] = None) -> None:
        self.program = get_text_from_file(input_file_path)
        self.gram = turtle_grammar or get_text_from_file(def_gram)
        self._parser = Lark(self.gram)

    def read_all(self):
        return self._parser.parse(self.program)
