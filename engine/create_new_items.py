import os

from base_objects import beaker, drill, microphone
from game_object import GameObject, Modifier
import json
from openai import OpenAI
from env import OPENAI_API_KEY


# ================== helper methods
def stringify(game_object):
    '''
    Returns a string rep of a GameObject `game_object` without the file name
    '''
    return str(game_object.model_dump(exclude=["sprites"]))


# ================== openAI API calls
client = OpenAI(
    api_key=OPENAI_API_KEY
)

system_prompt = '''
You are GameObjectGPT, a language model specialized in generating objects in games. Given a list of component parts, you are to come up with an inventive weapon or item that uses ALL those parts and assign an attack strength, as well as buffs or debuffs, to that item in the form of a JSON.

It is absolutely imperative that you use every item given to you in some fashion. Only provide at most one of a buff or debuff, NEVER both. 

The success of the game depends on your creativity. Thank you for your service.

Do not include any explanations, only provide a RFC8259 compliant JSON response following this format without deviation:
{{
  "name": "creative name for the item",
  "object_description": "short, one-sentence description of the item",
  "attack_description": "short, one-sentence description of how that item is used in an attack",
  "durability": integer r   epresenting the number of uses for this item,
  "accuracy": integer representing the accuracy. An accuracy value of 70 means that the attack is 70\% accurate,
  "speed": integer representing the number of times the object can act within a fixed amount of time,
  "strength": integer representing the amount of damage each individual attack by this item does,
  "debuff": null or {{
    "stat_affected": "accuracy, speed, or strength",
    "value": integer representing how much `stat_affected` is reduced,
    "duration": integer repreenting the number of opponent turns over which `stat_affected` is reduced,
    "reason": "short, one-sentence description of how the debuff works"
  }},
  "buff": null or {{
    "stat_affected": "accuracy, speed, or strength",
    "value": integer representing how much `stat_affected` is increased,
    "duration": integer representing the number of player turns over which `stat_affected` is increased,
    "reason": "short, one-sentence description of how the buff works"
  }},
}}
'''


def generate_ai_gameobject(user_selected_items, user_request):
    user_prompt = '''
    PLAYER-SELECTED PARTS:
    {0}

    ADDITIONAL INSTRUCTIONS FROM THE PLAYER:
    {1}

    The JSON response:
    '''.format(
        '\n'.join([stringify(item) for item in user_selected_items]),
        user_request
    )

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

    sprites = []
    for obj in user_selected_items:
        sprites.extend(obj.sprites)

    game_object_dict["file"] = "beaker.png" # no generative images for now
    game_object = GameObject(**game_object_dict, sprites=sprites)
    print ("returned GameObject: {}".format(stringify(game_object)))
    return game_object
