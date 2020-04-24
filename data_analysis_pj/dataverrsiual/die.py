from random import randint

class Die():
    '''表示一个掷色子的类'''

    def __init__(self,num_sides=6):
        '''默认认为色子是6面的'''
        self.num_sides=num_sides

    def roll(self):
        '''返回色子点数'''
        return randint(1,self.num_sides)

