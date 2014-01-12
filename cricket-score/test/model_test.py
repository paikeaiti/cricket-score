"""
"""
import unittest
from score_model import Team


class TestTeam(unittest.TestCase):
    """
    Test functionality of the cricket team
    """

    def testCreation(self):
        team = Team()
        self.assertEqual('', team.name)



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testTeam']
    unittest.main()
