from random import choice


class User:
    def __init__(self, name, age, email, nickname=None,  score=0):
        self.name = name
        self.age = age
        self.nickname = nickname
        self.score = score
        self.email = email
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_nickname(self):
        return self.nickname

    def get_score(self):
        return self.score

    def get_email(self):
        return self.email

    def generate_nickname(self):
        nicknames = [
            "ShadowX", "BlazeStorm", "NovaKing", "PhantomAce", "CyberWolf",
            "IronClaw", "DarkVortex", "NeonRider", "StormBreaker", "FrostByte",
            "GhostRider", "ThunderZ", "PixelNinja", "CrimsonEdge", "ZeroX",
            "InfernoKnight", "AquaPhantom", "SkyHunter", "VenomStrike", "EchoBlade",
            "LunarX", "SolarFlare", "NightHawk", "OmegaPulse", "SilentReaper",
            "HyperNova", "SteelTitan", "QuantumX", "FireFang", "IceDragon",
            "ShadowPulse", "WarpKnight", "TurboGhost", "DarkMatter", "AlphaStrike",
            "VoidHunter", "FlashCore", "MysticFury", "BlitzWolf", "CyberKnight"
        ]

        self.nickname = choice(nicknames)
        return self.nickname

    def add_score(self, points):
        self.score += points

    @staticmethod
    def input_name():
        return input("Please enter your name: ").strip().lower()

    @staticmethod
    def input_age():
        while True:
            try:
                return int(input("Please enter your age: "))
            except ValueError:
                print("Enter a valid number.")\

    @staticmethod
    def input_email():
        return input("Please enter your email: ").strip().lower()
