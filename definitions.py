# switchObj class is used to define switches
# address is a string and must be formatted properly: 'XX XX XX X'
#    single switches will always end with 1
#    do not include a leading 0 in a pair of characters
#    example: address 123405 would be 12 34 5 1 - note the trailing 1 for a single switch
# name is a string and must match the names in your .html files in the /templates directory
# slave is a Switch object and is only used if the switch has slave switches
#    this is used for three- or more way switches
class switchObj:
    address = ''
    name = ''
    slave = None

    def __init__(self):
        self.name = ''

    def __init__(self, name, address, slave=None):
        self.name = name
        self.address = address
        self.slave = slave

# First Floor Switches
kitchen = switchObj('Kitchen','38 1C 89 1',switchObj('Kitchen','38 18 E0 1'))
diningRoom = switchObj('DiningRoom','38 27 D9 1',switchObj('DiningRoom','38 1F 74 1'))
livingRoom = switchObj('LivingRoom','38 F 43 1',switchObj('LivingRoom','38 18 F2 1'))

# Outside Switches
frontPorch = switchObj('FrontPorch','38 A0 AA 1')
garageOutdoor = switchObj('GarageOutdoor','38 9E 37 1')
lightPost = switchObj('LightPost','38 F 84 1')

ISYADDRESS = 'http://10.0.0.1/rest/'
ISYADMIN = 'admin'
ISYPASSWORD = 'password'

# Use the python variable names from above and include them in the proper
# group (Python list) below.
FIRST_FLOOR = [kitchen, diningRoom, livingRoom]
OUTSIDE = [frontPorch, garageOutdoor, lightPost]
