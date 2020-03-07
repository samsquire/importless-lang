import ast

class Walker(ast.NodeVisitor):
    def __init__(self):
        self.seen = set() 
        self.discard = set()

    def visit_ClassDef(self, node):
        self.discard.add(node.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.discard.add(node.name)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.seen.add(node.id) 
        if isinstance(node.ctx, ast.Store):
            self.discard.add(node.id) 
        self.generic_visit(node)

    def find_globals(self):
        return self.seen - self.discard


def find_globals(fileobject):
    tree = ast.parse(fileobject.read())
    walker = Walker()
    walker.visit(tree)
    return walker.find_globals(), tree

