##########
# Import #
##########


import random
from collections import namedtuple

import constants


################
# Memory Class #
################


Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))


class Memory(object):
    def __init__(self, capacity=constants.MEMORY_CAPACITY):
        self.capacity = capacity
        self.memory = []
        self.position = 0
        

    def push(self, *args):
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        self.position = (self.position + 1) % self.capacity


    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)
