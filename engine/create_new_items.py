from base_objects import beaker, drill, microphone
from game_object import GameObject, Modifier
import json
from openai import OpenAI


# ================== helper methods
def stringify(game_object):
    '''
    Returns a string rep of a GameObject `game_object`
    '''
    return str(game_object.model_dump())


# ================== openAI API calls
client = OpenAI()

system_prompt = '''
You are GameObjectGPT, a language model specialized in generating objects in games. Given a list of component parts, you are to come up with an inventive weapon or item that uses all those parts and assign an attack strength, as well as buffs or debuffs, to that item in the form of a JSON.

Some example parts include:
Beaker: {0}
Microphone: {1}
Drill: {2}

Do not include any explanations, only provide a RFC8259 compliant JSON response following this format without deviation:
{{
  "name": "name of the item",
  "object_description": "short, one-sentence description of the item",
  "attack_description": "short, one-sentence description of how that item is used in an attack",
  "durability": integer r   epresenting the number of uses for this item,
  "accuracy": integer representing the accuracy. An accuracy value of 70 means that the attack is 70\% accurate,
  "speed": integer representing the number of times the object can act within a fixed amount of time,
  "strength": integer representing the amount of damage each individual attack by this item does,
  "debuff": {{
    "stat_affected": "one of accuracy or speed",
    "value": integer representing how much `stat_affected` is reduced,
    "duration": integer repreenting the number of opponent turns over which `stat_affected` is reduced,
    "reason": "short, one-sentence description of how the debuff works"
  }} or None,
  "buff": {{
    "stat_affected": "one of accuracy or speed",
    "value": integer representing how much `stat_affected` is increased,
    "duration": integer representing the number of player turns over which `stat_affected` is increased,
    "reason": "short, one-sentence description of how the buff works"
  }} or None,
}}
'''.format(stringify(beaker), stringify(microphone), stringify(drill))


def generate_ai_gameobject(user_selected_items):
    user_prompt = '''
    PLAYER-SELECTED PARTS:
    %s

    ADDITIONAL MATERIALS YOU CAN USE TO COMBINE PLAYER-SELECTED PARTS:
    - Twine
    - Tape
    - Gorilla glue

    The JSON response:
    ''' % '\n'.join([stringify(item) for item in user_selected_items])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    # convert the response to GameObject and Modifiers for type checking
    json_response = response.choices[0].message.content
    game_object_dict = json.loads(json_response)

    if game_object_dict["debuff"] is not None:
        debuff = Modifier(**game_object_dict["debuff"])
        game_object_dict["debuff"] = debuff
    if game_object_dict["buff"] is not None:
        buff = Modifier(**game_object_dict["buff"])
        game_object_dict["buff"] = buff

    game_object = GameObject(**game_object_dict)
    return game_object
