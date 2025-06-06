
"""
Lexer (Tokenizer)
- Formal Description & Program Implementation approach
- Regular expressions used to define token patterns
- Tokenizes input into stream of tokens
"""

import re
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

# Token türleri
token_specification = [
    ('COMMENT',   r'#.*'),                # Comment
    ('STRING',    r'\".*?\"|\'.*?\''),    # String    
    ('NUMBER',    r'\b\d+(\.\d*)?\b'),   # Integer or decimal number
    ('KEYWORD',   r'\b(if|else|for|while|return|def|class|import|from|as|try|except)\b'), # Keywords
    ('IDENTIFIER',r'\b[A-Za-z_]\w*\b'), # Identifiers
    ('OPERATOR',  r'[+\-*/=<>!]+'),       # Operators
    ('NEWLINE',   r'\n'),                # Line endings
    ('SKIP',      r'[ \t]+'),            # Skip spaces and tabs
    ('MISMATCH',  r'.'),                  # Any other character
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
get_token = re.compile(tok_regex).match

def extract_extracted_syntax_tokens(code):
    tokens = []
    pos = 0
    match = get_token(code, pos)
    while match is not None:
        typ = match.lastgroup
        val = match.group(typ)
        if typ != 'SKIP' and typ != 'NEWLINE':
            tokens.append(Token(typ, val))
        pos = match.end()
        match = get_token(code, pos)
    return tokens
