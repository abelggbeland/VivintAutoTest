class data:
    def __init__(self, Name, BadgeID, Assets, Peripherals):
        self.__Name = Name
        self.__BadgeID = BadgeID
        self.__Assets = Assets
        self.__Peripherals = Peripherals

    def getBadgeID(self):
        return self.__BadgeID

    def getName(self):
        return self.__Name

    def getAssets(self):
        return self.__Assets

    def getPeripherals(self):
        return self.__Peripherals

