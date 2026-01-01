#Polymorphism
class Instrument:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def play(self):
        print(F"Play the instrument.")

class Guitar(Instrument):
    def play(self):
        print(F"{self.name} the {self.model} guitar is strumming chords.")
class Piano(Instrument):
    def play(self):
        print(F"{self.name} the {self.model} piano is playing melodies.")
class Drum(Instrument):
    def play(self):
        print(F"{self.name} the {self.model} drum is beating rhythms.")
# Create objects of each subclass
guitar = Guitar("Fender", "Stratocaster")
piano = Piano("Yamaha", "U3")
drum = Drum("Pearl", "Export")
# Call the play method on each object
guitar.play()
piano.play()
drum.play()