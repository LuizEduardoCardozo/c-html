#!/usr/bin/env python3

from sys import argv as arg
from cHTML import cHTML
from pathlib import Path


def main(arg):
    if(len(arg) != 3):
        print("Usage: {} <html_source> <build_folder>".format(arg[0]))
        exit(1)

    htmlFile = Path(arg[1])
    buildFolder = Path(arg[2])

    outputHTML = buildFolder.joinpath(htmlFile)

    cHTML(htmlFile,outputHTML)

if __name__ == "__main__":
    main(arg)
