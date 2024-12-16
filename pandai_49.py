
BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

!rm -rf othello2024
!git clone https://github.com/kkuramitsu/othello2024.git

from othello2024.neko64 import nekoAI

!pip install -U kogi-canvas

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from collections import deque

from kogi_canvas import play_othello, PandaAI
