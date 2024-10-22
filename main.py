import tbc

def main():
    hero = tbc.Character()
    monster = tbc.Character("The Orc", 30, 35, 7, 2)
    hero.fight(hero, monster)
    
if __name__ == "__main__":
    main()