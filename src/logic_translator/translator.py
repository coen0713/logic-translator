from AST import Node
import string
import sys

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

def parse(tokens):
    if not tokens:
        return None

    if len(tokens) == 1 and tokens[0][1] == "ATOM":
        return Node(tokens[0][0], "ATOM")

    types = [t[1] for t in tokens]

    if "IF" in types:
        if_idx = types.index("IF")
        then_idx = types.index("THEN")
        return Node("implies", "IMPLIES", children=[
            parse(tokens[if_idx + 1 : then_idx]), 
            parse(tokens[then_idx + 1:])
        ])
        
    if "NOT" in types:
        pivot = types.index("NOT")
        return Node("not", "NOT", children=[parse(tokens[pivot + 1:])])

    if "OR" in types:
        pivot = types.index("OR")
        return Node("or", "OR", children=[
            parse(tokens[:pivot]), 
            parse(tokens[pivot + 1:]) 
        ])

    if "AND" in types:
        pivot = types.index("AND")
        return Node("and", "AND", children=[
            parse(tokens[:pivot]), 
            parse(tokens[pivot + 1:])
        ])
    
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py 'your sentance here'")
    else:
        user_input = sys.argv[1]

        tokens = tokenize(user_input)
        
        try:
            ast_root = parse(tokens)

            if ast_root:
                print("\n--- Translation ---")
                print(f"Input: {user_input}")
                print(f"Output: {ast_root.render()}\n")
            else:
                print("Error: Could not parse logic.")

        except Exception as e:
            print(f"An error occured: {e}")
