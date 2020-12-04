class Goblin:
    hp = 0
    dp = 0

    def __init__(self, hp, dp):
        self.hp = hp
        self.dp = dp

    def make_goblin(self, hp, dp):
        goblin = Goblin(hp, dp)
        return goblin

    def beaten(self, enemy_dp):
        self.dp -= enemy_dp

    def upgrade(self, hp, dp):
        self.hp += 2
        self.dp += 2


class Hero:
    name = ""
    hp = 0
    dp = 0

    def __init__(self, name, hp, dp):
        self.name = name
        self.hp = hp
        self.dp = dp

    def make_hero(self, name, hp, dp):
        hero = Hero(name, hp, dp)
        return hero

    def level_up(self, prompt="Please select which buff you want: "):
        print("Enter 1 or 2 to select your choice")
        print("1. Increase HP by 5")
        print("2. Increase DP by 5")
        choice = int(input(prompt))
        if choice == 1:
            self.hp += 5
        if choice == 2:
            self.dp += 5

    def beaten(self, enemy_dp):
        self.dp -= enemy_dp

