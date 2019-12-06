# https://codeforces.com/contest/1263/problem/B 

from random import randint

for i in range(int(input())):
    cards_list = []
    cards = {}
    swaps = 0
    for no_of_cards in range(int(input())):
        card = input()
        cards_list.append(card)
        if(card in cards):
            cards[card] += 1
            swaps += 1 
        else:
            cards[card] = 1
    print(str(swaps))

    if(swaps > 0): 
        for key in list(cards):
            reps = cards[key] - 1
            new_number = key
            while(reps > 0):
                while(True):
                    my_temp_key = list(key)
                    my_temp_key[randint(0,3)] = randint(0,9)
                    new_number  = (''.join(str(e) for e in my_temp_key))
                    if(new_number not in cards):
                        reps -= 1
                        cards[new_number] = 1 
                        loc = cards_list.index(key)
                        cards_list.remove(key)
                        cards_list.insert(loc, new_number)
                        break
    
    for x in cards_list:
        print(x)