#!/usr/bin/env python
import sys
from flaskmng.__main__ import main

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("flaskmng")
    main()