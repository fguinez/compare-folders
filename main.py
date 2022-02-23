from os import listdir
import argparse


def compare(path_1, path_2):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare two folders.')
    parser.add_argument('path_1', type=str, help='Path of first folder')
    parser.add_argument('path_2', type=str, help='Path of second folder')
    args = parser.parse_args()

    compare(args.path_1, args.path_2)
