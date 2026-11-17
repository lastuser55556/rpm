import unittest
from booking import BookingBook


class BookingTests(unittest.TestCase):
    def test_limit_and_reuse(self):
        book = BookingBook()
        for i in range(4):
            self.assertTrue(book.reserve("09:00", i))
        self.assertFalse(book.reserve("09:00", 4))
        self.assertTrue(book.cancel("09:00", 2))
        self.assertTrue(book.reserve("09:00", 4))
        self.assertFalse(book.reserve("09:00", 5))

    def test_times_independent(self):
        book = BookingBook()
        for i in range(4):
            book.reserve("09:00", i)
        self.assertTrue(book.reserve("10:00", 5))

    def test_repeat_and_missing(self):
        book = BookingBook()
        self.assertTrue(book.reserve("09:00", 20))
        self.assertFalse(book.reserve("09:00", 20))
        self.assertFalse(book.cancel("10:00", 20))
        self.assertTrue(book.cancel("09:00", 20))
        self.assertFalse(book.cancel("09:00", 20))


if __name__ == "__main__":
    unittest.main()
