import requests
from Poke_API import get_pokemon_data


class Pokemon:
  '''Represents a simple Pokemon object, instead of just a dictionary'''
  def __init__(self, name, id, hp, attack, sprite_url, type):
    self.name = name
    self.id = id,
    self.hp = hp
    self.attack = attack
    self.sprite_url = sprite_url
    self.type = type
  
  def info(self):
    print(f"=============== {self.name}'s Info ===============")
    print(f"ID: {self.id}")
    print(f"Stats: HP - {self.hp} Attack - {self.attack}")
    print(f"Type: {self.type}")
    print(f"Sprite: {self.sprite_url}")

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
    
    self.main_game_loop()
  
  def main_game_loop(self):
    '''Main game loop menu'''
    while True:
      print('''
============== Menu ================
1.) Search for a Pokemon
2.) View our team
3.) Remove Pokemon from team
4.) Quit game
''')
      choice = int(input("(1-4): "))
      if choice == 1:
        pass #Go look for pokemon to catch
      elif choice == 2:
        pass #View all the pokemon in the player's team
      elif choice == 3:
        pass # remove a pokemon from our team using its index
      elif choice == 4:
        print("Thanks for playing!")
        return #Quit out the game




charmander = get_pokemon_data("charmander")
print(charmander)
# {'name': 'charmander', 'id': 4, 'hp': 39, 'attack': 52, 'sprite_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png', 'type': 'fire'}

# object_charmander = Pokemon(name = charmander["name"], pokemon_id=charmander['id'], hp=charmander['hp'], attack=charmander['attack'], sprite_url=charmander['sprite_url'], pokemon_type=charmander['type'])

object_charmander = Pokemon(**charmander)

# object_charmander.info()

new_player = Player("Ash")
new_player.add_pokemon(object_charmander)
# print(new_player.remove_pokemon(2))
new_player.choose_starter()
new_player.show_collection()


