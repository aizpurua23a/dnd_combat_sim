from dice import Dice
from stats import ABILITIES


class Attack(object):
    def __init__(self, data):
        self.type = data.get('type')
        self.to_hit_bonus = data.get('to_hit_bonus')
        self.save_ability = data.get('save_ability')
        self.save_threshold = data.get('save_threshold')
        self.damage = data.get('damage')

    def validate(self):
        if self.type != "aim" and self.type != "save":
            raise Exception('Invalid Attack Type: '.format(self.type))
        if (self.type == "aim" and not self.to_hit_bonus) or \
                (self.type=='save' and not (self.save_ability and self.save_threshold)):
            raise Exception('Invalid Attack Format: '.format(self.data))
        if self.type == "save" and self.save_ability not in ABILITIES:
            raise Exception('Invalid Save Throw Ability: '.format(self.save_ability))
        if not self.damage:
            raise Exception('Invalid Damage Pattern: '.format(self.damage))

    def attack(self):
        if self.type == 'aim':
            return {
                type: self.type,
                to_hit: Dice.roll_expr(expression='1d20+{}'.format(self.to_hit_bonus))
                damage: Dice.roll_expr(self.damage)
            }

        if self.type == 'save':
            return {
                type: self.type,
                save_ability: self.save_ability,
                save_threshold: self.save_threshold,
                damage: Dice.roll_expr(self.damage)
            }
