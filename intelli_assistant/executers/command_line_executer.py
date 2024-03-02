from intelli_assistant.distributors.keyword_distributor import distribute_keyword
from intelli_assistant.utils.arg_unit import args_to_kwargs

def split_keyword_and_args(user_input):
    if ' ' not in user_input:
        keyword = user_input
        args = []
    else:
        keyword, args_string = user_input.split(maxsplit=1) 
        args = args_string.split()
    return keyword, args

def execute_from_command_line():
    print("Hello! I'm your intelligent assistant.")

    while True:
        keyword, args = split_keyword_and_args(input("What can I do for you? "))
        if keyword == 'exit':
            print("Goodbye!")
            break      
        if keyword not in distribute_keyword:
            print("Sorry, I don't know how to do that.")
            continue  
        search_result = distribute_keyword.get(keyword)(**args_to_kwargs(args))
        print(search_result)