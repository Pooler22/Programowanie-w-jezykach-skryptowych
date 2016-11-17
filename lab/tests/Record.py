import unittest
from lab.database.Record import Record


class RecordTestCase(unittest.TestCase):
    def test_something(self):
        sample1 = 1
        sample2 = "name"
        sample3 = "surname"
        sample4 = "234234"
        sample5 = "a@a.com"
        empty = ""

        r = Record(sample1, sample2, sample3)
        self.assertEquals(r.id, sample1)
        self.assertEquals(r.name, sample2)
        self.assertEquals(r.surname, sample3)
        self.assertEquals(r.number, empty)
        self.assertEquals(r.email, empty)

        r = Record(sample1, sample2, sample3, sample4, sample5)
        self.assertEquals(r.id, sample1)
        self.assertEquals(r.name, sample2)
        self.assertEquals(r.surname, sample3)
        self.assertEquals(r.number, sample4)
        self.assertEquals(r.email, sample5)

    def test_eq(self):
        id1 = 0
        id2 = 1
        name1 = "asd"
        name2 = "dsa"
        surname1 = "zxc"
        surname2 = "das"

        r1 = Record(id1, name1, surname1)
        r2 = Record(id2, name1, surname1)
        self.assertEquals(r1, r2)

        r3 = Record(id1, name2, surname2)
        self.assertNotEquals(r1, r3)

        self.assertNotEquals(r2, r3)

if __name__ == '__main__':
    unittest.main()
