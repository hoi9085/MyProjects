    #!/usr/bin/env python3

import sys
import random
import common 


def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))


def codemaker(combinaison):
    global solution
    return common.evaluation(combinaison, solution)