import unittest
from adventure import Tourist, City, Beach, Mountain

class TestAdventureGame(unittest.TestCase):

    def setUp(self):
        self.tourist = Tourist(name="Alice", money=100, avatar="🧔🏻")
        self.city = City(name="Paris", cost=20, experience=10, emoji="🗼")
        self.beach = Beach(name="Maldives", cost=20, experience=5, emoji="🏝️")
        self.mountain = Mountain(name="Everest", cost=50, experience=25, emoji="🗻")

    def test_gain_experience_and_level_up(self):
        self.tourist.gain_experience(150)
        self.assertEqual(self.tourist.experience, 150)
        self.assertEqual(self.tourist.level, 2)

    def test_city_interaction_adds_souvenir(self):
        initial_inventory = len(self.tourist.inventory)
        self.tourist.money = 100
        result = self.tourist.visit(self.city)
        self.assertIn("Souvenir from Paris", self.tourist.inventory)
        self.assertEqual(len(self.tourist.inventory), initial_inventory + 1)
        self.assertIn("gained", result)

    def test_beach_interaction_adds_experience(self):
        result = self.tourist.visit(self.beach)
        self.assertEqual(self.tourist.experience, 5)
        self.assertEqual(self.tourist.money, 80)
        self.assertIn("relaxed", result)

    def test_mountain_interaction_adds_more_experience(self):
        result = self.tourist.visit(self.mountain)
        expected_exp = int(25 * 1.5)
        self.assertEqual(self.tourist.experience, expected_exp)
        self.assertEqual(self.tourist.money, 50)
        self.assertIn("climbed", result)

    def test_visit_fails_if_not_enough_money(self):
        self.tourist.money = 10
        result = self.tourist.visit(self.city)
        self.assertEqual(result, "Not enough money to visit Paris.")
        self.assertEqual(self.tourist.experience, 0)
        self.assertEqual(self.tourist.money, 10)

if __name__ == '__main__':
    unittest.main()
