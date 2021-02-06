import random

moves = {

}

class Move():
    name = ''
    power = 0
    pktype = ''
    accuracy = 0
    selfdmg = 0
    pp = 0
    recharge = False
    charge = 0
    timesperturn = []
    atkraise = 0
    defraise = 0
    spdraise = 0

    def __init__(self,name:str):
        self.name = name
        self.power = moves[name]['power']
        self.pktype = moves[name]['pktype']
        self.accuracy = moves[name]['accuracy']
        self.selfdmg = moves[name]['recoil']
        self.pp = moves[name]['pp']
        self.recharge = moves[name]['recharge']
        self.charge = moves[name]['charge']
        self.timesperturn = moves[name]['timesperturn']
        self.atkraise = moves[name]['atkraise']
        self.defraise = moves[name]['defraise']
        self.spdraise = moves[name]['spdraise']

    def __str__(self):
        return str(self.__dict__)