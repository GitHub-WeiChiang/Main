__author__ = "ChiangWei"
__date__ = "2022/5/30"

import cProfile
import sorting
import random

l = list(range(500))
random.shuffle(l)
cProfile.run('sorting.selectionSort(l)')
