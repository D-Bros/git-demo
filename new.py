words =  ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(words)

guesses = ''

turns = 10
while turns > 0:
    print(f"you have left {turns} turns ")
    
    guesses_all = True
    for c in word:
        if c in guesses:
            print(c,end=' ')
        else:
            print('_',end=' ')
            guesses_all = False
    print()
    
    if not guesses_all:
        guess = input("Guess char  ")
        guesses = guesses + guess
        if guess not in word:
            turns = turns - 1
    else:
        print("you win")
        turns =0
