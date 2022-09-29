#!/usr/bin/env python3
import argparse
from .raffle import Raffle


def parse_arguments():
    parser = argparse.ArgumentParser(description='Program that does a raffle'
                                     ' draw')

    parser.add_argument("csv", help="CSV file to use.")
    parser.add_argument("-n", "--name", help="The label where the names are"
                        " stored.", default="Name")
    parser.add_argument("-t", "--ticket", help="The label where the number of"
                        "tickets are stored.", default="Tickets")
    parser.add_argument("-c", "--count", help="How many people to draw",
                        default=1, type=int)

    return parser.parse_args()


def main():
    args = parse_arguments()

    raffle = Raffle.from_csv(args.csv, args.name, args.ticket)
    print(raffle.draw(args.count))

    return 0
