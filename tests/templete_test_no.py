
"""Unittest."""


import unittest

from random import randint


# Random order for tests runs. (Original is: -1 if x<y, 0 if x==y, 1 if x>y).
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: randint(-1, 1)


def setUpModule():
    pass


def tearDownModule():
    pass


class TestName(unittest.TestCase):

    """Unittest."""
    
    maxDiff, __slots__ = None, ()

    def setUp(self):
        """Method to prepare the test fixture. Run BEFORE the test methods."""
        pass

    def tearDown(self):
        """Method to tear down the test fixture. Run AFTER the test methods."""
        pass

    def addCleanup(self, function, *args, **kwargs):
        """Function called AFTER tearDown() to clean resources used on test."""
        pass

    @classmethod
    def setUpClass(cls):
        """Class method called BEFORE tests in an individual class run. """
        pass  # Probably you may not use this one. See setUp().

    @classmethod
    def tearDownClass(cls):
        """Class method called AFTER tests in an individual class run. """
        pass  # Probably you may not use this one. See tearDown().

    @unittest.skip("Demonstrating skipping")  # Skips this test only
    @unittest.skipIf("boolean_condition", "Reason to Skip Test here.")  # Skips this test only
    @unittest.skipUnless("boolean_condition", "Reason to Skip Test here.")  # Skips this test only
    @unittest.expectedFailure  # This test MUST fail. If test fails, then is Ok.
    def test_dummy(self):
        self.skipTest("Just examples, use as template!.")  # Skips this test only
        self.assertEqual(a, b)  # a == b
        self.assertNotEqual(a, b)  # a != b
        self.assertTrue(x)  # bool(x) is True
        self.assertFalse(x)  # bool(x) is False
        self.assertIs(a, b)  # a is b
        self.assertIsNot(a, b)  # a is not b
        self.assertIsNone(x)  # x is None
        self.assertIsNotNone(x)  # x is not None
        self.assertIn(a, b)  # a in b
        self.assertNotIn(a, b)  # a not in b
        self.assertIsInstance(a, b)  # isinstance(a, b)
        self.assertNotIsInstance(a, b)  # not isinstance(a, b)
        self.assertAlmostEqual(a, b)  # round(a-b, 7) == 0
        self.assertNotAlmostEqual(a, b)  # round(a-b, 7) != 0
        self.assertGreater(a, b)  # a > b
        self.assertGreaterEqual(a, b)  # a >= b
        self.assertLess(a, b)  # a < b
        self.assertLessEqual(a, b)  # a <= b
        self.assertRegex(s, r)  # r.search(s)
        self.assertNotRegex(s, r)  # not r.search(s)
        self.assertItemsEqual(a, b)  # sorted(a) == sorted(b) and works with unhashable objs
        self.assertDictContainsSubset(a, b)  # all the key/value pairs in a exist in b
        self.assertCountEqual(a, b)  # a and b have the same elements in the same number, regardless of their order
        # Compare different types of objects
        self.assertMultiLineEqual(a, b)  # Compare strings
        self.assertSequenceEqual(a, b)  # Compare sequences
        self.assertListEqual(a, b)  # Compare lists
        self.assertTupleEqual(a, b)  # Compare tuples
        self.assertSetEqual(a, b)  # Compare sets
        self.assertDictEqual(a, b)  # Compare dicts
        # To Test code that MUST Raise Exceptions:
        self.assertRaises(SomeException, callable, *args, **kwds)  # callable Must raise SomeException
        with self.assertRaises(SomeException) as cm:
            do_something_that_raises() # This line  Must raise SomeException
        # To Test code that MUST Raise Warnings (see std lib warning module):
        self.assertWarns(SomeWarning, callable, *args, **kwds)  # callable Must raise SomeWarning
        with self.assertWarns(SomeWarning) as cm:
            do_something_that_warns() # This line  Must raise SomeWarning
        # Assert messages on a Logger log object.
        self.assertLogs(logger, level)
        with self.assertLogs('foo', level='INFO') as cm:
            logging.getLogger('foo').info('example message')  # cm.output is 'example message'


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
    # Run just 1 test.
    # unittest.main(defaultTest='TestFoo.test_foo', warnings='ignore')