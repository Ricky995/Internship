from random import randint
from sys import exit

class Moria(object):

    def open(self):
        print """You are a dwarf in the Mines of Moria. The mines are long overrun
        by goblins and orcs. But you are not alone, there are a couple of elves and
        men with you. You go deeper into the mines and as you go, you hear the gremlins
        and the orcs. Suddenly, there are 10 to 20 of them in front of you."""
        guess=raw_input("Answer: ")
        if "fight" in answer:
            print """That is a good choice because orcs and gremlins are no match
            to the likes of you! You win the fight and you go along your way deeper
            into the mines."""
            return 'Cave'
        elif "flee" or "run" in answer:
            print "They have very advanced long-range weapons. They use them and they kill you all."
            return 'death'
        else:
            print "Not available in the choices, so you die!"
            return 'death'

class Cave(object):

    def open(self):
        print """As you walk through the mines, another group spots you and comes after you,
        but this group is far larger in numbers, strength and types of soldiers. They have massive
        cave trolls and orc captains. They chase you in a cave, not very big, where you find a tomb
        of your cousin, which you didn't now is dead and a well..."""
        аnswer=raw_input("Answer: ")
        if "stay" or "fight" in answer:
            print"""Once again you've made the right choice. You struggle a little bit to defeat
            the trolls but you end up victorious once again. Your elf friend has no arrows left, your
            group is tired and you are yet to meet the greatest foe that ever existed in this realm..."""
            return 'Khazad-Dum'
        elif "jump" in answer:
            print "You died from the fall. The well is empty."
            return 'death'
        else:
            print "You are very bad at this..."
            return 'death'

class Khazad-Dum(object):

    def open(self):
        print """You continue your journey through the mines, you're trying to reach the
        other side but the gremlins and the orcs are aware of your presence and every gremlin and orc still alive in
        the mines comes at you.. and surrounds you. You have nowhere to go and there must be thousands of these
        creatures eager to kill you and eat your flesh. But, a very loud thud frightens them and they all run away.
        All of you are happy but you, because you know that, that thud came from the very creature that's about to come
        in front of you, and you are powerless to stop him. Behind you there's a bridge that leads to the outside world."""

        answer=raw_input("Answer: ")
        if "fight" in answer:
            print "You are no match for the Balrog. He burns all of your flesh and devours you."
            return 'death'
        if "bridge" in answer:
            print "Good choice, you run over the bridge and the Balrog cannot reach you."
            return 'complete'
