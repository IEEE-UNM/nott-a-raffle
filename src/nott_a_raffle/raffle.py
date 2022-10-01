#!/usr/bin/env python3
import random
import csv
from collections import defaultdict


class Raffle(defaultdict):
    """Class used for a raffle draw.

    Parameters
    ----------
    names: list[str]
        The names of the contestants
    tickets: list[int]
        How many tickets the contestants have
    """
    def __init__(self, names: list[str], tickets: list[int]):
        super().__init__(int)

        # Checking Lengths
        if not len(names) == len(tickets):
            raise ValueError("Length of name and tickets must be the same")

        # Adding ticket counts
        for name, ticket in zip(names, tickets):
            if int(ticket) < 0:
                continue
            else:
                self[name] += int(ticket)

    @classmethod
    def from_csv(cls, file: str, name: str = "Name", ticket: str = "Tickets"):
        """Gets data from a csv file.

        Parameters
        ----------
        file: str
            CSV file name
        name: str
            The label where the names are stored
        ticket: str
            The label where the number of tickets are stored
        """
        names = []
        tickets = []
        # Extracting Information
        with open(file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                names.append(row[name])
                tickets.append(int(row[ticket]))

        return cls(names, tickets)

    def draw(self, k: int = 1) -> list[str]:
        """Draws k winners.

        Parameters
        ----------
        k: int
            The number of winners

        Returns
        -------
        list[str]
            The winners
        """
        return random.sample(list(self.keys()), k, counts=list(self.values()))
