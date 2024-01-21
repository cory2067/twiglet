from game_object import GameObject, Modifier

OBJECTS = []

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
    strength=3,
    debuff=beaker_debuff,
    buff=None,
    sprites=["beaker.png"],
)

OBJECTS.append(beaker)

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
    sprites=["beer.png"],
)

OBJECTS.append(beer)

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
    buff=None,
    sprites=["bone.png"],
)

OBJECTS.append(bone)

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
    buff=None,
    sprites=["drill.png"],
)

OBJECTS.append(drill)

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
    buff=microphone_buff,
    sprites=["microphone.png"],
)

OBJECTS.append(microphone)

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
    buff=None,
    sprites=["wallet.png"],
)

OBJECTS.append(wallet)

# ====================================================

pickaxe = GameObject(
    name="Pickaxe",
    object_description="A heavy iron pickaxe",
    attack_description="Swing the pickaxe at your opponent",
    durability=3,
    accuracy=85,
    speed=2,
    strength=9,
    debuff=None,
    buff=None,
    sprites=["pickaxe.png"],
)

OBJECTS.append(pickaxe)

# ====================================================

toothbrush_debuff = Modifier(
    stat_affected="accuracy",
    value=5,
    duration=2,
    reason="The opponent is mildly distracted from worrying about their dental hygiene",
)

toothbrush = GameObject(
    name="Toothbrush",
    object_description="A cheap disposable toothbrush",
    attack_description="Start violently brushing your opponent's teeth",
    durability=2,
    accuracy=70,
    speed=3,
    strength=1,
    debuff=toothbrush_debuff,
    buff=None,
    sprites=["toothbrush.png"],
)

OBJECTS.append(toothbrush)

# ====================================================

wire_clippers_debuff = Modifier(
    stat_affected="strength",
    value=0.2,
    duration=5,
    reason="The opponent's weapon breaks, making it much weaker",
)

wire_clippers = GameObject(
    name="Wire Clippers",
    object_description="A pair of wire clippers",
    attack_description="Attempt to snip your opponent's weapon in half",
    durability=1,
    accuracy=50,
    speed=2,
    strength=0,
    debuff=None,
    buff=None,
    sprites=["wireclippers.png"],
)

OBJECTS.append(wire_clippers)

# ====================================================

coffee_pot_buff = Modifier(
    stat_affected="speed",
    value=1,
    duration=3,
    reason="Take a quick sip of coffee before attacking",
)

coffee_pot = GameObject(
    name="Coffee Pot",
    object_description="A coffee pot filled with hot coffee",
    attack_description="Spill scalding hot coffee on your opponent",
    durability=1,
    accuracy=90,
    speed=2,
    strength=6,
    debuff=None,
    buff=coffee_pot_buff,
    sprites=["coffeepot.png"],
)

OBJECTS.append(coffee_pot)

# ====================================================

computer = GameObject(
    name="Computer tower",
    object_description="A bulky computer tower from the 90s",
    attack_description="Lob the computer at your opponent",
    durability=1,
    accuracy=60,
    speed=1,
    strength=4,
    debuff=None,
    buff=None,
    sprites=["computer.png"],
)

OBJECTS.append(computer)

# ====================================================

fork = GameObject(
    name="Fork",
    object_description="A standard metal fork from the kitchen",
    attack_description="Stab the opponent with the fork",
    durability=5,
    accuracy=80,
    speed=5,
    strength=5,
    debuff=None,
    buff=None,
    sprites=["fork.png"],
)

OBJECTS.append(fork)

# ====================================================

headphones_debuff = Modifier(
    stat_affected="accuracy",
    value=5,
    duration=4,
    reason="The opponent is mildly distracted by the music blasting from your headphones",
)

headphones_buff = Modifier(
    stat_affected="speed",
    value=1,
    duration=4,
    reason="You are pumped by listening to your favorite music"
)

headphones = GameObject(
    name="Headphones",
    object_description="A set of open back, wired headphones",
    attack_description="Use the wire and headphones like a ball and chain to attack the opponent",
    durability=3,
    accuracy=50,
    speed=3,
    strength=1,
    debuff=headphones_debuff,
    buff=headphones_buff,
    sprites=["headphones.png"],
)

OBJECTS.append(headphones)

# ====================================================

pen_debuff = Modifier(
    stat_affected="accuracy",
    value=100,
    duration=4,
    reason="The opponent is persuaded by your brilliant essay and stops fighting",
)

pen = GameObject(
    name="Pen",
    object_description="The pen is mightier than the sword...?",
    attack_description="Write the opponent an essay about the futility of violence",
    durability=1,
    accuracy=5,
    speed=1,
    strength=0,
    debuff=pen_debuff,
    buff=None,
    sprites=["pen.png"],
)

OBJECTS.append(pen)

# ====================================================

teacup_buff = Modifier(
    stat_affected="speed",
    value=1,
    duration=3,
    reason="Take a quick sip of tea before attacking",
)

teacup = GameObject(
    name="Teacup",
    object_description="A delicate china teacup filled with tea",
    attack_description="Splash hot tea on your opponent",
    durability=1,
    accuracy=70,
    speed=4,
    strength=3,
    debuff=None,
    buff=teacup_buff,
    sprites=["teacup.png"],
)

OBJECTS.append(teacup)

# ====================================================

videocamera_debuff = Modifier(
    stat_affected="accuracy",
    value=50,
    duration=2,
    reason="The opponent hesitates briefly, because they do not want to be caught being violent on camera",
)

videocamera = GameObject(
    name="Video Camera",
    object_description="An HD video camera used by journalists across the globe",
    attack_description="Show the world the degeneracy of your opponent",
    durability=1,
    accuracy=60,
    speed=1,
    strength=0,
    debuff=videocamera_debuff,
    buff=None,
    sprites=["videocamera.png"],
)

OBJECTS.append(videocamera)

# ====================================================

nail = GameObject(
    name="Nail",
    object_description="A somewhat large and pointy nail",
    attack_description="Stab the opponent with the nail",
    durability=2,
    accuracy=70,
    speed=5,
    strength=2,
    debuff=None,
    buff=None,
    sprites=["nail.png"],
)

OBJECTS.append(nail)

# ====================================================