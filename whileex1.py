tries = 0
answer = "Watson"
while (tries<=3):
    print("what is the name of the computer that played on Jeopardy?")
    response = raw_input()
    tries = tries+1
    if (response == "Watson"):
        print("That is right")
        break;
    elif(tries==3):a
     print("sorry, the answer is Watson.")
     break;
    else:
        print("sorry. try again")
