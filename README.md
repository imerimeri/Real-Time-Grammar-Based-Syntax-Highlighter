
# Real-Time Grammar-Based Syntax Highlighter with GUI

## Programming Language
- Python 3.12
- PyQt5

## Syntax Analysis
- Parser implemented using **Top-Down Parsing** (preorder traversal)
- Context-Free Grammar (CFG) defined in `syntax_parser.py`

## Lexical Analysis
- Implemented using **Formal Description & Program Implementation** approach
- Tokenizer implemented with regular expressions in `tokenizer.py`

## Parsing Methodology
- Top-Down parsing
- Reports syntax correctness or syntax error

## Highlighting Scheme
Implemented using a subclass of **QSyntaxHighlighter** in `text_styler.py`.
The following token types are highlighted in real-time:
1. Keywords
2. Identifiers
3. Numbers
4. Strings
5. Operators
6. Comments

## GUI Implementation
- Implemented with **PyQt5**
- `.ui` file: `app_layout.ui`
- Real-time updating as the user types
- Status bar indicates syntax validity

## Project Structure
```
app_main.py          # Main application window
app_layout.ui        # UI layout
tokenizer.py         # Lexer
syntax_parser.py     # Parser
text_styler.py       # Syntax Highlighter
README.md            # This file
```

## Notes
- No external syntax highlighting libraries used.
- All components implemented manually.
- For full compliance, prepare:
    - Demo video
    - Publicly shared article

## How to Run
```bash
cd final_project_package
python app_main.py
```

Enjoy!
