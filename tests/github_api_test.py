import github_activity
import unittest

class MyTestCase(unittest.TestCase):

    def test_valid_user(self):
        events = github_activity.get_user_activity("cxyeat")
        self.assertIsNotNone(events, list)
        self.assertEqual(len(events),0)

    def test_invalid_user(self):
        with self.assertRaises(Exception):
            github_activity.get_user_activity("mwdmefndmsdnecfxmcenxm")


if __name__ == '__main__':
    unittest.main()
