from dice import Dice


class Creature(object):
    def __init__(self, data):
        self.allegiance = data.get('allegiance')

        self.max_hp = data.get('max_hp')
        self.current_hp = data.get('current_hp', self.max_hp)

        self.initiative_mod = data.get('initiative_mod', 0)

        self.ability_scores = data.ability_scores
        self.saving_throw_proficiencies = data.saving_throw_proficiencies

        self.attacks = data.attacks

        self.armor_class = data.armor_class

    def does_attack_hit(self, attack_outcome):
        if attack_outcome.type == 'aim':
            if attack_outcome.to_hit >= self.armor_class:
                return true
            return false

        elif attack_outcome.type == 'save':
            if self.save_roll(attack_outcome.save_ability) >= attack_outcome.save_threshold:
                return true
            return false
        raise Exception('Invalid Attack Outcome: '.format(attack_outcome.type))

    def save_roll(self, ability):
        return Dice.roll_expr('1d20+'.format(self.ability_scores.get(ability)))
