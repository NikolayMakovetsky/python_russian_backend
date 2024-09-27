# Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов, вернуть: Too weak
# - если пароль содержит только цифры, только строчные, только заглавные, вернуть: Weak
# - если пароль содержит символы любых 2 наборов, вернуть: Good
# - если пароль содержит символы любых 3 наборов, вернуть: Very Good
import string


def password_strength(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(value) < 8:
        return 'Too weak'  # после написания каждого нового условия - запускаем тесты!
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return 'Weak'
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return 'Very Good'
    if (any(e in digits for e in value) and any(e in lowers for e in value)) or \
       (any(e in uppers for e in value) and any(e in lowers for e in value)) or \
       (any(e in digits for e in value) and any(e in uppers for e in value)):
        return 'Good'


if __name__ == '__main__':

    assert password_strength('') == 'Too weak'
    assert password_strength('1234567') == 'Too weak'
    assert password_strength('wermjhm') == 'Too weak'
    assert password_strength('JGNDMLG') == 'Too weak'
    assert password_strength('23FgjR5') == 'Too weak'

    assert password_strength('12345678') == 'Weak'
    assert password_strength('12345678876') == 'Weak'
    assert password_strength('asdfghjk') == 'Weak'
    assert password_strength('asdfghjkfggh') == 'Weak'
    assert password_strength('ASDFGHJK') == 'Weak'
    assert password_strength('ASDFGHJKRTYU') == 'Weak'

    assert password_strength('1234qwer') == 'Good'
    assert password_strength('1234ASDF') == 'Good'
    assert password_strength('ASDFqwer') == 'Good'
    assert password_strength('123434ASDDOF') == 'Good'

    assert password_strength('123qweASD') == 'Very Good'
    assert password_strength('123546453qwAS') == 'Very Good'
    assert password_strength('fsdfsdfdsdfA4') == 'Very Good'
    assert password_strength('GHJGHJHGHJO4s') == 'Very Good'
