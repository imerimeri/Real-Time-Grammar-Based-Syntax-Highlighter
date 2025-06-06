
"""
Parser
- Top-Down Parsing approach (preorder traversal)
- Parses the token stream based on Context-Free Grammar (CFG)
- Reports syntax correctness
"""

from tokenizer import Token, extract_extracted_syntax_tokens


class GrammarParser:
    def __init__(self, extracted_syntax_tokens):
        self.extracted_syntax_tokens = extracted_syntax_tokens
        self.pos = 0

    def current_syntax_token(self):
        if self.pos < len(self.extracted_syntax_tokens):
            return self.extracted_syntax_tokens[self.pos]
        return Token("EOF", "", len(self.extracted_syntax_tokens))

    def regex_match(self, expected_type, expected_value=None):
        syntax_token = self.current_syntax_token()
        if syntax_token.type == expected_type and (expected_value is None or syntax_token.value == expected_value):
            self.pos += 1
            return syntax_token
        raise SyntaxError(f"Expected {expected_type} '{expected_value}' at pos {syntax_token.position}, got '{syntax_token.value}'")

    def analyze_structure(self):
        while self.current_syntax_token().type != "EOF":
            self.statement()

    def statement(self):
        syntax_token = self.current_syntax_token()
        if syntax_token.type == "KEYWORD" and syntax_token.value in {"int", "float"}:
            self.var_declaration()
        elif syntax_token.type == "IDENTIFIER":
            self.assignment()
        elif syntax_token.type == "KEYWORD" and syntax_token.value == "if":
            self.if_statement()
        elif syntax_token.type == "KEYWORD" and syntax_token.value == "while":
            self.while_statement()
        else:
            raise SyntaxError(f"Unexpected syntax_token '{syntax_token.value}'")

    def var_declaration(self):
        self.regex_match("KEYWORD")
        self.regex_match("IDENTIFIER")
        self.regex_match("DELIMITER", ";")

    def assignment(self):
        self.regex_match("IDENTIFIER")
        self.regex_match("OPERATOR", "=")
        self.expression()
        self.regex_match("DELIMITER", ";")

    def if_statement(self):
        self.regex_match("KEYWORD", "if")
        self.regex_match("DELIMITER", "(")
        self.expression()
        self.regex_match("DELIMITER", ")")
        self.regex_match("DELIMITER", "{")
        while self.current_syntax_token().value != "}":
            self.statement()
        self.regex_match("DELIMITER", "}")

    def while_statement(self):
        self.regex_match("KEYWORD", "while")
        self.regex_match("DELIMITER", "(")
        self.expression()
        self.regex_match("DELIMITER", ")")
        self.regex_match("DELIMITER", "{")
        while self.current_syntax_token().value != "}":
            self.statement()
        self.regex_match("DELIMITER", "}")

    def expression(self):
        self.arith_expression()
        if self.current_syntax_token().type == "OPERATOR" and self.current_syntax_token().value in {">", "<", ">=", "<=", "==", "!="}:
            self.regex_match("OPERATOR")
            self.arith_expression()

    def arith_expression(self):
        self.term()
        while self.current_syntax_token().value in {"+", "-"}:
            self.regex_match("OPERATOR")
            self.term()



    def term(self):
        self.factor()
        while self.current_syntax_token().value in {"*", "/"}:
            self.regex_match("OPERATOR")
            self.factor()

    def factor(self):
        syntax_token = self.current_syntax_token()
        if syntax_token.type == "NUMBER":
            self.regex_match("NUMBER")
        elif syntax_token.type == "IDENTIFIER":
            self.regex_match("IDENTIFIER")
        elif syntax_token.value == "(":
            self.regex_match("DELIMITER", "(")
            self.expression()
            self.regex_match("DELIMITER", ")")
        else:
            raise SyntaxError(f"Unexpected syntax_token '{syntax_token.value}' in factor")
