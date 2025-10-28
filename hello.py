def say_hello():
    print("Hello, world!")


def calculate_discount(price, percent):
    """Обчислює знижку від ціни"""
    return price - (price * percent / 100)


if __name__ == "__main__":
    say_hello()
