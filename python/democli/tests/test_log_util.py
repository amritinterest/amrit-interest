import unittest
from vserver_cli.utils.log_util import print_with_color, Color


class Test(unittest.TestCase):
    def test_log_util_print_with_color(self):
        """ Test print_with_color"""
        print_with_color("Hello", Color.BLUE)
