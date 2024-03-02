from intelli_assistant.executers.command_line_executer import split_keyword_and_args

def test_split_keyword_and_args():
    #given
    user_input = 'weather city=London'
    #when
    keyword, args = split_keyword_and_args(user_input)
    #then
    assert keyword == 'weather'
    assert args == ['city=London']

def test_split_keyword_and_args_no_args():
    #given
    user_input = 'exit'
    #when
    keyword, args = split_keyword_and_args(user_input)
    #then
    assert keyword == 'exit'
    assert args == []

def test_split_keyword_and_args_multiple_args():
    #given
    user_input = 'search engine=google query=python'
    #when
    keyword, args = split_keyword_and_args(user_input)
    #then
    assert keyword == 'search'
    assert args == ['engine=google', 'query=python']
