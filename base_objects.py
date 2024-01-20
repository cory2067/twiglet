import os

from game_object import GameObject, Modifier

beaker_debuff = {
    'stat_affected': "accuracy",
    'value': 20,
    'duration': 5,
    'reason': "The fluid within the beaker burns the opponent, preventing them from focusing on the battle"
}
beaker_debuff = Modifier(**beaker_debuff)

beaker_attributes = {
    'name': 'Beaker',
    'object_description': 'A glass beaker with a small amount of unknown, corrosive and toxic fluid'
    'attack_description': 'Splash the fluid onto your opponent'
    'durability': 1
    'accuracy': 50
    'speed': 4
    'strength': 10
    'debuff': beaker_debuff,
    'buff': None
}
beaker = GameObject(**beaker_attributes)

# ====================================================