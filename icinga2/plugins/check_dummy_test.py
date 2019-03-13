#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from check_dummy import CheckDummy


class CheckDummyTest(unittest.TestCase):
    def test_check(self):
        check = CheckDummy()
        ret = check.perform()
        self.assertEqual(0, ret)


if __name__ == "__main__":
    unittest.main()
