from datetime import datetime 

now=datetime.now()

name = raw_input("What is your last name?")
movie = raw_input("What is your favorite movie?")
color = raw_input("What is your favorite color?")

print "Ah, so your last name is %s, your favorite movie is %s, " \
"and your favorite color is %s." % (name,movie, color)
        
print "I never really liked the color %s." % (color)

number = raw_input("Do you have a favorite number? If so, what is it?")
print "That is an interesting number. %s is an important number in many " \
"cultures." % (number)

food = raw_input("Do you have a favorite food, perchance?")

print "Ah, the age - old %s. Such a great dish. Great for the palate!" % (food)

time = raw_input("Say, do you have the time?")

print "%s is not exact. The correct time is %s:%s:%s." %(time,now.hour,now.minute,now.second)

def drink():
    print "Well, we've been talking for too long, I haven't even offered you " \
    "a drink."  
    print "Would like some water or some tea?"
    answer = raw_input("Type water or tea and hit 'Enter'.").lower()
    if answer == "water" or answer == "w":
        print "Simple enough! Here you go. Enjoy it!"
    elif answer == "tea" or answer == "t":
        print "I thought you might like to have a nice brew!"
    else:
        print "I don't have any of that! Seriously, choose something."
        drink()

drink()

def WordMasher():
    print "Hey, I meant to ask: do you speak any spanish? Si o no?"
    answer = raw_input().lower()
    if answer == "si" or answer == "yes":
        print "Muy Bien! Como estas mi amigo?"
        answer1 = raw_input().lower()
        if len(answer1) > 0:
            print "Y yo tambien! Cual es tu nombre?"
            name2 = raw_input()
            if len(name2) > 0 and name2.isalpha():
                name3 = name2.lower()
                newname = name3+"a"
                print newname + " is a beautiful spanish rendition of your name!"
            else:
                "That isn't a real name. Let's try this again."
                WordMasher()
        else:
            print "speak up, you baffoon!"
    elif answer == "no":
        print "Ah, what a shame. It is truly a beautiful language."
    else:
        print "stop horsing around and answer the question. Yes or no?"
        WordMasher()
        
WordMasher()
            
            
            
def pyglatin():           

    pyg = 'ay'
    print "pyg latin is another beautiful language. I can translate any word you " \
    "give me into pyg!"
    original = raw_input("Go ahead, try me. Give me a word.") 
    
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        print new_word +". what a funny word! what a funny language! Ahahaha."
    else:
        print 'empty'
            
pyglatin()
