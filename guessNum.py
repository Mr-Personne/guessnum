import random

print("guess number game start")

def guessNum():
    answer = random.randint(1, 20)
    #print('the answer is : ',answer)
    userAnswer = int(input("what's the number answer? ") or 0)
    tries = 5

    if userAnswer == answer:
        print('you win!')
        playagain = input('play again? y/n ')
        if playagain == "y":
            guessNum()
        
    else:
        """if userAnswer > answer:
            print('answer is lower')
        else:
            print('answer is higher')"""
        tries = tries - 1
        while tries >= 1:
            if userAnswer == answer:
                print('you win!')
                playagain = input('play again? y/n ')
                if playagain == "y":
                    guessNum()
                break
            else:
                if userAnswer > answer:
                    print('->> answer is lower')
                else:
                    print('->> answer is higher')
                print('nope', tries, ' tries left')
                tries = tries - 1
                userAnswer = int(input("what's the number answer? ") or 0)
        else:
            print('answer was : ', answer)
            print('You lose! good DAY, sir...')
            playagain = input('play again? y/n ')
            if playagain == "y":
                guessNum()
            

guessNum()
