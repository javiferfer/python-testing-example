def test_empty():
    """
    PyTest tests are callables whose names start with "test"
    (by default)
    It looks for them in modules whose name starts with "test_" or ends with "_test"
    (by default)
    """
    pass


def empty_test():
    """
    My name doesn't start with "test", so I won't get run.
    (by default ;-)
    """
    pass


def test_comparing_dict():
    """
    But really, test cases should be callables containing assertions:
    """
    print("\nRunning test_example...")

    DATA_SET_A = {
        "Foo": "Bar",
        "Baz": [5, 7, 11],
        "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
    }

    DATA_SET_B = DATA_SET_A
    
    DATA_SET_C = {
        "Foo": "Bar",
        "Baz": [3, 5, 7],
        "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
    }

    assert DATA_SET_A == DATA_SET_B
    assert DATA_SET_A != DATA_SET_C
