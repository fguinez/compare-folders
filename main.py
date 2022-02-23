from email.policy import default
from os import listdir
import argparse


def compare(path_1, path_2, show_all=False):
    if show_all:
        files1 = set(listdir(path_1))
        files2 = set(listdir(path_2))
    else:
        files1 = set(f for f in listdir(path_1) if not f.startswith("."))
        files2 = set(f for f in listdir(path_2) if not f.startswith("."))
    print("\n- Unique files in path 1:", path_1)
    unique1 = files1 - files2
    print(f"    ({len(unique1)} files)")
    for filename in unique1:
        print(filename)

    print("\n- Unique files in path 2:", path_2)
    unique2 = files2 - files1
    print(f"    ({len(unique2)} files)")
    for filename in unique2:
        print(filename)

    print("\n- Resume:")
    unique2 = files2 - files1
    print(f"    ({len(unique2)} files)")
    print("Total files in path 1:", len(files1))
    print("Total files in path 2:", len(files2))
    print("Unique files in path 1:", len(unique1))
    print("Unique files in path 2:", len(unique2))
    print("Common files:", len(files1.intersection(files2)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare two folders.')
    parser.add_argument('-a', '--all', action='store_true', default=False,
                        help='Include hidden files')
    parser.add_argument('path_1', type=str, help='Path of first folder')
    parser.add_argument('path_2', type=str, help='Path of second folder')
    args = parser.parse_args()
    print(args.all)
    compare(args.path_1, args.path_2, show_all=args.all)
