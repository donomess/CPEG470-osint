from answers import *;

def main():
    print("Here is the first link, I feel as if the CLUE is hidden in plain sight, though... https://www.e52theatre.com/copy-of-sast-xiv-sast-furious\n")
    check_ans1()
    print("You made it to my University! Good job. \n I wonder what could be next? Do you happen to know the most famous UD alum?\n")
    check_ans2()
    print("I know! A president! Where did Biden give a campaign speech on October 6th during his run?")
    check_ans3()
    print("Good job! You're a pro at this. What's the coordinates of the building where Gettsyburg handle their finances?")


def check_ans1():
    ans1 = input("Put the link you found here: ")
    if ans1 == first_link:
        print("Good job! You found it. Advancing to step 2. \n")
        return
    else:
        print("Wrong! Try again.\n")
        check_ans1()

def check_ans2():
    ans2 = input("What is the link to their website? (Input it here)\n")
    if ans2 == second_link:
        print("Good job! You found it. Advancing to the third step. \n")
        return
    else:
        print("Wrong! Try again.\n")
        check_ans2()

def check_ans3():
    ans3 = input("Provide the city: ")
    if ans3 == third_answer:
        print("Great job! You found this historical town.\n")
        return
    else:
        print("Wrong! Try again.\n")
        check_ans3()

def check_ans4():
    ans4 = input("Provide the coords: (+/-##.##,+/-##.##)")
    if ans4 == password:
        print("Congrats! You've worked so hard. Here's your flag: " + flag + "}")
        return
    else:
        print("Wrong! Try again.\n")
        check_ans4()
main()
