"""Main story generation script"""

import character
import puncuate

HERO = character.generate('good')
VILLIAN = character.generate('bad')
SUPPORT = character.generate('help')
LOVE = character.generate('love')


print puncuate.dec("the hero of this story is %s %s"
                   % (HERO['first'], HERO['last']))
print puncuate.dec("%s is fighting %s %s"
                   % (HERO['pronouns'][0], VILLIAN['first'],
                      VILLIAN['last']))
print puncuate.dec("%s %s is a supporting character"
                   % (SUPPORT['first'], SUPPORT['last']))
print puncuate.dec("%s is interested in %s %s"
                   % (HERO['first'], LOVE['first'], LOVE['last']))
