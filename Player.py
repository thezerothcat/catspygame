import CellObject
import Stats
import Characters

class Player:
    def __init__(self, name = 'Hero'):
        self.characters = [ Characters.Character('Hero') ]
        self.characters[0].name = name
        self.money = 0
        self.progress = 0
        self.purchases = 0

    def send(self):
        out = []
        for character in self.characters:
            out.append(character.send())
        data = {'money':self.money, 'purchases':self.purchases, 'progress':self.progress, 'characters':out}

    def receive(self, data):
        guys = []
        for character_data in data['characters']:
            guy = Characters.Character('Hero')
            guys.append(guy.receive(character_data))
        self.money = data['money']
        self.progress = data['progress']
        self.purchases = data['purchases']




# will allow scene review later
#        self.scenes = []

#        self.human = human
# 'Apple', 'Apple', 'Apple', 'Apple', 'Bomb', 'Apple', 'Apple', 'Bomb', 'Apple', 'Bomb'

