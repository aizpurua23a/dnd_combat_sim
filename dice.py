import math
import random
import re


class Dice(object):

    @staticmethod
    def roll_expr(expression="1d20"):
        short_expr = expression.replace(' ', '')
        groups = re.match(r'^(\d+)d(\d+)(\+\d+)?$', short_expr).groups()
        (number_of_dice, type_of_dice, bonus) = groups

        if not bonus:
            bonus = 0

        if not number_of_dice or not type_of_dice:
            raise Exception('Invalid Dice Roll Expression provided: {}'.format(expression))

        return math.ceil(sum(
            [Dice.roll_one_die(type=int(type_of_dice)) for _ in range(int(number_of_dice))]) + int(bonus)
                         )

    @staticmethod
    def roll_one_die(type=20):
        return math.ceil(random.uniform(0, type))


if __name__ == "__main__":
    for _ in range(50):
        print(Dice.roll_expr('1d20+2'))
