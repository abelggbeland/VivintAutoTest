import Data
import Sender
import os
import base64
import APICalls


def main():
    #Chech to see if Auth file exist
    if not os.path.exists("Credentials"):
        f = open("Credentials", "w+")
        #ask for login
        email = input("Enter email: ")
        APIKey = input("Enter API Key: ")
        f.write(base64.b64encode(email.encode()).decode() + "\n")
        f.write(base64.b64encode(APIKey.encode()).decode())
        f.close()


    BadgeID = input("Please enter Badge ID")
    Assets = []
    Peripherals = []
    PeripheralsAdds = ["Keyboard", "Mouse", "Headset"]

    def getAssetNumbers(Asset):
        #TODO add checks
        if Asset != "X":
            Assets.append(Asset)
            getAssetNumbers(input("Please scan asset number"))

    getAssetNumbers(input("Please scan asset number"))

    def getPeripherals(PeripheralsAdds):
        # TODO add checks
        for Peripheral in range(len(PeripheralsAdds)):
            read = input("enter yes or no if you have a " + PeripheralsAdds[Peripheral])
            Peripherals.append(read)

    getPeripherals(PeripheralsAdds)

    data = Data.data(BadgeID, Assets, Peripherals, PeripheralsAdds)
    Sender.send(APICalls.makeIssue(data), "https://vivint.atlassian.net/rest/api/3/issue")

    #TODO setup data

main()