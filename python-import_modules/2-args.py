#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    argLen = len(args)
    
    if argLen == 0:
        print("0 arguments.")
    elif argLen == 1:
        print("1 argument:")
        print(f"1: {args[0]}")
