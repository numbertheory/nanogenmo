"""Generate a character"""

import random

# All characters are defined here in lists.  The generator
# will randomly select a name from each list.
#  Good : Hero
#  Bad: Villian
#  Help: Supporting Character
#  Love: Love interest


def generate(alignment):
    """Return a character based on alignment"""
    characters = {'good': [{'first': 'Jack', 'last': 'Goodguy',
                            'pronouns': ['he', 'him', 'his']},
                           {'first': 'Wanda', 'last': 'Smart',
                            'pronouns': ['she', 'her', 'her']},
                           {'first': 'Lancelot', 'last': 'Jones',
                            'pronouns': ['he', 'him', 'his']},
                           {'first': 'Melinda', 'last': 'Star',
                            'pronouns': ['she', 'her', 'her']}],
                  'bad': [{'first': 'Roy', 'last': 'Traitor',
                           'pronouns': ['he', 'him', 'his']},
                          {'first': 'Noire', 'last': 'Fatale',
                           'pronouns': ['she', 'her', 'her']},
                          {'first': 'Norman', 'last': 'Styles',
                           'pronouns': ['he', 'him', 'his']},
                          {'first': 'Melinda', 'last': 'Blackheart',
                           'pronouns': ['she', 'her', 'her']}],
                  'help': [{'first': 'Stan', 'last': 'Hughes',
                            'pronouns': ['he', 'him', 'his']},
                           {'first': 'Leslie', 'last': 'Duggan',
                            'pronouns': ['she', 'her', 'her']},
                           {'first': 'Joseph', 'last': 'Tankome',
                            'pronouns': ['he', 'him', 'his']},
                           {'first': 'Samantha', 'last': 'Templer',
                            'pronouns': ['she', 'her', 'her']}],
                  'love': [{'first': 'Sanford', 'last': 'Spelltion',
                            'pronouns': ['he', 'him', 'his']},
                           {'first': 'Penelope', 'last': 'Lewis',
                            'pronouns': ['she', 'her', 'her']},
                           {'first': 'Adelaide', 'last': 'Markson',
                            'pronouns': ['he', 'him', 'his']},
                           {'first': 'Guinevere', 'last': 'Simpson',
                            'pronouns': ['she', 'her', 'her']}]}
    return random.choice(characters[alignment])
