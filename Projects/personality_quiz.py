# beginning

triangle_points = 0
square_points = 0

print("welcome to my personality quiz! please answer the questions below.")

# middle

answer = input("are you A) a cat person, or B) a dog person ")
if answer == "A":
    triangle_points += 1
elif answer == "B":
    square_points += 1

answer = input("do you like A) sweet and sour, or B) savory ")
if answer == "A":
    triangle_points += 1
elif answer == "B":
    square_points += 1

answer = input("would you rather A) live in the countryside, or B) live in the city ")
if answer == "A":
    square_points += 1
elif answer == "B":
    triangle_points +=1

answer = input("are you more A) creative, or B) practical ")
if answer == "A":
    triangle_points += 1
elif answer == "B":
    square_points += 1

answer = input("are you an A) introvert, or B) extrovert ")
if answer == "A":
    square_points += 1
elif answer == "B":
    triangle_points += 1

answer = input("when hanging out with friends, would you rather A) go out to a loud party, or B) stay home ")
if answer == "A":
    triangle_points += 1
elif answer == "B":
    square_points += 1

answer = input("during the holidays, would you rather A) bake cookies, or B) go out ice skating ")
if answer == "A":
    square_points += 1
elif answer == "B":
    triangle_points += 1

answer = input("do you like A) red, orange or yellow, or B) green, blue, or purple ")
if answer == "A":
    triangle_points += 1
elif answer == "B":
    square_points += 1

answer = input("imagine you're in disneyland. would you rather A) go on the biggest rollercoaster, or B) go on a calmer ride ")
if answer == "A":
    triangle_points += 1
if answer == "B":
    square_points += 1

# end

if square_points > triangle_points:
    print("you are a square!")
elif triangle_points > square_points:
    print("you are a triangle!")