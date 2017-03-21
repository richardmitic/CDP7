#!/usr/bin/env python3

import unittest
import subprocess
import re
import os
import sys

def _is_fat(program):
    txt = str(subprocess.check_output(["lipo", "-info", program]), 'utf8')
    regex = r"(i386 x86_64|x86_64 i386)"
    return bool(re.search(regex, txt))

def make_test(program):
    def test(self):
        self.assertTrue(_is_fat(program), "{} is not fat".format(program))
    return test

class meta_TestFat(type):
  @classmethod
  def __prepare__(mcls, name, bases):
    d = dict()
    for root, dirs, files in os.walk("/Users/richard/Developer/CDP7/Release"):
        programs = [os.path.join(root, f) for f in files]
        for p in programs:
            test_name = "test_fat_{}".format(p)
            test = make_test(p)
            d[test_name] = test
    return d


class TestFat(unittest.TestCase, metaclass=meta_TestFat):
    @unittest.skip("Class must have at least one test")
    def test_thing(self):
        pass




if __name__ == '__main__':
    unittest.main()