high_score = 13  # global variable


""" THis gives UnboundLocalError: local variable 'high_score' referenced before assignment
def score():
    new_score = 465
    if new_score > high_score: # high score becomes a local name because it is re-assigned in line9
        print(f"New high score is{new_score}")
    high_score = new_score # if no high_score assignment existed, code would run 


score()
print(high_score)
"""


def score():
    global high_score
    new_score = 465
    if new_score > high_score:
        print(f"New high score is{new_score}")
    high_score = new_score


score()  # works as expected
print(high_score)  # 465


def function_where_global_name_can_be_accessed_without_using_globalKeyword_coz_assignment_of_that_name_does_not_exist():
    my_score = 20
    if my_score < high_score:  # high_score is 465(globally)
        print("I Lost")


function_where_global_name_can_be_accessed_without_using_globalKeyword_coz_assignment_of_that_name_does_not_exist()  # "I Lost"
## it worked because we are not re-assigning high_score name in local function body
