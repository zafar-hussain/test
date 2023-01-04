"""
     _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
import math
import sys
from typing import Union


def example1():
    """
    example1 _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """

    some_tuple = (1, 2, 3, "a")
    some_variable = {
        "long": "Long code lines should be wrapped within 79 characters.",
        "other": [
            math.pi,
            100,
            200,
            300,
            9876543210,
            "This is a long string that goes on",
        ],
        "more": {
            "inner": "This whole logical line should be wrapped.",
            some_tuple: [1, 20, 300, 40000, 500000000, 60000000000000000],
        },
    }
    return (some_tuple, some_variable)


def example2():
    """
    example2 _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    return {"has_key() is deprecated": True}.has_key({"f": 2}.has_key(""))


class Example3(object):
    """
    Example3 _summary_

    _extended_summary_

    Args:
        object (_type_): _description_
    """
    def init(self, _bar: int) -> Union[int, tuple[list[str], str]]:
        """
        TODO:
        """


        if _bar:
            _bar += 1
            _bar = _bar * _bar
            return _bar
        else:
            some_string: str = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
            return (sys.path, some_string)
