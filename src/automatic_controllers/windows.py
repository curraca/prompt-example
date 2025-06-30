class Windows:
    """
    A class to represent a collection of windows in a building.
    """

    def __init__(self, windows):
        """
        Initializes the Windows object with a list of windows.

        :param windows: List of window objects.
        """
        self.windows = windows

    def get_windows(self):
        """
        Returns the list of windows.

        :return: List of window objects.
        """
        return self.windows