import pyparsing as pp

class Symbol:
    def __init__(self, tokens):
        self._tokens = tokens
        self.parent = None
    
    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent
    
class Terminal(Symbol):
    def __init__(self, tokens):
        super().__init__(tokens)
        self._tokens = self._tokens[0]
    
    def __repr__(self):
        return "".join(self._tokens)

class NonTerminal(Symbol):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.children = self._tokens
        for child in self.children:
            child.set_parent(self)
    
    def __repr__(self):
        return f"{self.__class__.__name__}: {self._tokens}"
    
    def __len__(self):
        return len(self.children)
    
    def get_children(self):
        return self.children

class Collection(NonTerminal):
    def __init__(self, tokens):
        super().__init__(tokens)
        for child in self.children:
            child.root = True

class Tree(NonTerminal):
    def __init__(self, tokens):
        tokens = tokens[0]
        self.root = False
        super().__init__(tokens)
    
    def get_root(self):
        if self.root:
            return self.children[0].children[0]
        else:
            return AttributeError
    
class Sequence(NonTerminal):
    def __init__(self, tokens):
        super().__init__(tokens)

class Node(NonTerminal):
    def __init__(self, tokens):
        super().__init__(tokens)
    def squeeze(self):
        pass

class Property(NonTerminal):
    def __init__(self, tokens):
        super().__init__(tokens)
    def squeeze(self):
        return "".join(map(str, self._tokens))

class PropertyID(Terminal):
    def __init__(self, tokens):
        super().__init__(tokens)

    def __repr__(self):
        return "".join(self._tokens)

class PropertyValue(Terminal):
    def __init__(self, tokens):
        super().__init__(tokens)

    def __repr__(self):
        return "[" + "".join(self._tokens) + "]"

def syntax():
    tree = pp.Forward()
    prop_ident = pp.Word(pp.alphas.upper())
    prop_value = pp.nested_expr("[", "]") # Update ignore_expr later, content can be alphanums or smth

    prop = prop_ident + pp.OneOrMore(prop_value)
    node = pp.Suppress(";") + pp.ZeroOrMore(prop)
    sequence = pp.OneOrMore(node)
    tree << pp.nested_expr(content = sequence + pp.ZeroOrMore(tree))
    collection = pp.OneOrMore(tree)

    prop_ident.add_parse_action(PropertyID)
    prop_value.add_parse_action(PropertyValue)
    prop.add_parse_action(Property)
    node.add_parse_action(Node)
    sequence.add_parse_action(Sequence)
    tree.add_parse_action(Tree)
    collection.add_parse_action(Collection)

    return collection

def sgf_file_parse(file_name):
    eval = syntax()
    return eval.parse_file(file_name, encoding = "UTF-8")[0]

if __name__ == "__main__":
    eval = syntax()

    input = '''
    ;B[qd]
    '''

    output = eval.parse_file("-1.sgf", encoding="UTF-8")

    print(output)