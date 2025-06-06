
"""
Main Application Window
- GUI implemented with PyQt5
- Loads .ui layout
- Connects code editor with real-time syntax analysis
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from text_styler import SyntaxStyler
from tokenizer import extract_extracted_syntax_tokens
from syntax_parser import GrammarParser


class AppWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("app_layout.ui", self)

        self.highlighter = SyntaxStyler(self.codeEditor.document())
        self.codeEditor.textChanged.connect(self.analyze_structure_code)  
         

    def analyze_structure_code(self):  
        code = self.codeEditor.toPlainText()
        try:
            extracted_syntax_tokens = extract_extracted_syntax_tokens(code)
            analyze_structurer = GrammarParser(extracted_syntax_tokens)
            analyze_structurer.analyze_structure()
            self.statusLabel.setText("✅ Geçerli sözdizimi.")
        except SyntaxError as e:
            self.statusLabel.setText(f"❌ Hata: {e}")
        except Exception as ex:
            import traceback
            self.statusLabel.setText(str(ex))
            traceback.print_exc()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
