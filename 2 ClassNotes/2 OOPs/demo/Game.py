import math


def isPrime(n):
    if n < 2:
        return False
    if n!=2 and n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    else:
        return True

n = int(input("Enter the number"))
while not isPrime(n):
    n = int(input("Enter the number"))
else:
    game_point = n**2+1
    current_point = 0
    player = 1
    while current_point < game_point:
        print(f"Player {player} is playing {current_point}")
        choice = int(input("Enter the choice")) #2
        while choice<1 or choice>n or current_point+choice > game_point:
            choice = int(input("Enter the choice"))
        current_point += choice

        player = player % 2 + 1

    else:
        print(f"Player {player} wins the game")


