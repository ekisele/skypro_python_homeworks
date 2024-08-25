import pytest

from string_utils import StringUtils

utils = StringUtils()

import pytest
from string_utils import StringUtils

@pytest.mark.parametrize('input, result', [("katya","Katya")])
def test_capitilize_positive(input, result):
    string_utils = StringUtils ()
    res = string_utils.capitilize(input)
    assert res == result




def test_capitalize():
    """POSITIVE"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello") == "Hello"
    assert utils.capitilize("123") == "123"
    """NEGATIVE"""
    assert utils.capitilize("") == ""
    assert utils.capitilize(" ") == " "
    assert utils.capitilize("12345тест") == "12345тест"




def test_trim():
    """POSITIVE"""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello") ==  "hello"
    assert utils.trim("  SKY") == "SKY"
    """NEGATIVE"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"


@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim("  SKY  ") == "  SKY  "




@pytest.mark.parametrize('string, delimeter, result' ,[
    # POSITIVE
    ("яблоко,апельсин,мандарин", ",", ["яблоко", "апельсин", "мандарин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]), 
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result



@pytest.mark.parametrize('string, symbol, result', [

    ("мандарин", "м", True),
    ("гвоздь", "д", True),
    ("кот", "т", True),
    ("шкаф-купе", "-", True),
    ("145", "1", True),
    ("", "", True),
    ("Ростов", "в", False),
    ("привет", "з", False),
    ("ток", "№", False),
    ("", "з", False),
    ("12345", "h", False),  
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [
    ("цветок", "ц", "веток"), 
    ("Катя", "К", "атя"),
    ("Море", "М", "оре"),
    ("123", "1", "23"),
    ("Московская область", " ", "Московскаяобласть"),
    
    ("кофе", "и", "кофе"),
    ("", "", ""),
    ("", "с", ""),
    ("чай", "", "чай"),
    ("мята", " ", "мята"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result



@pytest.mark.parametrize('string, symbol, result',[
    ("тетрадь", "т", True),
    ("Ростов", "Р", True),
    ("", "", True),
    ("Анна-Мария", "А", True),
    ("123", "1", True),

    ("мир", "н", False),
    ("зонт", "р", False),
    ("собака", "о", False),
    ("", "?", False),
    ("дом", "п", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result',[
    ("Ольга", "а", True),
    ("клубника", "а", True),
    ("тапок", "к", True),
    ("кошка", "а", True),
    ("123", "3", True),

    ("слон", "м", False),
    ("зонт", "д", False),
    ("окно", "ю", False),
    ("", "?", False),
    ("дом", "п", False),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result',[
    ("", True),
    (" ", True),
    ("  ", True),

    ("не пусто", False),
    (" не пусто с пробелом", False),
    ("345", False),
])

def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize('lst, joiner, result',[
    (["c", "a", "t"], ",", "c,a,t"),
    ([1, 2, 3], None, "1, 2, 3"),
    (["к", "о", "т"], "", "кот"),

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", ""),
])

def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result