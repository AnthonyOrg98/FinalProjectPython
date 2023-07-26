import random

#define the cards
ace ="""   
       _____
      |     |
      |  A  |  
      |_____|  """
two = """   
       _____
      |     |
      |  2  |  
      |_____|  """
three = """   
       _____
      |     |
      |  3  |  
      |_____|  """
four = """   
       _____
      |     |
      |  4  |  
      |_____|  """
five = """   
       _____
      |     |
      |  5  |  
      |_____|  """
six = """   
       _____
      |     |
      |  6  |  
      |_____|  """
seven = """   
       _____
      |     |
      |  7  |  
      |_____|  """
eight = """   
       _____
      |     |
      |  8  |  
      |_____|  """
nine = """   
       _____
      |     |
      |  9  |  
      |_____|  """
ten = """   
       _____
      |     |
      | 10  |  
      |_____|  """
jack = """   
       _____
      |     |
      |  J  |  
      |_____|  """
queen = """   
       _____
      |     |
      |  Q  |  
      |_____|  """
king ="""   
       _____
      |     |
      |  K  |  
      |_____|  """

print("The following will execute a blackjack game(21).\n")
game= input("Would you like to play? ")

while game == "y" or game=="Y" or game== "yes":
    print("The following game is called blackjack or 21.\n To win you must draw cards that sum up to 21 or come closer to 21 than the computer.\n")
    print("Face cards are worth 10 and ace is worth 1 or 11 points depending on your hand.")

    Cards=[ace,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king]
    input("Type anything to deal the cards."  )
    player_score=0
    dealer_score=0
#np = Card npd = players score
#nd =computers/dealers card ndd = computer/dealers score
    for i in range (2):
        np=random.randint(0, 12)
        npd=np
        if npd>=10:
            npd=10
        elif npd==0 and player_score<21:
            npd=11
        elif npd == 0 and player_score>21:
            npd=1
        elif npd>=1:
            npd=npd+1
        player_score=npd+player_score
        print("Your hand: ")
        print(Cards[np])

        nd = random.randint(0, 12)
        ndd=nd
        if ndd>=10:
            ndd=10
        elif ndd == 0 and dealer_score<21:
            ndd = 11
        elif ndd == 0 and dealer_score>21:
            ndd=1
        elif ndd >=1:
            ndd = ndd + 1
        dealer_score=ndd+dealer_score
        print("Dealer hand: ")
        print(Cards[nd])

#First round of card dealing
    while(dealer_score<21 and player_score<21):
        if player_score <21 and dealer_score < 21:
            p=input("Would you like to hit(H) or check(C)?")
            if p == 'H' or p== 'h':
                np = random.randint(0, 12)
                npd = np
                if npd >= 10:
                    npd = 10
                elif npd == 0 and player_score<21:
                    npd = 11
                elif npd == 0 and player_score > 21:
                    npd = 1
                elif npd >= 1:
                    npd = npd + 1
                player_score = npd + player_score
                print("Your hand: ")
                print(Cards[np])
            if p == 'C' or p== 'c':
                nd = random.randint(0, 12)
                ndd = nd
                if ndd >= 10:
                    ndd = 10
                elif ndd == 0 and dealer_score<21:
                    ndd = 11
                elif ndd == 0 and dealer_score >21:
                    ndd = 11
                elif ndd >= 1:
                    ndd = ndd + 1
                dealer_score = ndd + dealer_score
                print("Dealer hand: ")
                print(Cards[nd])

        if player_score ==21 and dealer_score<21:
            print("You Win!!")
        if dealer_score ==21 and player_score<21:
            print("Computer Wins!!!")








    print("Your hand: ")
    print(player_score)

    print("dealer's hand: ")
    print(dealer_score)

    if dealer_score>player_score and dealer_score<=21:
        print("Dealer wins!!!")
    elif player_score>dealer_score and player_score<=21:
        print("You win!!!")
    elif player_score>21:
        print("you bust. Dealer wins")
    elif dealer_score>21:
        print("Dealer busts. You win")
    game = input("another round? ")
    print("Thanks for playing")
