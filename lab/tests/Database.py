import unittest
import lab.Database


class DatabaseTestClass(unittest.TestCase):
    def construct(self):
        database = lab.Database.Database()
        self.assertEqual(database.base_dict, {})
        self.assertEqual(database.base_name, "")


if __name__ == '__main__':
    unittest.main()
