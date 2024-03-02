from intelli_assistant.utils.arg_unit import args_to_kwargs

def test_args_to_kwargs():
    # given
    args = ['city=Seoul']
    # when
    result = args_to_kwargs(args)
    # then
    assert result == {'city': 'Seoul'}

def test_args_to_kwargs_multiple_args():
    # given
    args = ['city=Seoul', 'country=KR']
    # when
    result = args_to_kwargs(args)
    # then
    assert result == {'city': 'Seoul', 'country': 'KR'}

def test_args_to_kwargs_no_args():
    # given
    args = []
    # when
    result = args_to_kwargs(args)
    # then
    assert result == {}
