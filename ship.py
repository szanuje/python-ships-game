class Ship:
    """Class represent a ship"""

    def __init__(self):
        self.masts = []

    def num_of_masts(self):
        """:returns len of masts list"""
        return len(self.masts)
