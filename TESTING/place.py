from random import sample
import random
from telegram import InputMediaPhoto
import config

place = {
    "001":{
        'name' : 'Rec centre // 游泳馆',
        'pokemon' : ['007','008','009','054','055','060','061','062']
    },
    "002":{
        "name":"Christmas Park // 圣诞公园",
        'pokemon':["001",'002','003']
    }
}

pokemon = {
    '001':{
        'name': 'Bulbasaur 妙蛙种子',
        'hp': [200,294],
        'lvl': [1,16],
        'atk': [92,216],
        'Catch rate': 45,
        'pktype': 'Grass',
        'upgrade': '002'
    },
    '002':{
        'name': 'Ivysaur 妙蛙草',
        'hp': [230,324],
        'lvl': [16,32],
        'atk': [116,245],
        'Catch rate': 45,
        'pktype': 'Grass',
        'upgrade': '003'
    },
    '003':{
        'name': 'Venusaur 妙蛙草',
        'hp': [230,324],
        'lvl': [16,32],
        'atk': [116,245],
        'Catch rate': 45,
        'pktype': 'Grass',
        'upgrade': '003'
    },
    "007":{
        'name': 'Squirtle 杰尼龟',
        'hp': [198,292],
        'lvl': [1,16],
        'atk': [90,214],
        'Catch rate': 45,
        'pktype': 'Water',
        'upgrade': '008'
    },
    "008":{
        'name': 'Wartortle 卡咪龟',
        'hp': [228,322],
        'lvl': [16,36],
        'atk': [117,247],
        'Catch rate': 45,
        'pktype': 'Water',
        'upgrade': '009'
    },
    "009":{
        'name': 'Blastoise 水箭龟',
        'hp': [268,362],
        'lvl': [36,100],
        'atk': [153,291],
        'Catch rate': 45,
        'pktype': 'Water',
        'upgrade': ''
    },
    "054":{
        'name': 'Psyduck 可达鸭',
        'hp': [210,304],
        'lvl': [1,33],
        'atk': [90,223],
        'Catch rate': 90,
        'pktype': 'Water',
        'upgrade': '055'
    },
    "055":{
        'name': 'Golduck 哥达鸭',
        'hp': [270,364],
        'lvl': [33,100],
        'atk': [152,289],
        'Catch rate': 75,
        'pktype': 'Water',
        'upgrade': ''
    },
    "060":{
        'name': 'Poliwag 蚊香蝌蚪',
        'hp': [190,284],
        'lvl': [1,25],
        'atk': [94,218],
        'Catch rate': 95,
        'pktype': 'Water',
        'upgrade': '061'
    },
    "061":{
        'name': 'Poliwhirl 蚊香蝌蚪',
        'hp': [190,284],
        'lvl': [25,100],
        'atk': [94,218],
        'Catch rate': 90,
        'pktype': 'Water',
        'upgrade': '062'
    },
    "062":{
        'name': 'Poliwrath 蚊香蝌蚪',
        'hp': [190,284],
        'lvl': [25,100],
        'atk': [94,218],
        'Catch rate': 45,
        'pktype': 'Water',
        'upgrade': ''
    }
}

class Place:
    id = ''
    name = ''
    pokemon = []

    def __init__(self,id):
        self.id = id
        self.name = place[id]['name']
        self.pokemon = sample(place[id]['pokemon'],3)
        self.pokemon += sample(place[id]['pokemon'],2)
    
    def __str__(self):
        return str(self.__dict__)


class Pokemon():
    id = ''
    name = ''
    hp = 0
    lvl = 0
    atk = 0
    catchrate = 0.0
    pktype = ''
    upgrade = ''

    def getPhoto(self):
        file_name = f"{config.run_path}/images/{self.id}.jpg"
        # return InputMediaPhoto(media=open(file_name,'rb'))
        return file_name

    def __init__(self,id:str):
        self.id = id
        self.name = pokemon[id]['name']
        self.lvl = random.randint(pokemon[id]['lvl'][0],pokemon[id]['lvl'][1])
        maxhp = random.randint(pokemon[id]['hp'][0],pokemon[id]['hp'][1])
        lvlnum = pokemon[id]['lvl'][1] - pokemon[id]['lvl'][0]
        hpperlvl = int(maxhp / lvlnum)
        self.hp = hpperlvl * self.lvl
        maxatk = random.randint(pokemon[id]['atk'][0],pokemon[id]['atk'][1])
        atkperlvl = int(maxatk / lvlnum)
        self.atk = atkperlvl * self.lvl
        self.catchrate = pokemon[id]['Catch rate']
        self.pktype = pokemon[id]['pktype']
        self.upgrade = pokemon[id]['upgrade']
    
    @classmethod
    def init(self,id:str,name:str,lvl:int,hp:int,atk:int,catchrate:int,pktype:str,upgrade:str):
        p = Pokemon(id)
        p.lvl = lvl
        p.hp = hp
        p.atk = atk
        p.catchrate = catchrate
        p.pktype = pktype
        p.upgrade = upgrade
        return p
    
    @classmethod
    def init_from_dict(self,pdict):
        p = Pokemon(pdict['id'])
        p.lvl = pdict['lvl']
        p.hp = pdict['hp']
        p.atk = pdict['atk']
        p.catchrate = pdict['catchrate']
        p.pktype = pdict['pktype']
        p.upgrade = pdict['upgrade']
        return p

    def __str__(self):
        return str(self.__dict__)

def find_place():
    ps = list(place.keys())
    ps1 = sample(ps,2)
    ps = []
    for p in ps1:
        ps.append(Place(p))
    return ps

if __name__ == '__main__':
    # {'id': '001', 'name': 'Rec centre // 游泳馆', 'pokemon': ['009', '007', '062', '055', '009']}
    # {'id': '009', 'name': 'Blastoise 水箭龟', 'lvl': 86, 'hp': 344, 'atk': 258, 'catchrate': 5.9, 'pktype': 'Water', 'upgrade': ''}
    # 创建一个场所
    p1 = Place('001')        
    print(p1)
    # 创建一个pokemon
    p2 = Pokemon(id=p1.pokemon[0])
    print(p2)
    # 按指定的值还原一个pokemon
    p3 = Pokemon.init('009','Blastoise 水箭龟',40,388,291,5.9,'Water','')
    print(p3)
    #  从一个dict 还原一个 pokemon
    p = {'id': '009', 'name': 'Blastoise 水箭龟', 'lvl': 40, 'hp': 388, 'atk': 291, 'catchrate': 5.9, 'pktype': 'Water', 'upgrade': ''}
    print(Pokemon.init_from_dict(p))