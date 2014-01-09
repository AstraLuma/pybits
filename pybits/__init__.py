"""
Embed a little bit of Python
"""

class Drawer(object):
    """
    Segregates bits into their own package namespaces.

    The biggest thing done is that efforts are made to make module imports unique.
    """
    def __new__(cls, name):
        # TODO: Singleton by name
        self = super(Drawer, cls).__new__()
        return self

    def __init__(self, name):
        self.name = name

    def compile(self, txt):
        """
        Creates a bit from a string, using this drawer's state
        """

    def addvmod(self, vmod):
        """
        Adds a virtual module to be available for bits in this drawer
        """

compile = Drawer(None).compile
addvmod = Drawer(None).addvmod