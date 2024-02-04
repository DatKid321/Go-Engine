import pyparsing as pp 

def Syntax():
    PropIdent = pp.Word(pp.alphas.upper())
    PropValue = pp.QuotedString("[", esc_char = "\\", end_quote_char = "]")

    Property = pp.Group(PropIdent + pp.OneOrMore(PropValue))
    Node = pp.Suppress(";") + pp.ZeroOrMore(Property)
    RootNode = pp.Group(Node)
    NodeSequence = pp.ZeroOrMore(Node)
    Tail = pp.Forward()
    Tail << pp.nested_expr(content = NodeSequence + pp.ZeroOrMore(Tail))
    GameTree = pp.nested_expr(content = RootNode + NodeSequence + pp.ZeroOrMore(Tail))
    Collection = pp.ZeroOrMore(GameTree)

    return Collection

eval = Syntax()

print(eval.parse_file("-1.sgf"))


