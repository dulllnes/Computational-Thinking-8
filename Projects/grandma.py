guesses = 0
while True:
    word = input("What do you think grandma likes?")
    if "t" in word:
        print(f"grandma does not like {word}!")
    else:
        print(f"grandma likes {word}!")

    print ("")
    
    guesses +=1  
    
    if guesses == 10:
        print(f"grandma does not like you right now")
   
    if guesses == 15:
        why = input("are you ready to guess? ")
        if why == ("yes"):
            guess = input("ok. is it A, grandma does not like T. or is it B, grandma does not like two syllable words.")
            if guess ==("A"):
                print(f"YAYYYAYAYY YOU WIN")
            elif guess ==("B"):  
                print(f"NOOO YOU LOSE HAHA LLLLLL")
