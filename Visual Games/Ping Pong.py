import copy
import random

class Pokemon(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def ataque(self, oponent):
        oponent.hp = oponent.hp - 150 #just for a test

class Trainer(object):
    def __init__(self, name, *pokemon):
        self.name = name
        self.pokemon, self.pokemonname = [], []
        for pkmn in pokemon:
            self.pokemon.append(copy.deepcopy(pkmn))
            self.pokemonname.append(pkmn.name)

weavile = Pokemon ('Weavile', 150) #change the hp to more than 150 if you want to win
garchomp = Pokemon ('Garchomp', 250)
roserade = Pokemon ('Roserade', 160)
ambipom = Pokemon ('Ambipom', 160) 

me = Trainer('You', weavile) #or choose ambipom to win
cynthia = Trainer('Cynthia', garchomp)

def alive(pokemon): #check if the pokemon is alive
    if pokemon.hp>0:
        return True
    if pokemon.hp<=0:
        pokemon.hp=0
        return False

def battle(trainer1, trainer2): #battle between two trainers
    fight1, fight2 = True, True
    while fight1 and fight2:
        print ('Choose a pokemon:', trainer1.pokemonname)
        pokemon1 = eval(input())
        while not alive(pokemon1):
            print (pokemon1.name, 'is out of batlle. Choose another pokemon')
            pokemon1 = eval(input())
        pokemon2 = random.choice(trainer2.pokemon)
        while not alive(pokemon2):
            pokemon2 = random.choice(trainer2.pokemon)
        print (trainer1.name, 'chose', pokemon1.name, '\n', trainer2.name, 'chose', pokemon2.name)
        while alive(pokemon1) and alive(pokemon2):
            pokemon1.ataque(pokemon2)
            if alive(pokemon2):
                pokemon2.ataque(pokemon1)
            print (pokemon1.name, pokemon1.hp)
            print (pokemon2.name, pokemon2.hp)
        print (trainer1.pokemon[0].name, trainer1.pokemon[0].hp) #here its returning the original hp
        print (trainer2.pokemon[0].name, trainer2.pokemon[0].hp) #here its returning the current hp, as it should
        if not any(alive(pokemon) for pokemon in trainer1.pokemon):
            fight1 = False
        if not any(alive(pokemon) for pokemon in trainer2.pokemon):
            fight2 = False

battle(me, cynthia)