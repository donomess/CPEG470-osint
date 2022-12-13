from answers import *;

def main():
    print("Here is the first link, I feel as if the CLUE is hidden in plain sight, though... https://www.e52theatre.com/copy-of-sast-xiv-sast-furious\n")
    check_ans1()
    print("You made it to my University! Good job. \n I wonder what could be next? Do you happen to know the most famous UD alum?\n")
    check_ans2()


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
        print("Good job! You found it. Advancing to the last step. \n")
        return
    else:
        print("Wrong! Try again.\n")
        check_ans2()

main()
