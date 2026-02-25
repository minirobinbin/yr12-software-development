print("SUPABRIKS FESTIVAL COMPETITION POINTS HELPER") # introduction header for the program

def number_of_bricks(): # function to collect and validate the number of briks used
    no_of_briks = str(input("Enter the number of briks used. > ")) 
    if "." in no_of_briks: 
        print("Please enter whole number")
        no_of_briks = number_of_bricks()
        return no_of_briks
    else:
        try:
            no_of_briks = int(no_of_briks) 
            return no_of_briks
        except:
            print("Not a number") 
            no_of_briks = number_of_bricks()
            return no_of_briks


def scores(judge): # function to collect and validate the judges scores
    try:
        score = float(input(f"Enter Judge #{judge}'s score. > ")) 
    except:
        print("Not a number")
        score = scores(judge)
    if 0<=score<=10:
        return score
    else:
        print("Score not between 0 and 10.")
        score = scores(judge) 
        return score
    
def time_input(): # function to collect and validate the time input
    try:
        time = math.ceil(float(input("Enter the time taken (in minutes). > ")))
        return time
    except:
        print("Not a correct time, try again.")
        time = time_input()
        return time

def another_team(): # function to determine next program action
    try:
        finished = str(input("Do another team? (y = yes, n = no) > "))
    except:
        print()
    
    if finished == "y":
        program()
    elif finished == "n":
        return True
    else:
        print("Please enter y or n.")
        finished = another_team()
        return finished

import math
def program(): # the main program function
    no_of_briks = number_of_bricks()
    time = time_input()
    score_one = scores("1") # next time can use array and add them together with sum(scores) TODO
    score_two = scores("2")
    score_three = scores("3")

    # generating penalty rates
    if time >240: 
        penalty = 1.3
    elif time > 180:
        penalty = 1.1
    else:
        penalty = 1

    score_sum = score_one + score_two + score_three # add up judge score total
    points = score_sum * no_of_briks / penalty # calculate final points

    print(f"Final points: {int(points)}") # print final results
    finished = another_team() # ask if user wants to complete another team score
    if finished:
        return
    
program() # start the program


# functions used to easily test each section of code
# snake case used to follow suggested variable names

#---------------------+-----------------+-----------------+------------+-------+
#action               | expected result |  actual result  | pass/fail  | remedy|
# # of briks: 240     |no_of_briks= 240 |no_of_briks= 240 |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# # of briks: 202.3   | fail: ask again | fail: ask again |   pass     |       |
#---------------------+-----------------+-----------------+------------+-------+
# # of briks: j       |  fail: ask again| fail: ask again |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# # of briks: n       |no_of_briks= 3   |no_of_briks = 3  |    pass    |       |
# # of briks: 3       |                 |                 |            |       |
#---------------------+-----------------+-----------------+------------+-------+
# enter judge: 7      |  score_one =  7 |  score_one = 7  |    pass    |       |
# --------------------+-----------------+-----------------+------------+-------+ 
# enter judge: 7.5    |  score_one= 7.5 |  score_one= 7.5 |    pass    |       |
# --------------------+-----------------+-----------------+------------+-------+  
# enter judge: 11     | fail: ask again | fail: ask again |    pass    |       |
# --------------------+-----------------+-----------------+------------+-------+
# enter judge: -6     | fail ask again  | fail: ask again |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# enter judge: P      | fail: ask again | fail: ask again |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# enter time: 201.5   | time = 202      | time= 202       |    pass    |       |
# --------------------+-----------------+-----------------+------------+-------+
# enter time: hello   | fail: ask again | fail: ask again |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# enter time: 202     | time = 202      |  time = 202     |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# another team: y     |run program again|run program again|    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# another team: n     |   end program   |  end program    |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+
# another team: j     | fail: ask again | fail: ask again |    pass    |       |
#---------------------+-----------------+-----------------+------------+-------+


#+---------------------------+--------------------------+----------------------+
#|        input              |        process           |        output        |
#+---------------------------+--------------------------+----------------------+
#|        no_of_briks        |       1. judge score     |      final score     |
#|        time               |       2. penalty         |                      |
#|     three judge score     |       3. final score     |                      |
#+---------------------------+--------------------------+----------------------+