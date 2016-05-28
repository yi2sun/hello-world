from sys import exit

def start():
    print """
    You are in a dark room.
    There is a door to your left and right.
    Which one do you take?
    """
    
    next = raw_input("'left' or 'right'? >>>")
    
    if next == "left":
        print "You enter the bear room."
        bear_room()
    elif next == "right":
        print "You enter the monster room."
        monster_room()
    else:
        dead("You stumble around the room until you starve.")
    
def monster_room():
    print """
    Here you see the great evil monster.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or just stay there?
    """
    
    round = 0
    
    while True:
        next = raw_input("'flee' or 'stay'? >>>")
        
        if next == "flee":
            print "You leave the monster room."
            start()
        elif next == "stay":
            dead("Monster: Well, that's tasty!")
        else:
            round += 1
            print "You must select the given option."
       
        if round == 3:
            dead("You miss the choice. The monster eats you.")

def bear_room():
    print """
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    """
    
    bear_moved = False
    round = 0
    
    while True:
        next = raw_input("'take honey' or 'taunt bear' or 'open door'? >>>")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you leg off.")
        elif next == "open door" and not bear_moved:
            round += 1
            print "You can't open the door because the bear is still there!"
        elif next == "open door" and bear_moved:
            print "You enter the gold room."
            gold_room()
        else:
            round += 1
            print "I got no idea what the means."
            
        if round == 3:
            dead("The bear wakes up and eats you.")

def gold_room():
    print "This room is full of gold. How much do you take?"
    next = raw_input("Type a number between 1 to 100. >>>")
    if str.isdigit(next):
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 1:
        dead("You fool asshole!")
    elif how_much > 100:
        dead("You greedy bastard!")
    else:
        print "Nice, you're not greedy, you win and get %d money!" % how_much
        exit(0)
    
def dead(why):
    print why, "You dead!"
    exit(0)
    
start()

