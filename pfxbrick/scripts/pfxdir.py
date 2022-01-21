#! /usr/bin/env python3
"""
pfxdir - shows the PFx Brick file directory listing
"""
import argparse

from pfxbrick import *
from pfxbrick.pfxhelpers import get_one_pfxbrick


def main():
    parser = argparse.ArgumentParser(
        description="PFx Brick file directory listing",
        prefix_chars="-+",
    )
    parser.add_argument(
        "-s",
        "--serialno",
        default=None,
        help="Specify PFx Brick with serial number (if more than one connected)",
    )
    args = parser.parse_args()
    argsd = vars(args)

    b = get_one_pfxbrick(argsd["serialno"])
    r = b.open()
    if not r:
        exit()
    b.refresh_file_dir()
    print(b.filedir)
    b.close()


if __name__ == "__main__":
    main()
