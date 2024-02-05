import pyparsing as pp

class Symbol:
    def __init__(self, tokens):
        self.tokens = tokens.asList()
    def __repr__(self):
        return f"{self.__class__.__name__}: ({self.tokens})"
    
class Terminal(Symbol):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.tokens = self.tokens[0]

class NonTerminal(Symbol):
    def __init__(self, tokens):
        super().__init__(tokens)

class Collection(NonTerminal):
    pass

class Tree(NonTerminal):
    pass
    


def syntax():
    tail = pp.Forward()
    prop_ident = pp.Word(pp.alphas.upper()).addParseAction(Terminal)
    prop_value = pp.QuotedString("[", esc_char = "\\", end_quote_char = "]").addParseAction(Terminal)

    prop = pp.Group(prop_ident + pp.OneOrMore(prop_value)).addParseAction(NonTerminal)
    node = pp.Suppress(";") + pp.ZeroOrMore(prop).addParseAction(NonTerminal)
    root_node = pp.Group(node).addParseAction(NonTerminal)
    sequence = pp.OneOrMore(node).addParseAction(NonTerminal)
    tail << pp.nested_expr(content = sequence + pp.ZeroOrMore(tail))
    game_tree = pp.nested_expr(content = root_node + sequence + pp.ZeroOrMore(tail))
    collection = pp.OneOrMore(game_tree)

    return node

eval = syntax()

input = '''
;B[qd]
'''

print(eval.parse_string(input))

# print(eval.parse_file("-1.sgf"))


