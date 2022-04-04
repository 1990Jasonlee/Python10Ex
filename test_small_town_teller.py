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
if __name__ == '__main__':
    unittest.main()
