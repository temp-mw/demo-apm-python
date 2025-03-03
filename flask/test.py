import sys
import random

def sample_function(error_type: int):
    errors = [
        ZeroDivisionError("Division by zero"),
        TypeError("Invalid type operation"),
        NameError("Variable is not defined"),
        SyntaxError("Invalid syntax"),
        ValueError("Wrong value provided"),
        IndexError("Index out of range"),
        KeyError("Key not found in dictionary"),
        OverflowError("Number too large"),
        MemoryError("Out of memory"),
        RuntimeError("General runtime error"),
        AttributeError("Attribute not found"),
        NotImplementedError("Functionality not implemented"),
        FileNotFoundError("File not found"),
        PermissionError("Permission denied"),
        AssertionError("Assertion failed"),
        EOFError("End of file reached"),
        ReferenceError("Weak reference error"),
        UnicodeError("Unicode encoding/decoding error"),
        BufferError("Buffer operation error"),
        SystemError("Internal system error"),
    ]
    if 1 <= error_type <= 20:
        raise errors[error_type - 1]
    else:
        raise random.choice(errors)

def another_function(e: Exception):
    sys.excepthook(type(e), e, e.__traceback__)