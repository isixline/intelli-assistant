from intelli_assistant.checkers.text_space_checker import check_text_space

def test_check_text_space():
    # given
    text = 'hello世界'
    # when
    result = check_text_space(text)
    # then
    assert result == 'hello 世界'

def test_check_text_space_no_space():
    # given
    text = 'hello世界'
    # when
    result = check_text_space(text)
    # then
    assert result == 'hello 世界'

def test_check_text_space_with_multiple_space():
    # given
    text = 'hello  世界'
    # when
    result = check_text_space(text)
    # then
    assert result == 'hello 世界'

def test_check_text_space_english_space_english():
    # given
    text = 'hello  world'
    # when
    result = check_text_space(text)
    # then
    assert result == 'hello  world'