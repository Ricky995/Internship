# -*- coding: utf-8 -*-
from random import randint
from sys import exit

class Moria(object):

    def open(self):
        print "You are a dwarf in the Mines of Moria. The mines are long overrun"
        print "by goblins and orcs. But you are not alone, there are a couple of elves and"
        print "men with you. You go deeper into the mines and as you go, you hear the gremlins"
        print "and the orcs. Suddenly, there are 10 to 20 of them in front of you."
        answer=raw_input("Answer: ")
        if "fight" in answer:
            print "That is a good choice because orcs and gremlins are no match"
            print "to the likes of you! You win the fight and you go along your way deeper"
            print "into the mines."
            return 'Cave'
        elif "flee" or "run" in answer:
            print "They have very advanced long-range weapons. They use them and they kill you all."
            return 'death'
        else:
            print "Not available in the choices, so you die!"
            return 'death'

class Cave(object):

    def open(self):
        print "As you walk through the mines, another group spots you and comes after you,"
        print "but this group is far larger in numbers, strength and types of soldiers. They have massive"
        print "cave trolls and orc captains. They chase you in a cave, not very big, where you find a tomb"
        print "of your cousin, which you didn't now is dead and a well..."

        bla=raw_input()
        if "fight" in bla:
            print"Once again you've made the right choice. You struggle a little bit to defeat"
            print "the trolls but you end up victorious once again. Your elf friend has no arrows left, your"
            print "group is tired and you are yet to meet the greatest foe that ever existed in this realm..."
            return 'Khazad-Dum'
        elif "jump" in bla:
            print "You died from the fall. The well is empty."
            return 'death'
        else:
            print "You are very bad at this..."
            return 'death'

class Khazad_Dum(object):

    def open(self):
        print "You continue your journey through the mines, you're trying to reach the"
        print "other side but the gremlins and the orcs are aware of your presence and every gremlin and orc still alive in"
        print "the mines comes at you.. and surrounds you. You have nowhere to go and there must be thousands of these"
        print "creatures eager to kill you and eat your flesh. But, a very loud thud frightens them and they all run away."
        print "All of you are happy but you, because you know that, that thud came from the very creature that's about to come"
        print "in front of you, and you are powerless to stop him. Behind you there's a bridge that leads to the outside world."

        answer=raw_input("Answer: ")
        if "fight" in answer:
            print "You are no match for the Balrog. He burns all of your flesh and devours you."
            return 'death'
        elif "run" or "bridge" in answer:
            print "Good choice, you run over the bridge and the Balrog cannot reach you."
            return 'complete'
        else:
            print "Not listed"
            return 'death'

class complete(object):

    def open(self):
        print "You won! Nice going."
        return 'complete'

class death(object):

    def open(self):
        print "You lost. Game over..."
        exit(0)

class scenes(object):
    rooms={
        'Moria':Moria(),
        'Cave' :Cave(),
        'Khazad-Dum':Khazad_Dum(),
        'death':death(),
        'complete':complete()
    }
    def __init__(self,start):
        self.start=start
    def next(self,name):
        room=scenes.rooms.get(name)
        return room

    def first(self):
        return self.next(self.start)

    def play(self):
        current_scene=self.first()
        last_scene=self.next('complete')

        while current_scene != last_scene:
            next_name=current_scene.open()
            current_scene=self.next(next_name)
        current_scene.open()

game=scenes('Moria')
game_start=scenes.play(game)
