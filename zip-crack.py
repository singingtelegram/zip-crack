#!/usr/bin/env python3

import zipfile
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZIP password bruteforce utility")
    parser.add_argument("zipfile", help="Path to ZIP file")
    parser.add_argument("wordlist", help="Path to wordlist")
    args = parser.parse_args()
    wordlist = open(args.wordlist, "r")
    passwords = wordlist.read().split()
    with zipfile.ZipFile(args.zipfile, "r") as archive:
        for ele in passwords:
            try:
                archive.extractall(pwd=ele.encode())
                print("Password found: {}".format(ele))
                break
            except Exception as e:
                #print("Error caught: {} {}".format(e, ele.encode()))
                continue
    
    archive.close()
    wordlist.close()

