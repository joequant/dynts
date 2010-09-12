VERSION = (0, 1, 'a2')
 
def get_version():
    if len(VERSION) == 3:
            v = '%s.%s.%s' % VERSION
    else:
        v = '%s.%s' % VERSION[:2]
    return v
 
__version__  = get_version()
__license__  = "BSD"
__author__   = "Luca Sbardella"
__contact__  = "luca@quantmind.com"
__homepage__ = "http://github.com/quantmind/dynts/"


from backends import timeserie, BACKENDS
from data import providers, TimeSerieLoader
from dsl import parse


def get(symbols, start = None, end = None, provider = None):
    if not hasattr(symbols,'__iter__'):
        symbols = [symbols]
    res = providers.load(symbols, start, end, provider = provider)
    return res


def evaluate(e, start = None, end = None, variables = None):
    '''Evaluate expression *e*.
     * *e* instance of :ref:`Expr <expr>' obtained using the parse function.
     * *start* start date
     * *end* end date
     * *variables* dictionary of variables to replace strings
    '''
    variables = variables or {}
    symbols = e.symbols()
    data = providers.load(symbols, start, end)
    
    
def add2path():
    import os
    import sys
    path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    if path not in sys.path:
        sys.path.insert(0,path)
        
def runtests():
    import unittest
    add2path()
    from dynts import tests
    loader = unittest.TestLoader()
    suite  = loader.loadTestsFromModule(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)