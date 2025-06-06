
"""
Syntax Highlighter
- Implements real-time highlighting of 5+ distinct token types
- Subclasses PyQt5's QSyntaxHighlighter
- Token types highlighted: Keywords, Identifiers, Numbers, Strings, Operators, Comments
"""

from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from tokenizer import extract_extracted_syntax_tokens

class SyntaxStyler(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        # Formatlar
        self.formats = {
            'KEYWORD': self._create_format(QColor("#0000FF"), bold=True),
            'IDENTIFIER': self._create_format(QColor("#000000")),
            'NUMBER': self._create_format(QColor("#800080")),
            'STRING': self._create_format(QColor("#008000")),
            'OPERATOR': self._create_format(QColor("#FF0000")),
            'COMMENT': self._create_format(QColor("#808080"), italic=True),
        }

    def _create_format(self, color, bold=False, italic=False):
        text_format = QTextCharFormat()
        text_format.setForeground(color)
        if bold:
            text_format.setFontWeight(QFont.Bold)
        if italic:
            text_format.setFontItalic(True)
        return text_format

    def highlightBlock(self, text):
        tokens = extract_extracted_syntax_tokens(text)
        index = 0
        for token in tokens:
            length = len(token.value)
            token_format = self.formats.get(token.type)
            if token_format:
                self.setFormat(index, length, token_format)
            index += length
