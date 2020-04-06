import re

def is_parsable():
    user_input = input("type something:")
    for element in user_input:
        user_input_eval = re.match("[a-zA-Z0-9]", user_input)
        if user_input_eval:
            print("good")
            exit()
        else:
            print("no good")
            exit()

is_parsable()
