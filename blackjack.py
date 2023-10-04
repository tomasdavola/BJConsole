import random
cards=[('A', '♠'), (2, '♠'), (3, '♠'), (4, '♠'), (5, '♠'), (6, '♠'), (7, '♠'), (8, '♠'), (9, '♠'), (10, '♠'), ('J', '♠'), ('Q', '♠'), ('K', '♠'), ('A', '♥'), (2, '♥'), (3, '♥'), (4, '♥'), (5, '♥'), (6, '♥'), (7, '♥'), (8, '♥'), (9, '♥'), (10, '♥'), ('J', '♥'), ('Q', '♥'), ('K', '♥'), ('A', '♣'), (2, '♣'), (3, '♣'), (4, '♣'), (5, '♣'), (6, '♣'), (7, '♣'), (8, '♣'), (9, '♣'), (10, '♣'), ('J', '♣'), ('Q', '♣'), ('K', '♣'), ('A', '♦'), (2, '♦'), (3, '♦'), (4, '♦'), (5, '♦'), (6, '♦'), (7, '♦'), (8, '♦'), (9, '♦'), (10, '♦'), ('J', '♦'), ('Q', '♦'), ('K', '♦')]
cont=True
contsplit=True


hasntsplitted=True
def generatecard():
    index=random.randint(0,len(cards)-1)
    card=cards[index]
    cards.pop(index)
    return card

def generatedeck():
    deck = generatecard(),generatecard()
    return deck

def playerturn():
    global playerdeck
    global cont
    global hasntsplitted
    choice=input("What will you do")
    if choice=="h":
        playerdeck=list(playerdeck)
        playerdeck.append(generatecard())
        playerdeck=tuple(playerdeck)
        print(playerdeck)
    if choice=='st':
        cont=False
    if choice=="sp":
        if playerdeck[0][0]==playerdeck[1][0]and hasntsplitted==True:
            hasntsplitted=False
            print("Splitting")
            splitdeck1=[]
            splitdeck1.append(playerdeck[0])
            splitdeck2 = []
            splitdeck2.append(playerdeck[1])
            playerdeck=split(splitdeck1,splitdeck2)

        else:
            print("You can't split, your cards are not the same or it's too late")

def playerturnsplit(deck):
    global contsplit
    print(f"Your deck in play: {deck}")
    choice=input("What will you do")
    if choice=="h":
        deck=list(deck)

        deck.append(generatecard())

        deck=tuple(deck)
        print(deck)
        return deck
    if choice=='st':
        contsplit=False
        return deck
    if choice=='sp':
        return deck

def count(deck):
    calculator = []
    prevnumber=0
    nofaces=0
    possibilities=[]
    if 'A' not in str(deck):
        for card in deck:
            number=card[0]
            if card[0]== 'K' or card[0]== 'J' or card[0]== 'Q':
                number=10

            calculator.append(number)
        for number in calculator:
            prevnumber+=number
        return prevnumber
    else:
        for card in deck:
            number = card[0]
            if card[0] == 'K' or card[0] == 'J' or card[0] == 'Q':
                number = 10
                calculator.append(number)
            elif card[0]=="A":
                nofaces+=1
                number=1
                calculator.append(number)
            else:
                calculator.append(number)
        for number in calculator:
            prevnumber+=number
        while nofaces>0:
            if prevnumber+10*nofaces <= 21:
                possibilities.append(prevnumber+10*nofaces)
            nofaces-=1
        possibilities.sort()

        possibilities.insert(0,prevnumber)
        return possibilities

def check(deck):
    if isinstance(deck, list)==True:
        score=deck[len(deck)-1]
        return score

    if isinstance(deck, int)==True:
        if deck >21:
            score=0
        else:
            score=deck
        return score

def bankdeal(deck):
    bankcontinue=True
    while bankcontinue==True:
        if check(count(deck))<17and check(count(deck))>0:
            bankdeck.append(generatecard())
        elif check(count(deck))>16 and check(count(deck))<22:
            return check(count(deck))
        else:
            return 0


def split(deck1,deck2):
    global contsplit
    while contsplit==True:
        if count(deck1) > 21:
            break
        deck1=playerturnsplit(deck1)
        print(f"Your total(s) for deck 1 are: {count(deck1)}")
    contsplit=True
    while contsplit==True:
        if count(deck2) > 21:
            break
        deck2=playerturnsplit(deck2)
        print(f"Your total(s) for deck 2 are: {count(deck2)}")
    if check(count(deck1)) > check(count(deck2)):
        return deck1
    if check(count(deck1)) < check(count(deck2)):
        return deck2
    if check(count(deck1)) == check(count(deck2)) and check(count(deck1)) == 0:
        return deck1
    elif check(count(playerdeck)) == bankdeal(bankdeck):
        if len(deck1) < len(deck2):
            return(deck1)
        if len(deck1) > len(deck2):
            return (deck2)
        if len(deck1) == len(deck2):
            return(deck1)



bankdeck=generatedeck()
bankdeck = list(bankdeck)
playerdeck=generatedeck()
print(f"Your deck: {playerdeck}")
print(f"One of the dealers cards is a : {bankdeck[0]}")
print(f"Your total(s) are: {count(playerdeck)}")

while cont==True and hasntsplitted==True:
    if count(playerdeck)>21:
        break
    playerturn()
    print(f"Your total(s) are: {count(playerdeck)}")


if check(count(playerdeck)) > bankdeal(bankdeck):
    print("You won!")
if check(count(playerdeck)) < bankdeal(bankdeck):
    print("You lost!")
if check(count(playerdeck)) == bankdeal(bankdeck) and check(count(playerdeck))==0:
    print("House rules, You lose!")
elif check(count(playerdeck)) == bankdeal(bankdeck):
    if len(playerdeck) < len(bankdeck):
        print("You win (You have less cards)")
    if len(playerdeck) > len(bankdeck):
        print("You lost (You have more cards)")
    if len(playerdeck) == len(bankdeck):
        print("Draw!")

print(f"Your deck: {playerdeck}, Your score: {check(count(playerdeck))}, Your number of cards: {len(playerdeck)}")
print(f"House's deck: {bankdeck}, House's score: {check(count(bankdeck))}, House's number of cards: {len(bankdeck)}")