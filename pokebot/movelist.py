import random

moves = {
    "Absorb":{
        'power': 20,
        'pktype': 'Grass',
        'acc': 100,
        'selfdmg': -10,
        'pp': 25,
        'recharge': False,
        'charge': 0,
        'timesperturn': [1,1],
        'raise': [0,0,0],
        'eraise': [0,0,0],
        'raiser': [0,0,0],
        'eraiser': [0,0,0]
    },
    "Acid":{
        'power': 40,
        'pktype': 'Poison',
        'acc': 100,
        'selfdmg': 0,
        'pp': 30,
        'recharge': False,
        'charge': 0,
        'timesperturn': [1,1],
        'raise': [0,0,0],
        'eraise': [0,-1,0],
        'raiser': [0,0,0],
        'eraiser': [0,20,0]
    },
    "Acid Armor":{
        'power': 0,
        'pktype': 'Poison',
        'acc': 100,
        'selfdmg': 0,
        'pp': 20,
        'recharge': False,
        'charge': 0,
        'timesperturn': [1,1],
        'raise': [0,1,0],
        'eraise': [0,0,0],
        'raiser': [0,100,0],
        'eraiser': [0,0,0]
    },
    "Agility":{
        'power': 0,
        'pktype': 'Psychic',
        'acc': 100,
        'selfdmg': 0,
        'pp': 30,
        'recharge': False,
        'charge': 0,
        'timesperturn': [1,1],
        'raise': [0,0,2],
        'eraise': [0,0,0],
        'raiser': [0,0,100],
        'eraiser': [0,0,0]
    },
    "Amnesia":{
        'power': 0,
        'pktype': 'Psychic',
        'acc': 100,
        'selfdmg': 0,
        'pp': 20,
        'recharge': False,
        'charge': 0,
        'timesperturn': [1,1],
        'raise': [0,2,0],
        'eraise': [0,0,0],
        'raiser': [0,100,0],
        'eraiser': [0,0,0]
    }
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
    enemyatkraise = 0
    enemydefraise = 0
    enemyspdraise = 0
    atkraiserate = 0
    defraiserate = 0
    spdraiserate = 0
    enemyatkraiserate = 0
    enemydefraiserate = 0
    enemyspdraiserate = 0

    def __init__(self,name:str):
        self.name = name
        self.power = moves[name]['power']
        self.pktype = moves[name]['pktype']
        self.accuracy = moves[name]['acc']
        self.selfdmg = moves[name]['recoil']
        self.pp = moves[name]['pp']
        self.recharge = moves[name]['recharge']
        self.charge = moves[name]['charge']
        self.timesperturn = moves[name]['timesperturn']
        self.atkraise,self.defraise,self.spdraise = moves[name]['raise']
        self.enemyatkraise,self.enemydefraise,self.ememyspdraise = moves[name]['eraise']
        self.atkraiserate,self.defraiserate,self.spdraiserate = moves[name]['raiser']
        self.enemyatkraiserate,self.enemydefraiserate,self.ememyspdraiserate = moves[name]['eraiser']

    def __str__(self):
        return str(self.__dict__)