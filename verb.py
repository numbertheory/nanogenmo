"""Get a random verb, from a given tense"""

import random


def get(tense):
    """ Get a verb in the right tense """
    verbs = {'past': ['spoke', 'baked', 'competed',
                      'smoked', 'switched', 'unlocked'],
             'present': ['speaks', 'bakes', 'competes',
                         'smokes', 'switches', 'unlocks'],
             'future': ['speak', 'bake', 'compete',
                        'smoke', 'switch', 'unlock'],
             'past_perfect': ['spoken', 'baked', 'competed',
                              'smoked', 'switched', 'unlocked'],
             'future_perfect': ['spoken', 'baked',
                                'competed', 'smoked',
                                'switched', 'unlocked']}
    if tense == 'future':
        helper = ['will', '']
    elif 'future_perfect':
        helper = ['will', 'have']
    elif 'past_perfect':
        helper = ['had', '']
    else:
        helper = ['', '']
    return helper, random.choice(verbs[tense])
