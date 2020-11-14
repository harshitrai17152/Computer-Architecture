from m5.params import *
from m5.SimObject import SimObject

class AddNumber(SimObject):
    type = 'AddNumber'
    cxx_header = "learning_gem5/add_number.hh"
