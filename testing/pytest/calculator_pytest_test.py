# ВАЖНО! При написании каждого нового теста убедись, что он падает!
import pytest

from calculator import calculator


def test_plus():
    assert calculator("2+2") == 4  # при исполнении pytest подменит стандартный assert на свой


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator("abrakadabra")
    assert "Выражение должно содержать хотя бы один знак (+-/*)" == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator("2+2+3")
    assert "Выражение должно содержать 2 целых числа и 1 знак" == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
