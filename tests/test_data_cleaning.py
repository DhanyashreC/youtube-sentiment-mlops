from src.data_cleaning import clean_comment


def test_remove_extra_spaces():
    comment = "Hello     world"
    
    result = clean_comment(comment)
    
    assert result == "Hello world"


def test_remove_spaces_at_edges():
    comment = "   Hello world   "
    
    result = clean_comment(comment)
    
    assert result == "Hello world"


def test_multiple_whitespace():
    comment = "Hello\n\nworld\tPython"
    
    result = clean_comment(comment)
    
    assert result == "Hello world Python"