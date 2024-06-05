import random

def getTokens(curTokens):
    global tokens
    global new
    print(f"The number of tokens is {tokens}\n")
    print("How many tokens would you like to take? ", end='')
    take = int(input())

    if take < 1 or take > (tokens // 2):
        print(f"Number must be between 1 and {tokens // 2}.\n")
        getTokens(curTokens)
        return

    tokens = curTokens - take
    new = tokens // 2
    print(f'You take {take} tokens.')
    print(f'{tokens} tokens remaining.\n')

def compTurn(curTokens):
    global tokens
    global new
    if tokens == 1:
        take = 1
    else:
        take = random.randint(1, min(new, tokens - 1))
    tokens = curTokens - take
    print(f'Computer takes {take} tokens.')
    print(f'{tokens} tokens remaining.\n')

tokens = random.randint(2, 30)
while tokens > 0:
    getTokens(tokens)
    if tokens == 0:
        print("Player wins!")
        break
    compTurn(tokens)
    if tokens == 0:
        print("Computer wins!")
