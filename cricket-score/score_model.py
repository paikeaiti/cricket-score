"""
"""


class Team(object):
    """
    A cricket team, with a minimum of 12 players. There may be more than 12,
    but during a game only a maximum of 12 will participate.
    """

    def __init__(self, name):
        """
        Create a new team, with the given name
        """
        self.name = name
        self.players = list()

    @property
    def num_players(self):
        return len(self.players)

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self,player):
        self.players.remove(player)


class Player(object):
    """
    A cricket player. The player can participate as a batter or a bowler (or
    both). Their statistics will be kept here.
    """

    def __init__(self, name, ident=None):
        self.name = name
        self.identifier = ident


class Ball(object):
    """
    The core interaction between the bowler and batter
    Due to 'illegal' bowling there may be more than one actual ball bowled
    for each ball. These extras need to be recorded as well,"""
    def __init__(self,player,runs):
        self.player = player
        self.runs = runs
