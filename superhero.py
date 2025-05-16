class superhero:
    def __init__(self, name, power, country):
        self.name = name
        self.power = power
        self.country = country
    
    def freedom_fighter(self):
        print(f"{self.name} uses {self.power} to liberate {self.country}!")

# Creating a superhero instance.     
hero1 = superhero("Madmullah", "Spiritual and military power", "Somalia")
        
hero1.freedom_fighter()
