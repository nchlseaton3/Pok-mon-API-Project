import requests
import random 
from Poke_API import get_pokemon_data

#  Pokemon Class:

class Pokemon:
  '''Represents a simple Pokémon object, instead of just a dictionary'''
  def __init__(self, name, id, hp, attack, sprite_url, type):
    self.name = name
    self.id = id
    self.hp = hp
    self.attack = attack
    self.sprite_url = sprite_url
    self.type = type
  
  def info(self):
    """Display Pokémon Stats"""
    print(f"=============== {self.name}'s Info ===============")
    print(f"{self.name} (ID: {self.id})")
    print(f"Stats: HP: {self.hp}")
    print(f"Attack: {self.attack}")
    print(f"Type: {self.type}")
    print(f"Sprite: {self.sprite_url}")

# Player class:
class Player:
  
  def __init__(self, name):
    self.name = name
    self.team = [] #List of pokemon objects No more than 6 at a time
  
  def add_pokemon(self, pokemon):
    '''Takes in a Pokémon object and adds it to the team if there is room'''
    if len(self.team) < 6:
      self.team.append(pokemon)
      print(f"{pokemon.name} has been added to the team!")
      return
    else:
      print("The team is full, remove a Pokémon to make space.")
      return
    
  def remove_pokemon(self, index):
    """Remove a Pokémon from the collection by index"""
    if len(self.team) and index >= 0 and index < len(self.team):
      pokemon = self.team.pop(index)
      print(f"{pokemon.name} has been released!")
      return pokemon
    else:
      return None
    
  def show_collection(self):
    print(f"{self.name}'s Pokémon Collection:")
    i = 1
    for pokemon in self.team:
      print(f"{i}. {pokemon.name} (ID: {pokemon.id}) - {pokemon.type}")
      i += 1
  
  def choose_starter(self):
        """Let user pick their starter Pokémon"""
        print("\nChoose your starting Pokémon!")
        print("1. Bulbasaur (Grass type)")
        print("2. Charmander (Fire type)")
        print("3. Squirtle (Water type)")

        choice = input("Enter 1, 2, or 3: ").strip()
        starters = {"1": "Bulbasaur", "2": "Charmander", "3": "Squirtle"}

        if choice in starters:
            name = starters[choice]
            poke_dict = get_pokemon_data(name)
            if poke_dict:
                pokemon = Pokemon(**poke_dict)
                self.add_pokemon(pokemon)
                print(f"You chose {pokemon.name}! Great choice!")
            else:
                print("Could not fetch starter Pokémon data.")
        else:
            print("Invalid choice. Defaulting to Bulbasaur.")
            poke_dict = get_pokemon_data("bulbasaur")
            pokemon = Pokemon(**poke_dict)
            self.add_pokemon(pokemon)

#  Pokémon Game Class:

class PokemonGame:
    def __init__(self, player):
        self.player = player
        self.wild_pokemon = None
#  Go Hunting: 
    def go_hunting(self):
        """Find and encounter a wild Pokémon"""
        print("\nYou go hunting for Pokémon...")
        pokemon_id = random.randint(1, 151)
        data = get_pokemon_data(pokemon_id)

        if not data:
            print("No Pokémon found this time.")
            return

        # Create Pokémon object
        self.wild_pokemon = Pokemon(**data)

        print(f"\nA wild {self.wild_pokemon.name} appeared!")
        self.wild_pokemon.info()

        print("\n1. Try to catch")
        print("2. Flee")
        choice = input("What will you do? ").strip()

        if choice == "1":
            self.try_catch_pokemon()
        else:
            print(f"You fled from {self.wild_pokemon.name}.")
            self.wild_pokemon = None    
# Catch Pokemon 
    def try_catch_pokemon(self):
        """Attempt to catch the current wild Pokémon"""
        if not self.wild_pokemon:
            print("No wild Pokémon to catch!")
            return

        catch_rate = 0.25  # 25% chance
        chance = random.random()

        print(f"\nYou throw a Pokéball...")
        print(f"Catch rate: {catch_rate * 100:.0f}%")

        if chance <= catch_rate:
            print(f"Gotcha! {self.wild_pokemon.name} was caught!")
            self.player.add_pokemon(self.wild_pokemon)
            self.wild_pokemon = None
        else:
            print(f"Oh no! {self.wild_pokemon.name} broke free!")
    

# Remove Pokemon
    def remove_pokemon_menu(self):
        """Remove Pokémon from your team"""
        self.player.show_collection()
        try:
            choice = int(input("Enter the number of the Pokémon to release: ")) - 1
            removed = self.player.remove_pokemon(choice)
            if removed:
                print(f"{removed.name} was released from your team.")
        except ValueError:
            print("Please enter a valid number.")

#  Main Menu:
    def main_menu(self):
        """Loop for user input"""
        while True:
            print(f"\n=== Pokémon Adventure - {self.player.name} ===")
            print("1. Go hunting (Find wild Pokémon )")
            print("2. View your collection")
            print("3. Remove Pokémon")
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

#  Call to function 

if __name__ == "__main__":
    print("Welcome to Pokémon CLI Adventure!")
    trainer_name = input("What's your name, trainer? ").strip()
    player = Player(trainer_name)
    player.choose_starter()
    game = PokemonGame(player)
    game.main_menu()