import random


def run_game():
    list = []

    for k in range(1,5):
        list.append(str(random.randint(1,8)))
    list = ''.join(list)
    
    
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
        
    attempts = 12   
    while attempts > 0:
        user_input = input("Input 4 digit code: ")
        if not user_input.isdigit() or len(user_input) != 4 or "9" in user_input:     
            print("Please enter exactly 4 digits.")
            continue   
        correct_position = 0
        incorrect_position = 0
        for i in range(4):
            if list[i] == user_input[i]:
                correct_position += 1
        print("Number of correct digits in correct place:    ", correct_position)
                
        for i in range(4):
            if list[i] != user_input[i] and list[i] in user_input:
                incorrect_position += 1
        print("Number of correct digits not in correct place:", incorrect_position)
        if list == user_input:
            print("Congratulations! You are a codebreaker!")
            print("The code was:", list)
            break
        if list != user_input:
            attempts -= 1
            print("Turns left:", attempts)
            if attempts == 0:
                print("The code was:", list)   
    


if __name__ == "__main__":
    run_game()
