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
        if not name:
            name = ''
        self.name = name


class Player(object):
    """
    A cricket player. The player can participate as a batter or a bowler (or
    both). Their statistics will be kept here.
    """

    def __init__(self, name):
        self.name = name
