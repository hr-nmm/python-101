"""# import smart_door as sd

# sd.open()
# sd.close()"""

### If a func will be called multiple times in the scrpit the doing [namespace.func()] is tedious, use "from X import Y"
from smart_door import open, close

open()
close()
open()

#  Shadowing Problem: open() is also built-in python func

"""# somefile = open("data.txt", "r")
###...work with the file...
# somefile.close()"""
### => Type Error: open() takes no args
### the built-in open() function has been shadowed by smart_door.open()

## from smart_door import open as door_open, close as door_close   ==> now shadowing will not take place and the earlier code of some file opening and closing will work fine.


## BEWARE OF IMPORTING ALL * =>  open(), smart_door.open(), and gzip.open() all exist and are fighting over the same name in your file! ANd gzip.open() wins and shadows the other two coz twas imported last
"""
from smart_door import *
from gzip import *
open()
"""
