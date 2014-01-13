"""
"""
import unittest
from score_model import Team
from score_model import Player
from score_model import Ball


class TestTeam(unittest.TestCase):
    """
    Test functionality of the cricket team
    """

    def setUp(self):
        self.team_name = 'The Team'
        self.team = Team(self.team_name)
        self.player_name = 'A Player'
        self.player = Player(self.player_name)
        self.another_player_name = 'Another Player'
        self.another_player = Player(self.another_player_name)

    def test_creation(self):
        otago_name = 'Otago'
        team = Team(otago_name)
        self.assertEqual(otago_name, team.name)
        self.assertEqual(0, team.num_players)

    def test_adding_player(self):
        self.assertEqual(0, self.team.num_players)
        self.team.add_player(self.player)
        self.assertEqual(1, self.team.num_players)

    def test_adding_2_player(self):
        self.assertEqual(0, self.team.num_players)
        self.team.add_player(self.player)
        self.team.add_player(self.another_player)
        self.assertEqual(2, self.team.num_players)

    def test_removing_2_player(self):
        self.assertEqual(0, self.team.num_players)
        self.team.add_player(self.player)
        self.team.add_player(self.another_player)
        self.team.remove_player(self.player)
        self.team.remove_player(self.another_player)
        self.assertEqual(0, self.team.num_players)

class TestPlayer(unittest.TestCase):
    """
    Test functionality of the cricket player
    """

    def test_creation(self):
        player_name = 'A Player'
        player_ident = '20'
        player = Player(player_name)
        player.identifier = player_ident
        self.assertEqual(player_name,player.name)
        self.assertEqual(player_ident, player.identifier)

    def test_creation_with_ident(self):
        player_name = 'A Player'
        player_ident = '20'
        player = Player(player_name, player_ident)
        self.assertEqual(player_name, player.name)
        self.assertEqual(player_ident, player.identifier)


class BallTest(unittest.TestCase):
    """
    Test functionality of a ball being bowled
    """

    def setUp(self):
        self.player = Player('A Player')

    def test_creation(self):
        ball = Ball(self.player,0)
        self.assertEqual(0,ball.runs)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testTeam']
    unittest.main()
