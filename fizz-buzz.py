def buzz_quiz(number):

    if number%15==0:
        return "fizz buzz"
    elif number%3==0:
        return "fizz"
    elif number%5==0:
        return "buzz"
    else:
        return str(number)


next_number=0
while next_number<100:
    next_number+=1
    print(buzz_quiz(next_number))
    next_number+=1
    correct_answer=buzz_quiz(next_number)
    player_number=input("your number plz :")
    if player_number!=correct_answer:
        print("You lost this time Better luck next time")
        break
else:
    print("You played well")