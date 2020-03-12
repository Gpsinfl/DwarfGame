class DwarfWizard:

    def __init__(self, name, magicPts, agilityPts, witPts):
        self.name = name
        self.MagicPts = magicPts
        self.AgilityPts = agilityPts
        self.WitPoints = witPts

    # Add Magic Points
    def addMagicPts(self, points):
        self.MagicPts = self.MagicPts + points

    # Add Agility Points
    def addAgilityPts(self, points):
        self.AgilityPts = self.AgilityPts + points

    # Add Wit Points
    def addWitPts(self, points):
        self.WitPoints = self.WitPoints + points

    # List out points
    def printPoints(self):
        print("Current Points")
        print("Magic [" + str(self.MagicPts) + "]")
        print("Agility [" + str(self.AgilityPts) + "]")
        print("Wit [" + str(self.WitPoints) + "]")


class DwarfWarrior:
    def __init__(self, name, StrengthPts, AgilityPts, SpeedPts):
        self.name = name
        self.StrengthPts = StrengthPts
        self.AgilityPts = AgilityPts
        self.SpeedPts = SpeedPts

    # Add Strength Points
    def addStrengthPts(self, points):
        self.StrengthPts = self.StrengthPts + points

    # Add Agility Points
    def addAgilityPts(self, points):
        self.AgilityPts = self.AgilityPts + points

    # Add Speed Points
    def addSpeedPts(self, points):
        self.SpeedPts = self.SpeedPts + points

    # List out points
    def printPoints(self):
        print("Current Points")
        print("Strength [" + str(self.StrengthPts) + "]")
        print("Agility [" + str(self.AgilityPts) + "]")
        print("Speed [" + str(self.SpeedPts) + "]")


def ClassSelection():
    userClass = input("Please select a class \n -Wizard- or -Warrior-")
    if userClass == "Warrior":
        WarriorTree()
    elif userClass == "Wizard":
        WizardTree()
    else:
        print("Please choose either Wizard or Warrior (Case sensitive)")


def WarriorTree():
    user = DwarfWarrior(input("Name Your Challenger"), 0, 0, 0)
    print(user.name)


def WizardTree():
    user = DwarfWizard(input("Name Your Challenger"), 0, 0, 0)
    print(user.name)


ClassSelection()
