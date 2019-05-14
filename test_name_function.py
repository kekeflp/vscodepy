# _*_ coding:utf-8 _*_

from name_function import get_formatted_name
import unittest


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin","ewad")
        self.assertEqual(formatted_name, "Janis Ewad Joplin")

unittest.main()
 