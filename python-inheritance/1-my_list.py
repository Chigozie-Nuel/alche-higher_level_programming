#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""


class MyList(list):
    """MyList inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original list."""
        print(sorted(self))
