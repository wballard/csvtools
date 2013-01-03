"""
All about the columns in a CSV file.
"""

import csv
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='List the column names from a CSV file')
    parser.add_argument(
        'csv_file',
        help='name of a csv file to read, if unspecified this will read from sys.stdin',
        nargs='?',
        default='-',
    )
    args = parser.parse_args()
    read_from = sys.stdin if args.csv_file == '-' else open(args.csv_file)
    #assume the first row is csv
    for row in csv.reader(read_from):
        for column in row:
            print column
        sys.exit(0)
