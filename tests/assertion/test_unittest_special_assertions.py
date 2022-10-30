import unittest
import math


def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))


class ExceptionTest(unittest.TestCase):

    def test_div_zero_exception(self):
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_keyerror_details(self):
        my_map = {"foo": "bar"}

        with self.assertRaises(KeyError):
            _ = my_map["baz"]

    def test_approximate_matches(self):
        assert math.isclose(0.3, 0.1 + 0.2)

    def test_trap_locally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass

    def test_assert_raises(self):
        self.assertRaises(ValueError, raises_error, 'a', b='c')


if __name__ == '__main__':
    unittest.main()