class Mobile:
    def __init__(self, companyName, storage, serialNum, name, dualSim, support4K):
        self.companyName = companyName
        self.storage = storage
        self.serialNum = serialNum
        self.name = name
        self.dualSim = dualSim
        self.support4K = support4K

    def call(self, recipient):
        print(f"{self.name} is calling {recipient}.")

    def sendMessage(self, recipient, message):
        print(f"{self.name} sends a message to {recipient}: {message}.")

    def playMedia(self, media):
        if self.support4K:
            print(f"{self.name} plays {media} in 4K resolution.")
        else:
            print(f"{self.name} plays {media}.")

    def info(self):
        print(f"Mobile Info: {self.name} by {self.companyName}, Serial Number: {self.serialNum}, Storage: {self.storage}GB, Dual SIM: {self.dualSim}, 4K Support: {self.support4K}")

# Example Test
mobile1 = Mobile(companyName="Apple", storage=128, serialNum=123456789, name="iPhone 13", dualSim=False, support4K=True)

mobile1.info()
mobile1.call("John")
mobile1.sendMessage("Jane", "Hello!")
mobile1.playMedia("Movie")
