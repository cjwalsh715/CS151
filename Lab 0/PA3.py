# Programmers: Colin Walsh
# Course: CS151, Prof. Mehri
# Programming Assignment: 3
# Program Inputs: quidditch info, qbr info, score info
# Program Outputs: quidditch score, qbr, gymnist score


import sys

# quidditch function
def quidditch(goals, snitch):
    if snitch == True:
        points = goals * 10 + 30
        print("Score:", str(points), "points")
    elif snitch == False:
        points = goals * 10
        print("Score:", str(points), "points")

# QBR function
def QBR(completions,passing_yards,attempts,touchdowns,interceptions):
    qbr = ((5*((completions/attempts)-0.3)) + (0.25*((passing_yards/attempts)-3)) + 20*(touchdowns/attempts) + 2.375 - (25*(interceptions/attempts)))*100/6
    if qbr > 158.3:
        print("Perfect QBR")
    print("QBR:",str(qbr))

# gymnist function
def Gym(score, execution):
    maximum = max(execution)
    minimum = min(execution)
    rate = score + (sum(execution) - maximum - minimum) / 3
    print("Score:", str(rate), "points")

# Main Application
start = input("Enter: 1 for Quidditch Score; 2 for QBR; 3 for Gymnastics Score: ")
if start.isdigit() and int(start) <= 3 and int(start) >= 1:
    start = int(start)
else:
    print("Invalid input")
    sys.exit()

# Quidditch calling
def main():
    if start == 1:
        goal = input("Enter the number of goals: ")
        if goal.isdigit() and int(goal) >= 0:
            goal = int(goal)
        else:
            print("Invalid")
            sys.exit()
        snitch = input("Enter 1 if the snitch was caught or 0 if the snitch was not caught: ")
        if snitch.isdigit() and int(snitch) <= 1 and int(snitch) >= 0:
            snitch = int(snitch)
        else:
            print("Invalid input")
            sys.exit()
        quidditch(goal, snitch)

    # QBR calling
    elif start == 2:
        completion = input("Enter the completions: ")
        if completion.isdigit() and int(completion) >= 0:
            completion = int(completion)
        else:
            print("Invalid")
            sys.exit()
        pass_yards = input("Enter the passing yards: ")
        if pass_yards.isdigit() and int(pass_yards) >= 0:
            pass_yards = int(pass_yards)
        else:
            print("Invalid")
            sys.exit()
        attempt = input("Enter the attempts: ")
        if attempt.isdigit() and int(attempt) >= 0:
            attempt = int(attempt)
        else:
            print("Invalid")
            sys.exit()
        if(attempt == 0):
            print("Zero")
            sys.exit()
        touchdown = input("Enter the touchdown passes: ")
        if touchdown.isdigit() and int(touchdown) >= 0:
            touchdown = int(touchdown)
        else:
            print("Invalid")
            sys.exit()
        intercept = input("Enter the interceptions: ")
        if intercept.isdigit() and int(intercept) >= 0:
            intercept = int(intercept)
        else:
            print("Invalid")
            sys.exit()
        QBR(completion, pass_yards, attempt, touchdown, intercept)

    # Gym calling
    elif start == 3:
        score = input("Enter difficulty: ")
        if score.isdigit() and int(score) >= 0:
            score = int(score)
        else:
            print("Invalid")
            sys.exit()
        execute = []
        for i in range(5):
            temp = input("Enter execution " + str(i + 1) + ": ")
            if temp.isdigit() and int(temp) >= 0:
                execute.append(int(temp))
            else:
                print("Invalid")
                sys.exit()
        Gym(score, execute)
    else:
        print("Invalid input")

main()