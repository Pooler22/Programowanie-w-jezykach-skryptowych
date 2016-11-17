import unittest
from lab.database.Database import Database
from lab.database.Record import Record


class DatabaseTestClass(unittest.TestCase):
    def test_construct(self):
        db = Database()
        self.assertEqual(db.base, [])
        self.assertEqual(db.name, "")

    def test_load_save_db(self):
        test = "test"
        db1 = Database()
        db2 = Database()

        db1.name = test
        self.assertNotEquals(db1, db2)

        db1.save(test)
        db2.load(test)
        self.assertEqual(db1, db2)

    def test_load_from_file_data(self):
        txt = "test_file.txt"
        none = ""

        db1 = Database()
        self.assertEquals(db1.base, [])
        self.assertEquals(db1.name, none)
        self.assertEquals(db1.file_name, none)

        db1.load_from_file(txt)
        self.assertEquals(db1.file_name, txt)

    def test_add_record(self):
        sample1 = "asd"
        sample2 = "dsa"
        sample_id = 0
        db1 = Database()

        self.assertEquals(db1.base.__len__(), 0)

        db1.add_record(sample1, sample2)
        self.assertEquals(db1.base.__len__(), 1)
        self.assertEquals(db1.base[0], Record(sample_id, sample1, sample2))

    def test_autoincrement(self):
        tmp = []
        for i in range(1, 100):
            tmp.append(Database.auto_increment())

        for i in range(1, 100):
            for j in range(i+1, 100-1):
                self.assertNotEquals(tmp[i], tmp[j])

    def test_remove_record(self):
        db = Database()
        self.assertEquals(db.base.__len__(), 0)

        db.add_record("asd", "dsa")
        self.assertEquals(db.base.__len__(), 1)

        db.remove_record(0)
        self.assertEquals(db.base.__len__(), 0)


if __name__ == '__main__':
    unittest.main()
