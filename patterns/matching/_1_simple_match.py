def calculate(a, b, operation) -> int | str:
    match operation:
        case "+":
            return a + b  # после совпадения case дальше проверки не идут (вне зависимости от наличия return)
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a // b
        case _:  # 'wildcard' - все остальные случаи
            return f"Не знаю такой операции {operation}"


if __name__ == '__main__':
    print(calculate(2, 2, "+"))
    print(calculate(2, 2, "-"))
    print(calculate(2, 2, "*"))
    print(calculate(2, 2, "/"))
    print(calculate(2, 2, "**"))
