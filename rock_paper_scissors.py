#rock_paper_scissors

import random

def game(comp,you):
    if comp == you:
        return None
    if comp =='s':
        if you == 'r':
            return False
        elif you == 'p':
            return True
    elif comp =='r':
        if you == 'p':
            return False
        elif you == 's':
            return True
    elif comp =='p':
        if you == 's':
            return False
        elif you == 'r':
            return True

print("comp turn: scissors(s) rock(r) or paper(p)?")
randNo = random.randint(1, 3)

if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'r'
elif randNo==3:
    comp = 'p'

you = input("your's turn: scissors(s) rock(r) or paper(p)?\n")
a = game(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("its a tie")
elif a:
    print("you win!!")
else:
    print("you loose!!")