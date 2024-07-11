import random
choices=['rock','paper','scissors']
print("ROCK-PAPER-SCISSORS GAME")
print("Please note the rules of the game :")
print("(1) Scissor cuts paper and scisssor wins in such a combination.")
print("(2) Rock smashes scissor and rock wins in such a combination")
print("(3) Paper covers rock and paper wins in such a combination")
print("Your choices can be : ",choices)
while True:
    ch=input("Enter your choice : (Enter rock/paper/scissors) ")
    comp_ch=random.choice(choices)
    print("Computer chose : ",comp_ch, " and ","You chose : ",ch)
    if(comp_ch==ch):
        print("It's a tie")
    elif(comp_ch=='rock' and ch=='paper'):
        print("You win!! Computer looses!")
    elif(ch=='rock' and comp_ch=='paper'):
        print("You lose! Computer wins!!")
    elif(comp_ch=='rock' and ch=='scissors'):
        print("You lose! Computer wins!!")
    elif(ch=='rock' and comp_ch=='scissors'):
        print("You win!! Computer loses!")
    elif(comp_ch=='paper' and ch=='scissors'):
        print("You win!! Computer looses!")
    elif(comp_ch=='scissors' and ch=='paper'):
        print("You lose! Computer wins!!")
    else:
        print("Incorrect choice")
    yn=input("Do you want to play again ? (Enter yes/no) : " )
    if (yn=='no'):
        break
