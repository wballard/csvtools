import csv
import sys
import argparse


def main():
    parser = argparse.ArgumentParser(description='Cut the specified columns from a CSV file')
    parser.add_argument(
        'csv_file',
        help='name of a csv file to read, if unspecified this will read from sys.stdin',
        nargs='?',
        default='-',
    )
    parser.add_argument(
        '--named',
        help='named columns to cut from a CSV, this assumes a first row with column names',
        nargs='*',
    )
    args = parser.parse_args()
    read_from = sys.stdin if args.csv_file == '-' else open(args.csv_file)
    if args.named:
        writer = csv.DictWriter(sys.stdout, args.named)
        writer.writeheader()
        for row in csv.DictReader(read_from):
            out_row = {key: row[key] for key in args.named}
            writer.writerow(out_row)
