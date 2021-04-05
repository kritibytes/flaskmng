#!/usr/bin/env python
import sys
import os
from flaskmng.__main__ import main
os.chdir('./test')

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("flaskmng")
    try:
        main()
    except Exception as e:
        print("❌ "+str(e))