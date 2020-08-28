import Data
import Sender

def main():
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
    Sender.send(data)

    #TODO setup data

main()