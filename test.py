#!/usr/bin/env python
import sys
import os
from flaskmng.__main__ import command_line_interface
os.chdir('./test')

if __name__ == '__main__':
    command_line_interface()