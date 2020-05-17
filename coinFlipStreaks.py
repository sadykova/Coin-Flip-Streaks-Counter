import random #for randint 
import sys #for sys.exit()
# general function
#streakN is how many heads or tails in a row I want to see comes up in an experiment
#flipN is the number of flips I want to do in a single experiment
#experimentN is how many experiments I want to conduct
def streakCounter(consec, flipN, experimentN):
    if consec==0:
        sys.exit("Invalid input. Please enter a number larger than 0.") #makes sure a user enters valid input.
    if flipN==0:
        sys.exit("Invalid input. Please enter a number larger than 0.")
    if experimentN==0:
        sys.exit("Invalid input. Please enter a number larger than 0.")
    if consec>flipN:
        sys.exit("Invalid input. Number of streaks cannot be larger than a number of flips in an experiment.")
    numberOfStreaks=0 #increments by one if a single experiment had a streak as defined by user
    for experiment in range(experimentN):
        streak=0 # at the start of an experiment the number of streaks is 0
        flip_list=[random.randint(0, 1) for i in range(flipN)] #creates a sample of flips
        for i in range(flipN):
            if i==0: #passes the first item in the list
                pass
            elif flip_list[i] == flip_list[i-1]:  #checks for individual streaks
                streak += 1
            else:
                streak=0
            if streak == consec-1: # if I want to see 6 heads in a row, it will be counted as 5 streaks. 
                numberOfStreaks += 1
                break # abandons a current experiment if a streak is found
    print(numberOfStreaks)
    print(f"Chance of streak:{(numberOfStreaks/experimentN)*100}%")
