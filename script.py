"""Main story generation script"""

import character
import puncuate
import verb

CAST = {'hero': character.generate('good'),
        'villian': character.generate('bad'),
        'support': character.generate('help'),
        'love': character.generate('love')}

VERB = verb.get('present')

print puncuate.dec('%s %s %s here'
                   % (CAST['hero']['first'],
                      CAST['hero']['last'],
                      VERB[1]))
