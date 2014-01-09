"""
Virtual Modules

Contains utilities to define virtual modules
"""

class VirtualModule(object):
    def __new__(cls, ns={}):
        self = super(VirtualModule, cls).__new__()
        self.__dict__.update(ns)
        return self

def vimport(vmod):
    """
    "Import" a virtual module into the global package cache
    """
    pass