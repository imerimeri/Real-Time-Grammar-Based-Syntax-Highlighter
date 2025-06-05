Real-Time Grammar-Based Syntax Highlighter Using Python and Qt

Project Overview

This project implements a real-time syntax highlighting application based on a custom grammar. The system is designed to analyze code as it's written, providing both lexical and syntactic feedback in real time.

Key Features:
Lexical Analysis using regular expressions
Syntax Analysis using a recursive descent parser
User Interface built with PyQt5 and Qt Designer
Instant Feedback on syntax correctness with error messages and syntax highlighting
Technologies Used

Python 3
PyQt5 – for GUI development
Qt Designer – for creating .ui files
Python re module – for regex-based token generation
Language and Grammar

The application is based on a simplified, C-like programming language. Supported constructs include:

Variable declarations: int x;
Assignments: x = 5 + 3;
Conditional statements: if (x > 3) { ... }
Loops: while (x < 10) { ... }

✨ Core Functionality

Real-time syntax highlighting based on token types:

Keywords: blue
Identifiers: black
Numbers: purple
Operators: red
Delimiters: green
Invalid characters: gray
Additionally:

Real-time parsing and error reporting
User-friendly interface for writing and testing code
Designed to aid learners by providing immediate grammar-based feedback
System Architecture

lexer.py: Tokenizes input using regular expressions
parser.py: Parses tokens based on defined grammar rules
highlighter.py: Applies syntax highlighting using QSyntaxHighlighter
main.py: Initializes the GUI and handles signal connections
Challenges Faced

Implementing comparison operators (>, <, ==) in both lexer and parser
Maintaining real-time performance without relying on external libraries
Creating a robust feedback mechanism without external syntax parsers
Final Outcome

The application successfully delivers a real-time, grammar-driven syntax highlighting experience. It serves as an educational tool by reinforcing language structure through immediate visual and textual feedback.

🎥 Demo Video: Watch on YouTube
📝 Project Documentation: Read on GitHub
