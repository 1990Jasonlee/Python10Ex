import unittest
import small_town_teller

class SmallTownTellerTest(unittest.TestCase):
    def setUp(self) -> None:
        self._john = small_town_teller.Person(1, 'John', 'Smith')
        self._jane = small_town_teller.Person(2, 'Jane', 'Doe')
        self._walter = small_town_teller.Person(1, 'Walter', 'White')
        self._john_checking = small_town_teller.Account(123, 'CHECKING', self._john)
        self._jane_savings = small_town_teller.Account(456, 'SAVINGS', self._jane)
        self._walter_checking = small_town_teller.Account(123, 'CHECKING', self._walter)
        self._bank = small_town_teller.Person()

    def test_person_initialization(self):
        expected_id = 1
        expected_first_name = 'John'
        expected_las_name = 'Smith'

        self.assertEqual(expected_id, self._john.id)
        self.assertEqual(expected_first_name, self._john.first_name)
        self.assertEqual(expected_las_name, self._john.last_name)

    def test_account_initialization(self):
        expected_number = 123
        expected_type = 'CHECKING'
        expected_owner = 'id: 1. owner: John Smith'
        expected_balance = 0

        self.assertEqual(expected_number, self._john_checking.number)
        self.assertEqual(expected_type, self._john_checking.type)
        self.assertEqual(expected_owner, str(self._john_checking.owner))
        self.assertEqual(expected_balance, self._john_checking.balance)




if __name__ == '__main__':
    unittest.main()
