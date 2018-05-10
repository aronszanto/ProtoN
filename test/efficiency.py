#!/usr/bin/env python3
from sys import argv, exit
from os.path import isdir, join
from os import listdir
from subprocess import check_output
from json import load, dumps
from encoder import *
from decoder import *

def usage():
    """ Bad CLI options passed """
    print("Usage:", argv[0], "directory")
    exit()

def main():
    """ Main point of entry for CLI """
    # Check for correct arguments
    if len(argv) != 2 or not isdir(argv[1]):
        usage()
    dir = argv[1]
    json_sz = 0
    proton_sz = 0
    for filename in listdir(dir):
        if filename.endswith(".json"):
            with open(join(dir,filename), 'r') as f:
                obj = load(f)
            # Add size of JSON without added whitespace
            this_json = len(dumps(obj, separators=(',',':')).encode('utf-8'))
            json_sz += this_json
            # Add size of ProtoN
            this_proton = len(encode(obj))
            proton_sz += this_proton
            print("Testing \u001b[1m" + filename +
                    "\u001b[0m JSON:", this_json, "ProtoN:", this_proton,
                    "   \u001b[33m" + str(this_proton/this_json) + "\u001b[0m")
    # Print Results
    print("\n" + ('-'*30))
    print("\n\u001b[33mProtoN/JSON Size:", proton_sz/json_sz, "\u001b[0m")
    print("\n" + ('-'*30))

if __name__ == '__main__':
    main()