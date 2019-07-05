#!/usr/bin/env python
import sys
from termcolor import colored

try:
   text = sys.argv[1]
   print(text.lower().replace("a", "i").replace("e", "i").replace("o", "i").replace("u", "i"))
except:
   print(colored('Debe introducir un mansaje','red'))
