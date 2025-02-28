import sys
def sample_function():
    1/0
    
def another_function(e : Exception):
    sys.excepthook(type(e), e, e.__traceback__)