import os

from game_object import GameObject, Modifier


beaker_debuff = Modifier(
    stat_affected="accuracy",
    value=20,
    duration=5,
    reason="The fluid within the beaker burns the opponent, preventing them from focusing on the battle"
)

beaker = GameObject(
    name='Beaker',
    object_description='A glass beaker with a small amount of unknown, corrosive and toxic fluid',
    attack_description='Splash the fluid onto your opponent',
    durability=1,
    accuracy=50,
    speed=4,
    strength=10,
    debuff=beaker_debuff,
    buff=None,
)

# ====================================================

beer_debuff = Modifier(
    stat_affected="accuracy",
    value=5,
    duration=8,
    reason="The opponent drinks some of the alcohol, worsening their coordination"
)

beer = GameObject(
    name='Beer',
    object_description='A jug with beer',
    attack_description='Splash the fluid onto your opponent',
    durability=1,
    accuracy=50,
    speed=4,
    strength=2,
    debuff=beer_debuff,
    buff=None,
)

# ====================================================

bone = GameObject(
    name="Bone",
    object_description="A large bone loved by dogs",
    attack_description="Used as a blunt force melee weapon",
    durability=3,
    accuracy=85,
    speed=3,
    strength=3,
    debuff=None,
    buff=None
)

# ====================================================

drill = GameObject(
    name="Drill",
    object_description="A standard handheld drill",
    attack_description="Used as a blunt force melee weapon",
    durability=5,
    accuracy=80,
    speed=3,
    strength=4,
    debuff=None,
    buff=None
)

# ====================================================

microphone_buff = Modifier(
    stat_affected="accuracy",
    value=8,
    duration=8,
    reason="The microphone continues to amplify every sound the opponent makes",
)

microphone = GameObject(
    name="Microphone",
    object_description="A powered-on microphone with batteries",
    attack_description="Throw the microphone at your opponent",
    durability=1,
    accuracy=70,
    speed=4,
    strength=1,
    debuff=None,
    buff=microphone_buff
)

# ====================================================

wallet_debuff = Modifier(
    stat_affected="speed",
    value=1,
    duration=3,
    reason="The opponent is briefly distracted by the idea of stealing your money"
)

wallet = GameObject(
    name="Wallet",
    object_description="A nice, leather wallet with some cash and cards",
    attack_description="Throw the wallet at your opponent",
    durability=1,
    accuracy=90,
    speed=5,
    strength=1,
    debuff=wallet_debuff,
    buff=None
)