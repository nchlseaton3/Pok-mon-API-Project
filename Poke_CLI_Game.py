import requests
import random 
from Poke_API import get_pokemon_data

#  Pokemon Class:

class Pokemon:
  '''Represents a simple Pokemon object, instead of just a dictionary'''
  def __init__(self, name, id, hp, attack, sprite_url, type):
    self.name = name
    self.id = id
    self.hp = hp
    self.attack = attack
    self.sprite_url = sprite_url
    self.type = type
  
  def info(self):
    """Display Pokemon Stats"""
    print(f"=============== {self.name}'s Info ===============")
    print(f"ID: {self.id}")
    print(f"Stats: HP - {self.hp} Attack - {self.attack}")
    print(f"Type: {self.type}")
    print(f"Sprite: {self.sprite_url}")

# Player class:
class Player:
  
  def __init__(self, name):
    self.name = name
    self.team = [] #List of pokemon objects No more than 6 at a time
  
  def add_pokemon(self, pokemon):
    '''Takes in a pokemon object and adds it to the team if there is room'''
    if len(self.team) < 6:
      self.team.append(pokemon)
      print(f"{pokemon.name} has been added ot the team!")
      return
    else:
      print("The team is full, remove a pokemon to make space.")
      return
    
  def remove_pokemon(self, index):
    """Remove a Pokemon from the collection by index"""
    if len(self.team) and index >= 0 and index < len(self.team):
      pokemon = self.team.pop(index)
      print(f"{pokemon.name} has been released!")
      return pokemon
    else:
      return None
    
  def show_collection(self):
    print(f"{self.name}'s Pokemon Collection:")
    i = 1
    for pokemon in self.team:
      print(f"{i}. {pokemon.name} (ID: {pokemon.id}) - {pokemon.type}")
      i += 1
  
  def choose_starter(self):
    print("Choose your starting Pokemon!")
    print("1. Bulbasaur")
    print("2. Charmander")
    print("3. Squirtle")

    name = input("Enter your pokemon's name: ")
    poke_dict = get_pokemon_data(name)
    if poke_dict:
      pokemon = Pokemon(**poke_dict)
      self.add_pokemon(pokemon)
    else:
      print("Invalid Pokename, please try again")

#  Pokemon Game Class:

class PokemonGame:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.wild_pokemon = None
#  Go Hunting: 
    def go_hunting(self):
        """Find and encounter a wild Pokémon"""
        pass
# Catch Pokemon 
    def try_catch_pokemon(self):
        """Attempt to catch the current wild Pokémon"""
        pass
# Remove Pokemon
    def remove_pokemon_menu(self):
        """Remove Pokémon from your team"""
        pass

#  Main Menu:
    def main_menu(self):
        """Loop for user input"""
        while True:
            print(f"\n=== Pokemon Adventure - {self.player.name} ===")
            print("1. Go hunting")
            print("2. View your collection")
            print("3. Remove Pokemon")
            print("4. Quit game")

            choice = input("\nWhat would you like to do? ")

            if choice == "1":
                self.go_hunting()
            elif choice == "2":
                self.player.show_collection()
            elif choice == "3":
                self.remove_pokemon_menu()
            elif choice == "4":
                print("Goodbye, trainer!")
                break
            else:
                print("Invalid option. Try again!")

