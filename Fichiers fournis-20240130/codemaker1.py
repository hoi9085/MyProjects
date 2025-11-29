    #!/usr/bin/env python3

import sys
import random
import common  # N'utilisez pas la syntaxe "from common import XXX"


def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))


def codemaker(combinaison):
    global solution
    return common.evaluation(combinaison, solution)