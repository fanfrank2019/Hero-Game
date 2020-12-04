from Characters.npc import *
import time

from Characters.npc import *


def main():
    name = input("Please enter your hero's name: ")

    goblin_health = 10;
    goblin_hp = 10
    goblin_dp = 5

    hero_hp = 50
    hero_dp = 3

    hero = Hero(name, hero_hp, hero_dp)
    goblin = Goblin(goblin_hp, goblin_dp)

    counter = 0
    turn = 0
    print("=================")
    print("1.attack")
    print("2.training")
    print("=================")
    prompt = int(input("What is your next move?"))
    print("=================")
    while turn <= 100:
        turn += 1
        print("Turn: ", turn)
        print("Hero Index: HP:", hero.hp, "DP:", hero.dp)
        print("Goblin Index: HP:", goblin.hp, "DP:", goblin.dp)
        go_health = goblin.hp


        if prompt == 1:
            print("combating...")
            time.sleep(2)
            hero.hp -= goblin.dp
            print("Hero Health -", goblin_dp)
            goblin.hp -= hero.dp
            print("Goblin Health -", hero.dp)
            if hero.hp > 0 and goblin.hp <= 0:
                print("You won")
                print("Your HP:", hero.hp)
                counter += 1
                goblin = Goblin(goblin_hp, goblin_dp)
            elif hero.hp > 0 and goblin.hp > 0:
                print("Your HP:", hero.hp)
                print("Goblin's HP:", goblin.hp)
                print("=================")
            else:
                print("You lose")

        else:
            print("Training for 10 turns...")
            hero.hp += 10
            hero.dp += 5
            turn += 10

        if counter % 5 == 0 and counter >= 5:
            hero.level_up()

        if turn % 5 == 0:
            goblin_hp += 3
            goblin_dp += 1

        prompt = int(input("What is your next move?"))
        print("=================")

    else:
        if hero.hp > 0:
            print("You won the game")


class GameClient:
    if __name__ == '__main__':
        main()
