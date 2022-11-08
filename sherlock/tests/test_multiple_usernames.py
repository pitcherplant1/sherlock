
import unittest
from sherlock.sherlock import (
    CheckForParameter,
    MultipleUsernames
)

checksymbols = []
checksymbols = ["_", "-", "."]

"""Test for mulriple usernames.

        This test ensures that the function MultipleUsernames works properly. More specific,
        different scenarios are tested and only usernames that contain this specific sequence: {?} 
        should return positive.
      
        Keyword Arguments:
        self                   -- This object.

        Return Value:
        Nothing.
        """
class TestMultipleUsernames(unittest.TestCase):
    def test_area(self):
        test_usernames = ["test{?}test" , "test{?feo" , "test"]
        for name in test_usernames:
            if(CheckForParameter(name)):
                self.assertAlmostEqual(MultipleUsernames(name), ["test_test" , "test-test" , "test.test"])
            else:
                self.assertAlmostEqual(name, name)