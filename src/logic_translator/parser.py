from AST.py import Node
import string

TOKEN_MAP = {
        "and" : "AND",
        "or" : "OR",
        "not" : "NOT",
        "if" : "IF",
        "then" : "THEN"
}

STOP_WORDS = {"it", "is", "the", "a", "an", "are", "was", "were"}

def tokenize(sentance):
    sentance = sentance.lower()
    for char in string.punctuation:
        sentance = sentance.replace(char, "")
    
    words = sentance.split()
    tokens = []
    temp_atom = []

    for word in words:
        token_type = get_token_type(word)

        if token_type == "ATOM":
            if word not in STOP_WORDS:
                temp_atom.append(word)

        else:
            if temp_atom:
                tokens.append(("_".join(temp_atom), "ATOM"))
                temp_atom = []

            tokens.append((word, token_type))

    if temp_atom:
        tokens.append(("_".join(temp_atom), "ATOM"))

    return tokens

def get_token_type(word):
    return TOKEN_MAP.get(word, "ATOM")

