# Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов, вернуть: Too weak
# - если пароль содержит только цифры, только строчные, только заглавные, вернуть: Weak
# - если пароль содержит символы любых 2 наборов, вернуть: Good
# - если пароль содержит символы любых 3 наборов, вернуть: Very Good
import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0  # счетчик силы пароля
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue  # перейти к следующему набору
    if count == 3:
        return "Very Good"
    else:
        return "Weak" if count == 1 else "Good"
    # Если возникла ошибка, то сначала дописываем assert, а затем меняем код


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
