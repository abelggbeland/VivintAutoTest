import requests
from requests.auth import HTTPBasicAuth
import json

class data:
    def __init__(self, BadgeID, Assets, Peripherals, PeripheralsAdds):
        self.__BadgeID = BadgeID
        self.__Assets = Assets
        self.__Peripherals = Peripherals
        self.__PeripheralsAdds = PeripheralsAdds

    def getBadgeID(self):
        return self.__BadgeID

    def getAssets(self):
        return self.__Assets

    def getPeripherals(self):
        yes = []
        for i in range(len(self.__Peripherals)):
            if self.__Peripherals[i] == "yes":
                yes.append(self.__PeripheralsAdds[i])
        return yes

    def getPeripheralsAdda(self):
        return self.__PeripheralsAdds

