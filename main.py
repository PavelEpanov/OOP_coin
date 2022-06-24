import random

class Coin:
    def __init__(self):
        self.sideup = "Орёл"

    def toss(self):
        if random.randint(1, 2) == 1:
            self.sideup = "Орёл"
        else:
            self.sideup = "Решка"

    def get_name(self):
        return self.sideup


def main():
    my_coin = Coin()

    print("Эта сторона обращена вверх", my_coin.get_name())

    print("Подбрасываем моенту...")
    my_coin.toss()

    print("Эта сторона обращена вверх", my_coin.get_name())

main()

