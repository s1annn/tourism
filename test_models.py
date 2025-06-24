from models import Tourist, Beach, Mountain, City
import unittest

class TestTourist(unittest.TestCase):
    def setUp(self):
        self.tourist = Tourist("Tester", 50, "🙂")
        self.beach = Beach("Sunny Beach", 20, 5, "🏖️")

    def test_visit_enough_money(self):
        result = self.tourist.visit(self.beach)
        self.assertIn("visited", result)
        self.assertEqual(self.tourist.money, 30)
        self.assertEqual(self.tourist.experience, 5)

    def test_visit_not_enough_money(self):
        poor_tourist = Tourist("Poor", 10, "🙁")
        result = poor_tourist.visit(self.beach)
        self.assertIn("Not enough money", result)
        self.assertEqual(poor_tourist.money, 10)
        self.assertEqual(poor_tourist.experience, 0)

if __name__ == "__main__":
    unittest.main()