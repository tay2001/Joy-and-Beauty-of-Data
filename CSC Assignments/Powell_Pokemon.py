##programmer: taylor powell
##assignment: pokemon

##-----------------------------

class Pokemon:
    """pokemon class for representing and editing pokemon"""

    ##the init
    def __init__(self, name, number, combat_points):
        """A constructor method that sets the name number and combat points"""
        self.name = name
        self.number = number
        self.combat_points = combat_points

    ## get name
    def get_name(self):
        """A reader method that returns the pokemon name"""
        return self.name

    ## get number
    def get_number(self):
        """A reader method that returns the number"""
        return self.number
    
    ##get combat points
    def get_combat_points(self):
        """A reader method that returns the combat points"""
        return self.combat_points

    
    ##set combat points
    def set_combat_points(self, combat_points):
        """A writer methods that sets the combat points"""
        self.combat_points = combat_points

    
# -------------------------------

def createPokemon():
    ##ask if they wanna pokemon
    ask = input(str("Would you like to add a pokemon?: y/n "))
        
    ##ask questions for input
    while ask == 'y':
        name = input(str("What is the pokemon?: "))
        number = input(str("What is the level number?: "))
        combat = input(str("What is the combat points amount?: "))

        # Create an instance of pokemon w the name number n combat points
        poke = Pokemon(name, number, combat)
        print("Pokemon:", poke.get_name(), poke.get_number(), poke.get_combat_points())

        ##would you like to change the combat points?
        ask1 = input(str("Would you like to change the current pokemons combat points?: y/n "))

        while ask1 == 'y':
            combat = input(str("What value would you like to change the combat points of the current pokemon?: "))
            poke.set_combat_points(combat)
            print("Pokemon:", poke.get_name(), poke.get_number(), poke.get_combat_points())
            ask1 = input(str("Would you like to change it again?: y/n "))

        ask= input(str("Would you like to add another?: y/n "))


    ##finish
    print('Goodbye! :>')

def main():
    createPokemon()

main()

