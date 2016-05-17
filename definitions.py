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

FIRST_FLOOR = [kitchen, diningRoom, livingRoom]
OUTSIDE = [frontPorch, garageOutdoor, lightPost]


