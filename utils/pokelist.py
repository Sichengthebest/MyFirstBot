from random import sample
import random
from telegram import InputMediaPhoto
import config

       
rarity = {
    'l':['144','145','146','150','151','243','244','245','249','250','251','377','378','379','380','381','382','383','384','385','386'],
    's':['003','006','009','036','038','059','065','068','076','083','094','115','127','128','130','131','132','134','135','136','142','143','149','154','157','160','186','196','197','201','208','212','213','226','227','230','235','241','242','248','254','257','260','282','289','302','335','336','337','338','350','351','352','357','358','359','367','368','369','373','376','389','392','395','398','405','407'],
    'r':['002','005','008','012','015','018','026','031','034','035','040','045','062','071','073','078','085','091','095','103','106','107','108','113','121','122','124','139','141','148','153','156','159','169','176','181','182','184','185','189','199','202','233','237','247','253','256','259','267','269','272','275','281','288','291','292','295','306','315','319','321','330','334','344','346','348','365','372','375','388','391','394','404','409','411'],
    'u':['001','004','007','011','014','017','020','022','024','025','028','030','033','037','039','042','044','047','049','051','053','055','057','058','061','064','067','070','072','075','077','080','082','084','087','089','093','097','099','101','105','110','112','114','117','119','123','125','126','133','138','140','147','152','155','158','162','164','166','168','171','172','173','174','175','178','180','183','188','190','192','193','195','198','200','203','205','206','207','210','211','214','215','217','219','221','222','224','225','229','232','234','236','238','239','240','246','252','255','258','262','264','266','268','271','274','277','279','280','284','286','287','290','294','297','298','299','301','303','305','308','310','311','312','313','314','317','318','320','323','324','326','327','329','332','333','340','342','343','345','347','349','354','356','360','362','364','366','370','371','374','387','390','393','397','400','402','403','406','408','410'],
    'c':['010','013','016','019','021','023','027','029','032','041','043','046','048','050','052','054','056','060','063','066','069','074','079','081','086','088','090','092','096','098','100','102','104','109','111','116','118','120','129','137','161','163','165','167','170','177','179','187','191','194','204','209','216','218','220','223','228','231','261','263','265','270','273','276','278','283','285','293','296','300','304','307','309','316','322','325','328','331','339','341','353','355','361','363','396','399','401']
}

def getPokemon():
    rarityroll = random.randint(1,1000)
    if rarityroll <= 500:
        pokemons = rarity['c']
        rarityy = 'c'
    elif rarityroll > 500 and rarityroll <= 760:
        pokemons = rarity['u']
        rarityy = 'u'
    elif rarityroll > 760 and rarityroll <= 950:
        pokemons = rarity['r']
        rarityy = 'r'
    elif rarityroll > 950 and rarityroll <= 997:
        pokemons = rarity['s']
        rarityy = 's'
    elif rarityroll > 997 and rarityroll <= 1000:
        pokemons = rarity['l']
        rarityy = 'l'
    pk = random.choice(pokemons)
    return pk,rarityy

pokemon = {
    '001':{
        'name': 'Bulbasaur',
        'hp': [200,294],
        'lvl': [1,15],
        'atk': [92,216],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['002']
    },
    '002':{
        'name': 'Ivysaur',
        'hp': [230,324],
        'lvl': [16,31],
        'atk': [116,245],
        'speed': [112,240],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['003']
    },
    '003':{
        'name': 'Venusaur',
        'hp': [270,364],
        'lvl': [32,100],
        'atk': [152,289],
        'speed': [148,284],
        'Catch rate': [25,40,55,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['']
    },
    "004":{
        'name': 'Charmander',
        'hp': [188,282],
        'lvl': [1,15],
        'atk': [98,223],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['005']
    },
    "005":{
        'name': 'Charmeleon',
        'hp': [226,320],
        'lvl': [16,35],
        'atk': [119,249],
        'speed': [148,284],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fire'],
        'upgrade': ['006']
    },
    "006":{
        'name': 'Charizard',
        'hp': [266,360],
        'lvl': [36,100],
        'atk': [155,293],
        'speed': [184,328],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire','Flying'],
        'upgrade': ['']
    },
    "007":{
        'name': 'Squirtle',
        'hp': [198,292],
        'lvl': [1,15],
        'atk': [90,214],
        'speed': [81,203],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['008']
    },
    "008":{
        'name': 'Wartortle',
        'hp': [228,322],
        'lvl': [16,35],
        'atk': [117,247],
        'speed': [108,236],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water'],
        'upgrade': ['009']
    },
    "009":{
        'name': 'Blastoise',
        'hp': [268,362],
        'lvl': [36,100],
        'atk': [153,291],
        'speed': [144,280],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "010":{
        'name': 'Caterpie',
        'hp': [200,294],
        'lvl': [1,6],
        'atk': [58,174],
        'speed': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug'],
        'upgrade': ['011']
    },
    "011":{
        'name': 'Metapod',
        'hp': [210,304],
        'lvl': [7,9],
        'atk': [40,152],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug'],
        'upgrade': ['012']
    },
    "012":{
        'name': 'Butterfree',
        'hp': [230,324],
        'lvl': [10,100],
        'atk': [85,207],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Bug','Flying'],
        'upgrade': ['']
    },
    "013":{
        'name': 'Weedle',
        'hp': [190,284],
        'lvl': [1,6],
        'atk': [67,185],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['014']
    },
    "014":{
        'name': 'Kakuna',
        'hp': [200,294],
        'lvl': [7,9],
        'atk': [49,163],
        'speed': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['015']
    },
    "015":{
        'name': 'Beedrill',
        'hp': [240,334],
        'lvl': [10,100],
        'atk': [166,306],
        'speed': [139,273],
        'Catch rate': [45,60,75,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['']
    },
    "016":{
        'name': 'Pidgey',
        'hp': [190,284],
        'lvl': [1,17],
        'atk': [85,207],
        'speed': [105,232],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['017']
    },
    "017":{
        'name': 'Pidgeotto',
        'hp': [236,330],
        'lvl': [18,35],
        'atk': [112,240],
        'speed': [132,265],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['018']
    },
    "018":{
        'name': 'Pidgeot',
        'hp': [276,370],
        'lvl': [36,100],
        'atk': [148,284],
        'speed': [186,331],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "019":{
        'name': 'Rattata',
        'hp': [170,264],
        'lvl': [1,19],
        'atk': [105,232],
        'speed': [134,267],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['020']
    },
    "020":{
        'name': 'Raticate',
        'hp': [220,314],
        'lvl': [20,100],
        'atk': [150,287],
        'speed': [179,322],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "021":{
        'name': 'Spearow',
        'hp': [190,284],
        'lvl': [1,19],
        'atk': [112,240],
        'speed': [130,262],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['022']
    },
    "022":{
        'name': 'Fearow',
        'hp': [240,334],
        'lvl': [20,100],
        'atk': [166,306],
        'speed': [184,328],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "023":{
        'name': 'Ekans',
        'hp': [180,274],
        'lvl': [1,21],
        'atk': [112,240],
        'speed': [103,229],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison'],
        'upgrade': ['024']
    },
    "024":{
        'name': 'Arbok',
        'hp': [230,324],
        'lvl': [22,100],
        'atk': [175,314],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison'],
        'upgrade': ['']
    },
    "025":{
        'name': 'Pikachu',
        'hp': [180,274],
        'lvl': [1,100],
        'atk': [103,229],
        'speed': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['026']
    },
    "026":{
        'name': 'Raichu',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [202,350],
        'Catch rate': [45,60,75,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "027":{
        'name': 'Sandshrew',
        'hp': [210,304],
        'lvl': [1,21],
        'atk': [139,273],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ground'],
        'upgrade': ['028']
    },
    "028":{
        'name': 'Sandslash',
        'hp': [260,354],
        'lvl': [22,100],
        'atk': [184,328],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground'],
        'upgrade': ['']
    },
    "029":{
        'name': 'Nidoran-♀',
        'hp': [220,314],
        'lvl': [1,15],
        'atk': [89,212],
        'speed': [78,199],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison'],
        'upgrade': ['030']
    },
    "030":{
        'name': 'Nidorina',
        'hp': [250,344],
        'lvl': [16,35],
        'atk': [116,245],
        'speed': [105,232],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison'],
        'upgrade': ['031']
    },
    "031":{
        'name': 'Nidoqueen',
        'hp': [290,384],
        'lvl': [36,100],
        'atk': [170,311],
        'speed': [141,276],
        'Catch rate': [45,60,75,100],
        'pktype': ['Poison'],
        'upgrade': ['']
    },
    "032":{
        'name': 'Nidoran-♂︎',
        'hp': [202,292],
        'lvl': [1,15],
        'atk': [107,234],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison'],
        'upgrade': ['033']
    },
    "033":{
        'name': 'Nidorino',
        'hp': [232,326],
        'lvl': [16,35],
        'atk': [134,267],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison'],
        'upgrade': ['034']
    },
    "034":{
        'name': 'Nidoking',
        'hp': [272,366],
        'lvl': [36,100],
        'atk': [188,333],
        'speed': [157,295],
        'Catch rate': [45,60,75,100],
        'pktype': ['Poison'],
        'upgrade': ['']
    },
    "035":{
        'name': 'Clefairy',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [85,207],
        'speed': [67,185],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fairy'],
        'upgrade': ['036']
    },
    "036":{
        'name': 'Clefable',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [130,262],
        'speed': [112,240],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fairy'],
        'upgrade': ['']
    },
    "037":{
        'name': 'Vulpix',
        'hp': [186,280],
        'lvl': [1,100],
        'atk': [78,199],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['038']
    },
    "038":{
        'name': 'Ninetales',
        'hp': [256,350],
        'lvl': [1,100],
        'atk': [141,276],
        'speed': [184,328],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire'],
        'upgrade': ['']
    },
    "039":{
        'name': 'Jigglypuff',
        'hp': [340,434],
        'lvl': [1,100],
        'atk': [85,207],
        'speed': [40,152],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fairy'],      
        'upgrade': ['040']
    },
    "040":{
        'name': 'Wigglytuff',
        'hp': [390,484],
        'lvl': [1,100],
        'atk': [130,262],
        'speed': [85,207],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fairy'],        
        'upgrade': ['']
    },
    "041":{
        'name': 'Zubat',
        'hp': [190,284],
        'lvl': [1,21],
        'atk': [85,207],
        'speed': [103,229],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison','Flying'],        
        'upgrade': ['042']
    },
    "042":{
        'name': 'Golbat',
        'hp': [260,354],
        'lvl': [22,100],
        'atk': [148,284],
        'speed': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison','Flying'],
        'upgrade': ['169']
    },
    "043":{
        'name': 'Oddish',
        'hp': [200,294],
        'lvl': [1,20],
        'atk': [94,218],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass','Poison'],  
        'upgrade': ['044']
    },
    "044":{
        'name': 'Gloom',
        'hp': [230,324],
        'lvl': [21,100],
        'atk': [121,251],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Poison'],         
        'upgrade': ['045','182']
    },
    "045":{
        'name': 'Vileplume',
        'hp': [260,354],
        'lvl': [21,100],
        'atk': [148,284],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass','Poison'],        
        'upgrade': ['']
    },
    "046":{
        'name': 'Paras',
        'hp': [180,274],
        'lvl': [1,23],
        'atk': [130,262],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug','Grass'],        
        'upgrade': ['047']
    },
    "047":{
        'name': 'Parasect',
        'hp': [230,324],
        'lvl': [24,100],
        'atk': [175,317],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Grass'],         
        'upgrade': ['']
    },
    "048":{
        'name': 'Venonat',
        'hp': [230,324],
        'lvl': [1,30],
        'atk': [103,229],
        'speed': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug','Poison'],         
        'upgrade': ['049']
    },
    "049":{
        'name': 'Venomoth',
        'hp': [250,344],
        'lvl': [31,100],
        'atk': [121,251],
        'speed': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['']
    },
    "050":{
        'name': 'Diglett',
        'hp': [130,224],
        'lvl': [1,25],
        'atk': [103,229],
        'speed': [175,317],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ground'],         
        'upgrade': ['051']
    },
    "051":{
        'name': 'Dugtrio',
        'hp': [180,274],
        'lvl': [26,100],
        'atk': [184,328],
        'speed': [220,372],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground'],    
        'upgrade': ['']
    },
    "052":{
        'name': 'Meowth',
        'hp': [190,284],
        'lvl': [1,27],
        'atk': [85,207],
        'speed': [166,306],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],         
        'upgrade': ['053']
    },
    "053":{
        'name': 'Persian',
        'hp': [240,334],
        'lvl': [28,100],
        'atk': [130,262],
        'speed': [211,361],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],        
        'upgrade': ['']
    },
    "054":{
        'name': 'Psyduck',
        'hp': [210,304],
        'lvl': [1,32],
        'atk': [98,223],
        'speed': [103,229],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['055']
    },
    "055":{
        'name': 'Golduck',
        'hp': [270,364],
        'lvl': [33,100],
        'atk': [152,289],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],        
        'upgrade': ['']
    },
    "056":{
        'name': 'Mankey',
        'hp': [190,284],
        'lvl': [1,27],
        'atk': [148,284],
        'speed': [130,262],
        'Catch rate': [75,85,95,100],
        'pktype': ['Fighting'],         
        'upgrade': ['057']
    },
    "057":{
        'name': 'Primeape',
        'hp': [240,334],
        'lvl': [28,100],
        'atk': [193,339],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fighting'],        
        'upgrade': ['']
    },
    "058":{
        'name': 'Growlithe',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [130,262],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],      
        'upgrade': ['059']
    },
    "059":{
        'name': 'Arcanine',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [202,350],
        'speed': [175,317],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire'],        
        'upgrade': ['']
    },
    "060":{
        'name': 'Poliwag',
        'hp': [190,284],
        'lvl': [1,24],
        'atk': [94,218],
        'speed': [166,306],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['061']
    },
    "061":{
        'name': 'Poliwhirl',
        'hp': [240,334],
        'lvl': [25,100],
        'atk': [121,251],
        'speed': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['062','186']
    },
    "062":{
        'name': 'Poliwrath',
        'hp': [290,384],
        'lvl': [25,100],
        'atk': [175,317],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "063":{
        'name': 'Abra',
        'hp': [160,254],
        'lvl': [1,15],
        'atk': [40,152],
        'speed': [166,306],
        'Catch rate': [75,85,95,100],
        'pktype': ['Psychic'],
        'upgrade': ['064']
    },
    "064":{
        'name': 'Kadabra',
        'hp': [190,284],
        'lvl': [16,100],
        'atk': [67,185],
        'speed': [193,339],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': ['065']
    },
    "065":{
        'name': 'Alakazam',
        'hp': [220,314],
        'lvl': [16,100],
        'atk': [94,218],
        'speed': [220,372],
        'Catch rate': [25,40,55,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "066":{
        'name': 'Machop',
        'hp': [250,344],
        'lvl': [1,27],
        'atk': [148,284],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Fighting'],
        'upgrade': ['067']
    },
    "067":{
        'name': 'Machoke',
        'hp': [270,364],
        'lvl': [28,100],
        'atk': [184,328],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fighting'],
        'upgrade': ['068']
    },
    "068":{
        'name': 'Machamp',
        'hp': [290,384],
        'lvl': [28,100],
        'atk': [238,394],
        'speed': [103,229],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fighting'],
        'upgrade': ['']
    },
    "069":{
        'name': 'Bellsprout',
        'hp': [210,304],
        'lvl': [1,20],
        'atk': [139,273],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass','Poison'],
        'upgrade': '070'
    },
    "070":{
        'name': 'Weepinbell',
        'hp': [240,334],
        'lvl': [21,100],
        'atk': [166,306],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['071']
    },
    "071":{
        'name': 'Victreebel',
        'hp': [270,364],
        'lvl': [21,100],
        'atk': [193,339],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['']
    },
    "072":{
        'name': 'Tentacool',
        'hp': [190,284],
        'lvl': [1,29],
        'atk': [76,196],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Poison'],
        'upgrade': ['073']
    },
    "073":{
        'name': 'Tentacruel',
        'hp': [270,364],
        'lvl': [30,100],
        'atk': [130,262],
        'speed': [184,328],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Poison'],
        'upgrade': ['']
    },
    "074":{
        'name': 'Geodude',
        'hp': [190,284],
        'lvl': [1,24],
        'atk': [148,284],
        'speed': [40,152],
        'Catch rate': [75,85,95,100],
        'pktype': ['Rock','Ground'],
        'upgrade': ['075']
    },
    "075":{
        'name': 'Graveler',
        'hp': [220,314],
        'lvl': [25,100],
        'atk': [175,317],
        'speed': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock','Ground'],
        'upgrade': ['076']
    },
    "076":{
        'name': 'Golem',
        'hp': [270,364],
        'lvl': [25,100],
        'atk': [220,372],
        'speed': [85,207],
        'Catch rate': [25,40,55,100],
        'pktype': ['Rock','Ground'],
        'upgrade': ['']
    },
    "077":{
        'name': 'Ponyta',
        'hp': [210,304],
        'lvl': [1,39],
        'atk': [147,295],
        'speed': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['078']
    },
    "078":{
        'name': 'Rapidash',
        'hp': [240,334],
        'lvl': [40,100],
        'atk': [184,328],
        'speed': [193,339],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fire'],
        'upgrade': ['079']
    },
    "079":{
        'name': 'Slowpoke',
        'hp': [290,384],
        'lvl': [1,36],
        'atk': [121,251],
        'speed': [31,141],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Psychic'],
        'upgrade': ['080','199']
    },
    "080":{
        'name': 'Slobro',
        'hp': [300,394],
        'lvl': [37,100],
        'atk': [139,273],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Psychic'],
        'upgrade': ['']
    },
    "081":{
        'name': 'Magnemite',
        'hp': [160,254],
        'lvl': [1,29],
        'atk': [67,185],
        'speed': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': ['Electric','Steel'],
        'upgrade': ['082']
    },
    "082":{
        'name': 'Magneton',
        'hp': [210,304],
        'lvl': [30,100],
        'atk': [112,240],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric','Steel'],
        'upgrade': ['']
    },
    "083":{
        'name': "Farfetch'd",
        'hp': [214,308],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [112,240],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "084":{
        'name': 'Doduo',
        'hp': [180,274],
        'lvl': [1,30],
        'atk': [157,295],
        'speed': [139,273],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['085']
    },
    "085":{
        'name': 'Dodrio',
        'hp': [230,324],
        'lvl': [31,100],
        'atk': [202,350],
        'speed': [202,350],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "086":{
        'name': 'Seel',
        'hp': [240,334],
        'lvl': [1,33],
        'atk': [85,207],
        'speed': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['087']
    },
    "087":{
        'name': 'Dewgong',
        'hp': [294,384],
        'lvl': [34,100],
        'atk': [130,262],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Ice'],
        'upgrade': ['']
    },
    "088":{
        'name': 'Grimer',
        'hp': [270,364],
        'lvl': [1,37],
        'atk': [148,284],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison'],
        'upgrade': ['089']
    },
    "089":{
        'name': 'Muk',
        'hp': [320,414],
        'lvl': [38,100],
        'atk': [193,339],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison'],
        'upgrade': ['']
    },
    "090":{
        'name': 'Shellder',
        'hp': [170,264],
        'lvl': [1,100],
        'atk': [121,251],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['091']
    },
    "091":{
        'name': 'Cloyster',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [175,317],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Ice'],
        'upgrade': ['']
    },
    "092":{
        'name': 'Gastly',
        'hp': [170,264],
        'lvl': [1,24],
        'atk': [67,185],
        'speed': [148,284],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ghost','Poison'],
        'upgrade': ['093']
    },
    "093":{
        'name': 'Haunter',
        'hp': [200,294],
        'lvl': [25,100],
        'atk': [94,218],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ghost','Poison'],
        'upgrade': ['094']
    },
    "094":{
        'name': 'Gengar',
        'hp': [230,324],
        'lvl': [25,100],
        'atk': [121,251],
        'speed': [202,350],
        'Catch rate': [25,40,55,100],
        'pktype': ['Ghost','Poison'],
        'upgrade': ['']
    },
    "095":{
        'name': 'Onix',
        'hp': [180,274],
        'lvl': [1,100],
        'atk': [85,207],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock','Ground'],
        'upgrade': ['208']
    },
    "096":{
        'name': 'Drowzee',
        'hp': [230,324],
        'lvl': [1,25],
        'atk': [90,214],
        'speed': [80,201],
        'Catch rate': [75,85,95,100],
        'pktype': ['Psychic'],
        'upgrade': ['097']
    },
    "097":{
        'name': 'Hypno',
        'hp': [280,374],
        'lvl': [26,100],
        'atk': [135,269],
        'speed': [125,256],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "098":{
        'name': 'Krabby',
        'hp': [170,264],
        'lvl': [1,27],
        'atk': [193,339],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['099']
    },
    "099":{
        'name': 'Kingler',
        'hp': [220,314],
        'lvl': [28,100],
        'atk': [238,394],
        'speed': [139,273],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "100":{
        'name': 'Voltorb',
        'hp': [190,284],
        'lvl': [1,29],
        'atk': [58,174],
        'speed': [184,328],
        'Catch rate': [75,85,95,100],
        'pktype': ['Electric'],
        'upgrade': ['101']
    },
    "101":{
        'name': 'Electrode',
        'hp': [230,324],
        'lvl': [30,100],
        'atk': [94,218],
        'speed': [274,428],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "102":{
        'name': 'Exeggcute',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [76,196],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass','Psychic'],
        'upgrade': ['103']
    },
    "103":{
        'name': 'Exeggcutor',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [175,314],
        'speed': [103,229],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass','Psychic'],
        'upgrade': ['']
    },
    "104":{
        'name': 'Cubone',
        'hp': [210,304],
        'lvl': [1,27],
        'atk': [94,218],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ground'],
        'upgrade': ['105']
    },
    "105":{
        'name': 'Marowak',
        'hp': [230,324],
        'lvl': [28,100],
        'atk': [148,284],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground'],
        'upgrade': ['']
    },
    "106":{
        'name': 'Hitmonlee',
        'hp': [210,304],
        'lvl': [20,100],
        'atk': [220,372],
        'speed': [161,300],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fighting'],
        'upgrade': ['']
    },
    "107":{
        'name': 'Hitmonchan',
        'hp': [210,304],
        'lvl': [20,100],
        'atk': [193,339],
        'speed': [141,276],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fighting'],
        'upgrade': ['']
    },
    "108":{
        'name': 'Lickitung',
        'hp': [290,384],
        'lvl': [1,32],
        'atk': [103,229],
        'speed': [58,174],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "109":{
        'name': 'Koffing',
        'hp': [190,284],
        'lvl': [1,34],
        'atk': [121,251],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison'],
        'upgrade': ['110']
    },
    "110":{
        'name': 'Weezing',
        'hp': [240,334],
        'lvl': [35,100],
        'atk': [166,306],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison'],
        'upgrade': ['']
    },
    "111":{
        'name': 'Rhyhorn',
        'hp': [270,364],
        'lvl': [1,41],
        'atk': [157,295],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ground','Rock'],
        'upgrade': ['112']
    },
    "112":{
        'name': 'Rhydon',
        'hp': [320,414],
        'lvl': [42,100],
        'atk': [238,394],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground','Rock'],
        'upgrade': ['']
    },
    "113":{
        'name': 'Chansey',
        'hp': [610,704],
        'lvl': [1,100],
        'atk': [13,119],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal'],
        'upgrade': ['242']
    },
    "114":{
        'name': 'Tangela',
        'hp': [240,334],
        'lvl': [1,37],
        'atk': [103,229],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass'],
        'upgrade': ['']
    },
    "115":{
        'name': 'Kangaskhan',
        'hp': [320,414],
        'lvl': [1,100],
        'atk': [175,317],
        'speed': [166,306],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "116":{
        'name': 'Horsea',
        'hp': [170,264],
        'lvl': [1,31],
        'atk': [79,196],
        'speed': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Dragon'],
        'upgrade': ['117']
    },
    "117":{
        'name': 'Seadra',
        'hp': [220,314],
        'lvl': [32,100],
        'atk': [121,251],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Dragon'],
        'upgrade': ['230']
    },
    "118":{
        'name': 'Goldeen',
        'hp': [200,294],
        'lvl': [1,32],
        'atk': [125,256],
        'speed': [117,247],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['119']
    },
    "119":{
        'name': 'Seaking',
        'hp': [270,364],
        'lvl': [33,100],
        'atk': [170,311],
        'speed': [126,258],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "120":{
        'name': 'Staryu',
        'hp': [170,264],
        'lvl': [1,100],
        'atk': [85,207],
        'speed': [157,295],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['121']
    },
    "121":{
        'name': 'Starmie',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [211,361],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Psychic'],
        'upgrade': ['']
    },
    "122":{
        'name': 'Mr.Mime',
        'hp': [190,284],
        'lvl': [15,100],
        'atk': [85,207],
        'speed': [166,306],
        'Catch rate': [45,60,75,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "123":{
        'name': 'Scyther',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [202,350],
        'speed': [193,339],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Flying'],
        'upgrade': ['212']
    },
    "124":{
        'name': 'Jynx',
        'hp': [240,334],
        'lvl': [30,100],
        'atk': [94,218],
        'speed': [175,317],
        'Catch rate': [45,60,75,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "125":{
        'name': 'Electabuzz',
        'hp': [240,334],
        'lvl': [30,100],
        'atk': [85,207],
        'speed': [193,339],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "126":{
        'name': 'Magmar',
        'hp': [240,334],
        'lvl': [30,100],
        'atk': [175,317],
        'speed': [171,313],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['']
    },
    "127":{
        'name': 'Pinsir',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [229,383],
        'speed': [157,295],
        'Catch rate': [25,40,55,100],
        'pktype': ['Bug'],
        'upgrade': ['']
    },
    "128":{
        'name': 'Tauros',
        'hp': [260,354],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [203,350],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "129":{
        'name': 'Magikarp',
        'hp': [150,244],
        'lvl': [1,19],
        'atk': [22,130],
        'speed': [148,284],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['130']
    },
    "130":{
        'name': 'Gyarados',
        'hp': [300,394],
        'lvl': [20,100],
        'atk': [229,383],
        'speed': [150,287],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Flying'],
        'upgrade': ['']
    },
    "131":{
        'name': 'Lapras',
        'hp': [370,464],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [112,240],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Ice'],
        'upgrade': ['']
    },
    "132":{
        'name': 'Ditto',
        'hp': [206,300],
        'lvl': [1,100],
        'atk': [90,214],
        'speed': [90,214],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "133":{
        'name': 'Eevee',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [103,229],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['134','135','136','196','197']
    },
    "134":{
        'name': 'Vaporeon',
        'hp': [370,464],
        'lvl': [1,100],
        'atk': [121,251],
        'speed': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "135":{
        'name': 'Jolteon',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [121,251],
        'speed': [238,394],
        'Catch rate': [25,40,55,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "136":{
        'name': 'Flareon',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [238,394],
        'speed': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire'],
        'upgrade': ['']
    },
    "137":{
        'name': 'Porygon',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [112,240],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['233']
    },
    "138":{
        'name': 'Omanyte',
        'hp': [180,274],
        'lvl': [1,39],
        'atk': [76,196],
        'speed': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Rock'],
        'upgrade': ['139']
    },
    "139":{
        'name': 'Omastar',
        'hp': [250,344],
        'lvl': [40,100],
        'atk': [112,240],
        'speed': [103,229],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Rock'],
        'upgrade': ['']
    },
    "140":{
        'name': 'Kabuto',
        'hp': [170,264],
        'lvl': [1,39],
        'atk': [148,284],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Rock'],
        'upgrade': ['141']
    },
    "141":{
        'name': 'Kabutops',
        'hp': [230,324],
        'lvl': [40,100],
        'atk': [211,361],
        'speed': [148,284],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Rock'],
        'upgrade': ['']
    },
    "142":{
        'name': 'Aerodactyl',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [193,339],
        'speed': [238,394],
        'Catch rate': [25,40,55,100],
        'pktype': ['Rock','Flying'],
        'upgrade': ['']
    },
    "143":{
        'name': 'Snorlax',
        'hp': [430,524],
        'lvl': [1,100],
        'atk': [202,350],
        'speed': [58,174],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "144":{
        'name': 'Articuno',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [157,295],
        'Catch rate': [5,20,35,100],
        'pktype': ['Ice','Flying'],
        'upgrade': ['']
    },
    "145":{
        'name': 'Zapdos',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [184,328],
        'Catch rate': [5,20,35,100],
        'pktype': ['Electric','Flying'],
        'upgrade': ['']
    },
    "146":{
        'name': 'Moltres',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [166,306],
        'Catch rate': [5,20,35,100],
        'pktype': ['Fire','Flying'],
        'upgrade': ['']
    },
    '147':{
        'name': 'Dratini',
        'hp': [192,286],
        'lvl': [1,29],
        'atk': [119,249],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dragon'],
        'upgrade': ['148']
    },
    '148':{
        'name': 'Dragonair',
        'hp': [232,326],
        'lvl': [30,54],
        'atk': [155,293],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Dragon'],
        'upgrade': ['149']
    },
    '149':{
        'name': 'Dragonite',
        'hp': [292,386],
        'lvl': [55,100],
        'atk': [245,403],
        'speed': [148,284],
        'Catch rate': [25,40,55,100],
        'pktype': ['Dragon','Flying'],
        'upgrade': ['']
    },
    "150":{
        'name': 'Mewtwo',
        'hp': [322,416],
        'lvl': [1,100],
        'atk': [202,350],
        'speed': [238,394],
        'Catch rate': [5,20,35,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "151":{
        'name': 'Mew',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [184,328],
        'Catch rate': [5,20,35,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "152":{
        'name': 'Chikorita',
        'hp': [200,294],
        'lvl': [1,15],
        'atk': [92,216],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass'],
        'upgrade': ['153']
    },
    '153':{
        'name': 'Bayleef',
        'hp': [230,324],
        'lvl': [16,31],
        'atk': [116,245],
        'speed': [112,240],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass'],
        'upgrade': ['154']
    },
    '154':{
        'name': 'Meganium',
        'hp': [270,364],
        'lvl': [32,100],
        'atk': [152,289],
        'speed': [148,284],
        'Catch rate': [25,40,55,100],
        'pktype': ['Grass'],
        'upgrade': ['']
    },
    "155":{
        'name': 'Cyndaquil',
        'hp': [188,282],
        'lvl': [1,13],
        'atk': [98,223],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['156']
    },
    "156":{
        'name': 'Quilava',
        'hp': [226,320],
        'lvl': [14,35],
        'atk': [119,249],
        'speed': [148,284],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fire'],
        'upgrade': ['157']
    },
    "157":{
        'name': 'Typhlosion',
        'hp': [266,360],
        'lvl': [36,100],
        'atk': [155,293],
        'speed': [184,238],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire'],
        'upgrade': ['']
    },
    "158":{
        'name': 'Totodile',
        'hp': [210,304],
        'lvl': [1,17],
        'atk': [121,251],
        'speed': [81,203],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['159']
    },
    "159":{
        'name': 'Croconaw',
        'hp': [240,334],
        'lvl': [18,29],
        'atk': [148,284],
        'speed': [108,236],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water'],
        'upgrade': ['160']
    },
    "160":{
        'name': 'Feraligatr',
        'hp': [280,374],
        'lvl': [30,100],
        'atk': [193,339],
        'speed': [144,280],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "161":{
        'name': 'Sentret',
        'hp': [180,274],
        'lvl': [1,14],
        'atk': [87,210],
        'speed': [40,152],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['162']
    },
    "162":{
        'name': 'Furret',
        'hp': [280,374],
        'lvl': [15,100],
        'atk': [141,276],
        'speed': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "163":{
        'name': 'Hoothoot',
        'hp': [230,324],
        'lvl': [1,19],
        'atk': [58,174],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['164']
    },
    "164":{
        'name': 'Noctowl',
        'hp': [310,404],
        'lvl': [20,100],
        'atk': [94,218],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "165":{
        'name': 'Ledyba',
        'hp': [190,284],
        'lvl': [1,17],
        'atk': [40,152],
        'speed': [103,229],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug','Flying'],
        'upgrade': ['166']
    },
    "166":{
        'name': 'Ledian',
        'hp': [220,314],
        'lvl': [18,100],
        'atk': [67,185],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Flying'],
        'upgrade': ['']
    },
    "167":{
        'name': 'Spinarak',
        'hp': [190,284],
        'lvl': [1,21],
        'atk': [112,240],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['168']
    },
    "168":{
        'name': 'Ariados',
        'hp': [250,344],
        'lvl': [22,100],
        'atk': [166,306],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['']
    },
    "169":{
        'name': 'Crobat',
        'hp': [280,374],
        'lvl': [22,100],
        'atk': [166,306],
        'speed': [238,394],
        'Catch rate': [45,60,75,100],
        'pktype': ['Poison','Flying'],
        'upgrade': ['']
    },
    "170":{
        'name': 'Chinchou',
        'hp': [260,354],
        'lvl': [1,26],
        'atk': [72,192],
        'speed': [125,256],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Electric'],
        'upgrade': ['171']
    },
    "171":{
        'name': 'Lanturn',
        'hp': [360,454],
        'lvl': [27,100],
        'atk': [108,236],
        'speed': [125,256],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Electric'],
        'upgrade': ['']
    },
    "172":{
        'name': 'Pichu',
        'hp': [150,244],
        'lvl': [1,100],
        'atk': [76,196],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['025']
    },
    "173":{
        'name': 'Cleffa',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [49,163],
        'speed': [31,141],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fairy'],
        'upgrade': ['035']
    },
    "174":{
        'name': 'Igglybuff',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [58,174],
        'speed': [31,141],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fairy'],
        'upgrade': ['039']
    },
    "175":{
        'name': 'Togepi',
        'hp': [180,274],
        'lvl': [1,100],
        'atk': [40,152],
        'speed': [40,152],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fairy'],
        'upgrade': ['176']
    },
    "176":{
        'name': 'Togetic',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [76,196],
        'speed': [76,196],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fairy'],
        'upgrade': ['']
    },
    "177":{
        'name': 'Natu',
        'hp': [190,284],
        'lvl': [1,24],
        'atk': [94,218],
        'speed': [130,262],
        'Catch rate': [75,85,95,100],
        'pktype': ['Psychic','Flying'],
        'upgrade': ['177']
    },
    "178":{
        'name': 'Xatu',
        'hp': [240,334],
        'lvl': [25,100],
        'atk': [139,273],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic','Flying'],
        'upgrade': ['']
    },
    "179":{
        'name': 'Mareep',
        'hp': [220,314],
        'lvl': [1,14],
        'atk': [76,196],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Electric'],
        'upgrade': ['180']
    },
    "180":{
        'name': 'Flaaffy',
        'hp': [250,344],
        'lvl': [15,29],
        'atk': [103,229],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['181']
    },
    "181":{
        'name': 'Ampharos',
        'hp': [290,384],
        'lvl': [30,100],
        'atk': [139,273],
        'speed': [103,229],
        'Catch rate': [45,60,75,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "182":{
        'name': 'Bellossom',
        'hp': [260,354],
        'lvl': [21,100],
        'atk': [148,284],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass'],
        'upgrade': ['']
    },
    "183":{
        'name': 'Marill',
        'hp': [250,344],
        'lvl': [1,17],
        'atk': [40,152],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['184']
    },
    "184":{
        'name': 'Azumarill',
        'hp': [310,404],
        'lvl': [18,100],
        'atk': [94,218],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "185":{
        'name': 'Sudowoodo',
        'hp': [250,344],
        'lvl': [15,100],
        'atk': [184,328],
        'speed': [58,174],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock'],
        'upgrade': ['']
    },
    "186":{
        'name': 'Politoed',
        'hp': [290,384],
        'lvl': [25,100],
        'atk': [139,273],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "187":{
        'name': 'Hoppip',
        'hp': [180,274],
        'lvl': [1,17],
        'atk': [67,185],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass','Flying'],
        'upgrade': ['188']
    },
    "188":{
        'name': 'Skiploom',
        'hp': [220,314],
        'lvl': [18,26],
        'atk': [85,207],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Flying'],
        'upgrade': ['189']
    },
    "189":{
        'name': 'Jumpluff',
        'hp': [260,354],
        'lvl': [27,100],
        'atk': [103,229],
        'speed': [202,350],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass','Flying'],
        'upgrade': ['']
    },
    "190":{
        'name': 'Aipom',
        'hp': [220,314],
        'lvl': [1,31],
        'atk': [130,262],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "191":{
        'name': 'Sunkern',
        'hp': [170,264],
        'lvl': [1,100],
        'atk': [58,174],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass'],
        'upgrade': ['192']
    },
    "192":{
        'name': 'Sunflora',
        'hp': [260,354],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [58,174],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass'],
        'upgrade': ['']
    },
    "193":{
        'name': 'Yanma',
        'hp': [240,334],
        'lvl': [1,32],
        'atk': [121,251],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Flying'],
        'upgrade': ['']
    },
    "194":{
        'name': 'Wooper',
        'hp': [220,314],
        'lvl': [1,19],
        'atk': [58,174],
        'speed': [31,141],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Ground'],
        'upgrade': ['195']
    },
    "195":{
        'name': 'Quagsire',
        'hp': [300,394],
        'lvl': [20,100],
        'atk': [157,295],
        'speed': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Ground'],
        'upgrade': ['']
    },
    "196":{
        'name': 'Espeon',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [121,251],
        'speed': [202,350],
        'Catch rate': [25,40,55,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "197":{
        'name': 'Umbreon',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [121,251],
        'speed': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': ['Dark'],
        'upgrade': ['']
    },
    "198":{
        'name': 'Murkrow',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [168,309],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dark','Flying'],
        'upgrade': ['']
    },
    "199":{
        'name': 'Slowking',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [58,174],
        'Catch rate': [45,60,75,100],
        'pktype': ['Psychic','Water'],
        'upgrade': ['']
    },
    "200":{
        'name': 'Misdreavus',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [112,240],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ghost'],
        'upgrade': ['']
    },
    "201":{
        'name': 'Unown',
        'hp': [206,300],
        'lvl': [1,100],
        'atk': [130,264],
        'speed': [90,214],
        'Catch rate': [25,40,55,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "202":{
        'name': 'Wobbuffet',
        'hp': [490,584],
        'lvl': [15,100],
        'atk': [63,181],
        'speed': [63,181],
        'Catch rate': [45,60,75,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "203":{
        'name': 'Girafarig',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [148,284],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "204":{
        'name': 'Pineco',
        'hp': [210,304],
        'lvl': [1,30],
        'atk': [121,251],
        'speed': [31,141],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug'],
        'upgrade': ['205']
    },
    "205":{
        'name': 'Forretress',
        'hp': [260,354],
        'lvl': [31,100],
        'atk': [166,306],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Steel'],
        'upgrade': ['']
    },
    "206":{
        'name': 'Dunsparce',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [130,262],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground'],
        'upgrade': ['']
    },
    "207":{
        'name': 'Gligar',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground','Flying'],
        'upgrade': ['']
    },
    "208":{
        'name': 'Steelix',
        'hp': [260,354],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [58,174],
        'Catch rate': [25,40,55,100],
        'pktype': ['Steel','Ground'],
        'upgrade': ['']
    },
    "209":{
        'name': 'Snubbull',
        'hp': [230,324],
        'lvl': [1,22],
        'atk': [148,284],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['210']
    },
    "210":{
        'name': 'Granbull',
        'hp': [290,384],
        'lvl': [23,100],
        'atk': [220,372],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "211":{
        'name': 'Qwilfish',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [175,317],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Poison'],
        'upgrade': ['']
    },
    "212":{
        'name': 'Scizor',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [238,394],
        'speed': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': ['Bug','Steel'],
        'upgrade': ['']
    },
    "213":{
        'name': 'Shuckle',
        'hp': [150,244],
        'lvl': [1,100],
        'atk': [22,130],
        'speed': [13,119],
        'Catch rate': [25,40,55,100],
        'pktype': ['Bug','Rock'],
        'upgrade': ['']
    },
    "214":{
        'name': 'Heracross',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [229,383],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Fighting'],
        'upgrade': ['']
    },
    "215":{
        'name': 'Sneasel',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [175,317],
        'speed': [211,361],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dark'],
        'upgrade': ['']
    },
    "216":{
        'name': 'Teddiursa',
        'hp': [230,324],
        'lvl': [1,29],
        'atk': [148,284],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['217']
    },
    "217":{
        'name': 'Ursaring',
        'hp': [290,384],
        'lvl': [30,100],
        'atk': [238,394],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "218":{
        'name': 'Slugma',
        'hp': [190,284],
        'lvl': [1,37],
        'atk': [76,196],
        'speed': [40,152],
        'Catch rate': [75,85,95,100],
        'pktype': ['Fire'],
        'upgrade': ['219']
    },
    "219":{
        'name': 'Magcargo',
        'hp': [230,324],
        'lvl': [38,100],
        'atk': [94,218],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['']
    },
    "220":{
        'name': 'Swinub',
        'hp': [210,304],
        'lvl': [1,32],
        'atk': [94,218],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ice','Ground'],
        'upgrade': ['221']
    },
    "221":{
        'name': 'Piloswine',
        'hp': [310,404],
        'lvl': [33,100],
        'atk': [184,328],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ice','Ground'],
        'upgrade': ['']
    },
    "222":{
        'name': 'Corsola',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [103,229],
        'speed': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Rock'],
        'upgrade': ['']
    },
    "223":{
        'name': 'Remoraid',
        'hp': [180,274],
        'lvl': [1,24],
        'atk': [121,251],
        'speed': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['224']
    },
    "224":{
        'name': 'Octillery',
        'hp': [260,354],
        'lvl': [25,100],
        'atk': [193,339],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "225":{
        'name': 'Delibird',
        'hp': [200,294],
        'lvl': [1,100],
        'atk': [103,229],
        'speed': [139,273],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ice','Flying'],
        'upgrade': ['']
    },
    "226":{
        'name': 'Mantine',
        'hp': [280,374],
        'lvl': [1,100],
        'atk': [76,196],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Flying'],
        'upgrade': ['']
    },
    "227":{
        'name': 'Skarmory',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [148,284],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Steel','Flying'],
        'upgrade': ['']
    },
    "228":{
        'name': 'Houndour',
        'hp': [200,294],
        'lvl': [1,23],
        'atk': [112,240],
        'speed': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': ['Dark','Fire'],
        'upgrade': ['229']
    },
    "229":{
        'name': 'Houndoom',
        'hp': [260,354],
        'lvl': [24,100],
        'atk': [166,306],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dark','Fire'],
        'upgrade': ['']
    },
    "230":{
        'name': 'Kingdra',
        'hp': [260,354],
        'lvl': [32,100],
        'atk': [175,317],
        'speed': [157,295],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Dragon'],
        'upgrade': ['']
    },
    "231":{
        'name': 'Phanpy',
        'hp': [290,384],
        'lvl': [1,24],
        'atk': [112,240],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ground'],
        'upgrade': ['232']
    },
    "232":{
        'name': 'Donphan',
        'hp': [290,384],
        'lvl': [25,100],
        'atk': [220,372],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground'],
        'upgrade': ['']
    },
    "233":{
        'name': 'Porygon2',
        'hp': [280,374],
        'lvl': [1,100],
        'atk': [148,284],
        'speed': [112,240],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "234":{
        'name': 'Stantler',
        'hp': [256,350],
        'lvl': [1,100],
        'atk': [175,317],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "235":{
        'name': 'Smeargle',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [40,152],
        'speed': [139,273],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "236":{
        'name': 'Tyrogue',
        'hp': [180,274],
        'lvl': [1,19],
        'atk': [67,185],
        'speed': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fighting'],
        'upgrade': ['106','107','237']
    },
    "237":{
        'name': 'Hitmontop',
        'hp': [210,304],
        'lvl': [20,100],
        'atk': [175,317],
        'speed': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fighting'],
        'upgrade': ['']
    },
    "238":{
        'name': 'Smoochum',
        'hp': [200,294],
        'lvl': [1,29],
        'atk': [58,174],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': ['124']
    },
    "239":{
        'name': 'Elekid',
        'hp': [200,294],
        'lvl': [1,29],
        'atk': [117,247],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['125']
    },
    "240":{
        'name': 'Magby',
        'hp': [200,294],
        'lvl': [1,29],
        'atk': [139,273],
        'speed': [153,291],
        'Catch rate': [25,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['126']
    },
    "241":{
        'name': 'Miltank',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [148,284],
        'speed': [184,328],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "242":{
        'name': 'Blissey',
        'hp': [620,714],
        'lvl': [1,100],
        'atk': [22,130],
        'speed': [103,229],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "243":{
        'name': 'Raikou',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [211,361],
        'Catch rate': [5,20,35,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "244":{
        'name': 'Entei',
        'hp': [340,434],
        'lvl': [1,100],
        'atk': [211,361],
        'speed': [184,328],
        'Catch rate': [5,20,35,100],
        'pktype': ['Ice','Flying'],
        'upgrade': ['']
    },
    "245":{
        'name': 'Suicune',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [157,295],
        'Catch rate': [5,20,35,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    '246':{
        'name': 'Larvitar',
        'hp': [210,304],
        'lvl': [1,29],
        'atk': [119,249],
        'speed': [78,199],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock','Ground'],
        'upgrade': ['247']
    },
    '247':{
        'name': 'Pupitar',
        'hp': [250,344],
        'lvl': [30,54],
        'atk': [155,293],
        'speed': [96,221],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock','Ground'],
        'upgrade': ['248']
    },
    '248':{
        'name': 'Tyranitar',
        'hp': [310,404],
        'lvl': [55,100],
        'atk': [245,403],
        'speed': [114,243],
        'Catch rate': [25,40,55,100],
        'pktype': ['Rock','Dark'],
        'upgrade': ['']
    },
    "249":{
        'name': 'Lugia',
        'hp': [322,416],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [202,350],
        'Catch rate': [5,20,35,100],
        'pktype': ['Psychic','Water'],
        'upgrade': ['']
    },
    "250":{
        'name': 'Ho-oh',
        'hp': [322,416],
        'lvl': [1,100],
        'atk': [238,394],
        'speed': [166,306],
        'Catch rate': [5,20,35,100],
        'pktype': ['Fire','Flying'],
        'upgrade': ['']
    },
    "251":{
        'name': 'Celebi',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [184,328],
        'Catch rate': [5,20,35,100],
        'pktype': ['Psychic','Grass'],
        'upgrade': ['']
    },
    "252":{
        'name': 'Treecko',
        'hp': [190,284],
        'lvl': [1,15],
        'atk': [85,207],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass'],
        'upgrade': ['253']
    },
    '253':{
        'name': 'Grovyle',
        'hp': [210,304],
        'lvl': [16,35],
        'atk': [121,251],
        'speed': [175,317],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass'],
        'upgrade': ['254']
    },
    '254':{
        'name': 'Sceptile',
        'hp': [250,344],
        'lvl': [36,100],
        'atk': [157,295],
        'speed': [220,372],
        'Catch rate': [25,40,55,100],
        'pktype': ['Grass'],
        'upgrade': ['']
    },
    "255":{
        'name': 'Torchic',
        'hp': [200,294],
        'lvl': [1,15],
        'atk': [112,240],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['256']
    },
    "256":{
        'name': 'Combusken',
        'hp': [230,324],
        'lvl': [16,35],
        'atk': [157,295],
        'speed': [103,229],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fire','Fighting'],
        'upgrade': ['257']
    },
    "257":{
        'name': 'Blaziken',
        'hp': [270,364],
        'lvl': [36,100],
        'atk': [220,372],
        'speed': [148,284],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire','Fighting'],
        'upgrade': ['']
    },
    "258":{
        'name': 'Mudkip',
        'hp': [210,304],
        'lvl': [1,15],
        'atk': [130,262],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['259']
    },
    "259":{
        'name': 'Marshtomp',
        'hp': [250,344],
        'lvl': [16,35],
        'atk': [157,295],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Ground'],
        'upgrade': ['260']
    },
    "260":{
        'name': 'Swampert',
        'hp': [310,404],
        'lvl': [36,100],
        'atk': [202,350],
        'speed': [112,240],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Ground'],
        'upgrade': ['']
    },
    "261":{
        'name': 'Poochyena',
        'hp': [180,274],
        'lvl': [1,17],
        'atk': [103,229],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Dark'],
        'upgrade': ['262']
    },
    "262":{
        'name': 'Mightyena',
        'hp': [250,344],
        'lvl': [18,100],
        'atk': [166,306],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dark'],
        'upgrade': ['']
    },
    "263":{
        'name': 'Zigzagoon',
        'hp': [186,280],
        'lvl': [1,19],
        'atk': [58,174],
        'speed': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['264']
    },
    "264":{
        'name': 'Linoone',
        'hp': [266,360],
        'lvl': [20,100],
        'atk': [130,262],
        'speed': [184,328],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "265":{
        'name': 'Wurmple',
        'hp': [200,294],
        'lvl': [1,6],
        'atk': [85,207],
        'speed': [40,152],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug'],
        'upgrade': ['266','268']
    },
    "266":{
        'name': 'Silcoon',
        'hp': [210,304],
        'lvl': [7,9],
        'atk': [67,185],
        'speed': [31,141],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug'],
        'upgrade': ['267']
    },
    "267":{
        'name': 'Beautifly',
        'hp': [230,324],
        'lvl': [10,100],
        'atk': [130,262],
        'speed': [121,251],
        'Catch rate': [45,60,75,100],
        'pktype': ['Bug','Flying'],
        'upgrade': ['']
    },
    "268":{
        'name': 'Cascoon',
        'hp': [210,304],
        'lvl': [7,9],
        'atk': [67,185],
        'speed': [31,141],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug'],
        'upgrade': ['269']
    },
    "269":{
        'name': 'Dustox',
        'hp': [230,324],
        'lvl': [10,100],
        'atk': [94,218],
        'speed': [121,251],
        'Catch rate': [45,60,75,100],
        'pktype': ['Bug','Poison'],
        'upgrade': ['']
    },
    "270":{
        'name': 'Lotad',
        'hp': [190,284],
        'lvl': [1,13],
        'atk': [58,174],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Grass'],
        'upgrade': ['271']
    },
    "271":{
        'name': 'Lombre',
        'hp': [230,324],
        'lvl': [14,100],
        'atk': [94,218],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Grass'],
        'upgrade': ['272']
    },
    "272":{
        'name': 'Ludicolo',
        'hp': [270,364],
        'lvl': [14,100],
        'atk': [130,262],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Grass'],
        'upgrade': ['']
    },
    "273":{
        'name': 'Seedot',
        'hp': [190,284],
        'lvl': [1,13],
        'atk': [76,196],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass'],
        'upgrade': ['274']
    },
    "274":{
        'name': 'Nuzleaf',
        'hp': [250,344],
        'lvl': [14,100],
        'atk': [94,218],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dark','Grass'],
        'upgrade': ['275']
    },
    "275":{
        'name': 'Shiftry',
        'hp': [290,384],
        'lvl': [14,100],
        'atk': [184,328],
        'speed': [148,284],
        'Catch rate': [25,40,55,100],
        'pktype': ['Dark','Grass'],
        'upgrade': ['']
    },
    "276":{
        'name': 'Taillow',
        'hp': [190,284],
        'lvl': [1,21],
        'atk': [103,229],
        'speed': [157,295],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['277']
    },
    "277":{
        'name': 'Swellow',
        'hp': [230,324],
        'lvl': [22,100],
        'atk': [157,295],
        'speed': [229,383],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "278":{
        'name': 'Wingull',
        'hp': [190,284],
        'lvl': [1,24],
        'atk': [58,174],
        'speed': [157,295],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Flying'],
        'upgrade': ['279']
    },
    "279":{
        'name': 'Pelipper',
        'hp': [230,324],
        'lvl': [25,100],
        'atk': [94,218],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Flying'],
        'upgrade': [''] 
    },
    "280":{
        'name': 'Ralts',
        'hp': [166,260],
        'lvl': [1,19],
        'atk': [76,196],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': ['281']
    },
    "281":{
        'name': 'Kirlia',
        'hp': [186,280],
        'lvl': [20,29],
        'atk': [67,185],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Psychic'],
        'upgrade': ['282']
    },
    "282":{
        'name': 'Gardevoir',
        'hp': [246,340],
        'lvl': [30,100],
        'atk': [121,251],
        'speed': [148,284],
        'Catch rate': [25,40,55,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    "283":{
        'name': 'Surskit',
        'hp': [190,284],
        'lvl': [1,21],
        'atk': [58,174],
        'speed': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Bug'],
        'upgrade': ['284']
    },
    "284":{
        'name': 'Masquerain',
        'hp': [250,344],
        'lvl': [22,100],
        'atk': [112,240],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Flying'],
        'upgrade': [''] 
    },
    "285":{
        'name': 'Shroomish',
        'hp': [230,324],
        'lvl': [1,22],
        'atk': [76,196],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['286']
    },
    "286":{
        'name': 'Breloom',
        'hp': [230,324],
        'lvl': [23,100],
        'atk': [238,394],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Fighting'],
        'upgrade': [''] 
    },
    "287":{
        'name': 'Slakoth',
        'hp': [230,324],
        'lvl': [1,17],
        'atk': [112,240],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['288']
    },
    "288":{
        'name': 'Vigoroth',
        'hp': [270,364],
        'lvl': [18,35],
        'atk': [148,284],
        'speed': [166,306],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal'],
        'upgrade': ['289']
    },
    "289":{
        'name': 'Slaking',
        'hp': [410,504],
        'lvl': [36,100],
        'atk': [292,460],
        'speed': [184,328],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "290":{
        'name': 'Nincada',
        'hp': [172,266],
        'lvl': [1,19],
        'atk': [85,207],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug','Ground'],
        'upgrade': ['291','292']
    },
    "291":{
        'name': 'Ninjask',
        'hp': [232,326],
        'lvl': [20,100],
        'atk': [166,306],
        'speed': [292,460],
        'Catch rate': [45,60,75,100],
        'pktype': ['Bug','Flying'],
        'upgrade': [''] 
    },
    "292":{
        'name': 'Shedinja',
        'hp': [1,1],
        'lvl': [20,100],
        'atk': [166,306],
        'speed': [76,196],
        'Catch rate': [45,60,75,100],
        'pktype': ['Bug','Ghost'],
        'upgrade': [''] 
    },
    "293":{
        'name': 'Whismur',
        'hp': [238,332],
        'lvl': [1,19],
        'atk': [96,221],
        'speed': [54,170],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['294']
    },
    "294":{
        'name': 'Loudred',
        'hp': [278,372],
        'lvl': [20,39],
        'atk': [132,265],
        'speed': [90,214],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal'],
        'upgrade': ['295']
    },
    "295":{
        'name': 'Exploud',
        'hp': [318,412],
        'lvl': [40,100],
        'atk': [168,309],
        'speed': [126,258],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "296":{
        'name': 'Makuhita',
        'hp': [254,348],
        'lvl': [1,23],
        'atk': [112,240],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Fighting'],
        'upgrade': ['297']
    },
    "297":{
        'name': 'Hariyama',
        'hp': [398,492],
        'lvl': [24,100],
        'atk': [220,372],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fighting'],
        'upgrade': [''] 
    },
    "298":{
        'name': 'Azurill',
        'hp': [210,304],
        'lvl': [1,18],
        'atk': [40,152],
        'speed': [40,152],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['183']
    },
    "299":{
        'name': 'Nosepass',
        'hp': [170,264],
        'lvl': [1,100],
        'atk': [85,207],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock'],
        'upgrade': ['']
    },
    "300":{
        'name': 'Skitty',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [85,207],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['301']
    },
    "301":{
        'name': 'Delcatty',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [121,251],
        'speed': [166,306],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal'],
        'upgrade': [''] 
    },
    "302":{
        'name': 'Sableye',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [94,218],
        'Catch rate': [25,40,55,100],
        'pktype': ['Dark','Ghost'],
        'upgrade': ['']
    },
    "303":{
        'name': 'Mawile',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Steel','Fairy'],
        'upgrade': ['']
    },
    "304":{
        'name': 'Aron',
        'hp': [210,304],
        'lvl': [1,31],
        'atk': [130,263],
        'speed': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': ['Steel','Ground'],
        'upgrade': ['305']
    },
    "305":{
        'name': 'Lairon',
        'hp': [230,324],
        'lvl': [32,41],
        'atk': [166,306],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Steel','Ground'],
        'upgrade': ['306']
    },
    "306":{
        'name': 'Aggron',
        'hp': [250,344],
        'lvl': [42,100],
        'atk': [202,350],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Steel','Ground'],
        'upgrade': ['']
    },
    "307":{
        'name': 'Meditite',
        'hp': [170,264],
        'lvl': [1,36],
        'atk': [76,196],
        'speed': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': ['Fighting','Psychic'],
        'upgrade': ['308']
    },
    "308":{
        'name': 'Medicham',
        'hp': [230,324],
        'lvl': [37,100],
        'atk': [112,240],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fighting','Psychic'],
        'upgrade': ['']
    },
    "309":{
        'name': 'Electrike',
        'hp': [190,284],
        'lvl': [1,25],
        'atk': [85,207],
        'speed': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': ['Electric'],
        'upgrade': ['310']
    },
    "310":{
        'name': 'Manectric',
        'hp': [250,344],
        'lvl': [26,100],
        'atk': [139,273],
        'speed': [193,339],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': [''] 
    },
    "311":{
        'name': 'Plusle',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [94,218],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "312":{
        'name': 'Minun',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [76,196],
        'speed': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': [''] 
    },
    "313":{
        'name': 'Volbeat',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [135,269],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug'],
        'upgrade': ['']
    },
    "314":{
        'name': 'Illumise',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [89,212],
        'speed': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug'],
        'upgrade': [''] 
    },
    "315":{
        'name': 'Roselia',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [112,240],
        'speed': [121,251],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['407'] 
    },
    "316":{
        'name': 'Gulpin',
        'hp': [250,344],
        'lvl': [1,25],
        'atk': [81,203],
        'speed': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': ['Poison'],
        'upgrade': ['317']
    },
    "317":{
        'name': 'Swalot',
        'hp': [310,404],
        'lvl': [26,100],
        'atk': [135,269],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Poison'],
        'upgrade': [''] 
    },
    "318":{
        'name': 'Carvanha',
        'hp': [200,294],
        'lvl': [1,29],
        'atk': [166,306],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Dark'],
        'upgrade': ['319']
    },
    "319":{
        'name': 'Sharpedo',
        'hp': [250,344],
        'lvl': [30,100],
        'atk': [220,372],
        'speed': [175,317],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Dark'],
        'upgrade': [''] 
    },
    "320":{
        'name': 'Wailmer',
        'hp': [370,464],
        'lvl': [1,39],
        'atk': [130,262],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['321']
    },
    "321":{
        'name': 'Wailord',
        'hp': [450,544],
        'lvl': [40,100],
        'atk': [166,306],
        'speed': [112,240],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water'],
        'upgrade': [''] 
    },
    "322":{
        'name': 'Numel',
        'hp': [230,324],
        'lvl': [1,32],
        'atk': [112,240],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Fire','Ground'],
        'upgrade': ['323']
    },
    "323":{
        'name': 'Camerupt',
        'hp': [250,344],
        'lvl': [33,100],
        'atk': [184,328],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire','Ground'],
        'upgrade': [''] 
    },
    "324":{
        'name': 'Torkoal',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [157,295],
        'speed': [40,152],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire'],
        'upgrade': [''] 
    },
    "325":{
        'name': 'Spoink',
        'hp': [230,324],
        'lvl': [1,31],
        'atk': [49,163],
        'speed': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': ['Psychic'],
        'upgrade': ['326']
    },
    "326":{
        'name': 'Grumpig',
        'hp': [270,364],
        'lvl': [32,100],
        'atk': [85,207],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': [''] 
    },
    "327":{
        'name': 'Spinda',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [112,240],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': [''] 
    },
    "328":{
        'name': 'Trapinch',
        'hp': [200,294],
        'lvl': [1,34],
        'atk': [184,328],
        'speed': [22,130],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ground'],
        'upgrade': ['329']
    },
    "329":{
        'name': 'Vibrava',
        'hp': [210,304],
        'lvl': [35,44],
        'atk': [130,262],
        'speed': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dragon','Ground'],
        'upgrade': ['330']
    },
    "330":{
        'name': 'Flygon',
        'hp': [270,364],
        'lvl': [45,100],
        'atk': [184,328],
        'speed': [184,328],
        'Catch rate': [45,60,75,100],
        'pktype': ['Dragon','Ground'],
        'upgrade': ['']
    },
    "331":{
        'name': 'Cacnea',
        'hp': [210,304],
        'lvl': [1,31],
        'atk': [157,295],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Grass'],
        'upgrade': ['332']
    },
    "332":{
        'name': 'Cacturne',
        'hp': [250,344],
        'lvl': [32,100],
        'atk': [211,361],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Dark'],
        'upgrade': [''] 
    },
    "333":{
        'name': 'Swablu',
        'hp': [200,294],
        'lvl': [1,34],
        'atk': [76,196],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['334']
    },
    "334":{
        'name': 'Altaria',
        'hp': [260,354],
        'lvl': [35,100],
        'atk': [130,262],
        'speed': [148,284],
        'Catch rate': [45,60,75,100],
        'pktype': ['Dragon','Flying'],
        'upgrade': [''] 
    },
    "335":{
        'name': 'Zangoose',
        'hp': [256,350],
        'lvl': [1,100],
        'atk': [211,361],
        'speed': [166,306],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': ['']
    },
    "336":{
        'name': 'Seviper',
        'hp': [256,350],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': ['Poison'],
        'upgrade': ['']
    },
    "337":{
        'name': 'Lunatone',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [103,229],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Rock','Psychic'],
        'upgrade': ['']
    },
    "338":{
        'name': 'Solrock',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [175,317],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Rock','Psychic'],
        'upgrade': ['']
    },
    "339":{
        'name': 'Barboach',
        'hp': [210,304],
        'lvl': [1,29],
        'atk': [90,214],
        'speed': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water','Ground'],
        'upgrade': ['340']
    },
    "340":{
        'name': 'Whiscash',
        'hp': [330,424],
        'lvl': [30,100],
        'atk': [144,280],
        'speed': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Ground'],
        'upgrade': [''] 
    },
    "341":{
        'name': 'Corphish',
        'hp': [196,290],
        'lvl': [1,29],
        'atk': [148,284],
        'speed': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': ['Water'],
        'upgrade': ['342']
    },
    "342":{
        'name': 'Crawdaunt',
        'hp': [236,330],
        'lvl': [30,100],
        'atk': [220,372],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Dark'],
        'upgrade': [''] 
    },
    "343":{
        'name': 'Baltoy',
        'hp': [190,284],
        'lvl': [1,35],
        'atk': [76,196],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ground','Psychic'],
        'upgrade': ['344']
    },
    "344":{
        'name': 'Claydol',
        'hp': [230,324],
        'lvl': [36,100],
        'atk': [130,262],
        'speed': [139,273],
        'Catch rate': [45,60,75,100],
        'pktype': ['Ground','Psychic'],
        'upgrade': [''] 
    },
    "345":{
        'name': 'Lileep',
        'hp': [242,336],
        'lvl': [1,39],
        'atk': [78,199],
        'speed': [45,159],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock','Grass'],
        'upgrade': ['346']
    },
    "346":{
        'name': 'Cradily',
        'hp': [282,376],
        'lvl': [40,100],
        'atk': [150,287],
        'speed': [81,203],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock','Grass'],
        'upgrade': [''] 
    },
    "347":{
        'name': 'Anorith',
        'hp': [200,294],
        'lvl': [1,39],
        'atk': [175,317],
        'speed': [139,273],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock','Bug'],
        'upgrade': ['348']
    },
    "348":{
        'name': 'Armaldo',
        'hp': [260,354],
        'lvl': [40,100],
        'atk': [229,383],
        'speed': [85,207],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock','Bug'],
        'upgrade': [''] 
    },
    "349":{
        'name': 'Feebas',
        'hp': [150,244],
        'lvl': [1,100],
        'atk': [31,141],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['350']
    },
    "350":{
        'name': 'Milotic',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [112,240],
        'speed': [150,287],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': [''] 
    },
    "351":{
        'name': 'Castform',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [130,262],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': [''] 
    },
    "352":{
        'name': 'Kecleon',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [76,196],
        'Catch rate': [25,40,55,100],
        'pktype': ['Normal'],
        'upgrade': [''] 
    },
    "353":{
        'name': 'Shuppet',
        'hp': [198,292],
        'lvl': [1,36],
        'atk': [139,273],
        'speed': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ghost'],
        'upgrade': ['354']
    },
    "354":{
        'name': 'Banette',
        'hp': [238,332],
        'lvl': [37,100],
        'atk': [211,361],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ghost'],
        'upgrade': [''] 
    },
    "355":{
        'name': 'Duskull',
        'hp': [150,244],
        'lvl': [1,36],
        'atk': [76,196],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ghost'],
        'upgrade': ['356']
    },
    "356":{
        'name': 'Dusclops',
        'hp': [190,284],
        'lvl': [37,100],
        'atk': [130,262],
        'speed': [49,163],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ghost'],
        'upgrade': [''] 
    },
    "357":{
        'name': 'Tropius',
        'hp': [308,402],
        'lvl': [1,100],
        'atk': [126,258],
        'speed': [96,221],
        'Catch rate': [25,40,55,100],
        'pktype': ['Grass','Flying'],
        'upgrade': [''] 
    },
    "358":{
        'name': 'Chimecho',
        'hp': [260,354],
        'lvl': [1,100],
        'atk': [94,218],
        'speed': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': ['Psychic'],
        'upgrade': [''] 
    },
    "359":{
        'name': 'Absol',
        'hp': [240,334],
        'lvl': [1,100],
        'atk': [238,394],
        'speed': [139,273],
        'Catch rate': [25,40,55,100],
        'pktype': ['Dark'],
        'upgrade': [''] 
    },
    "360":{
        'name': 'Wynaut',
        'hp': [300,394],
        'lvl': [1,14],
        'atk': [45,159],
        'speed': [45,159],
        'Catch rate': [65,80,90,100],
        'pktype': ['Psychic'],
        'upgrade': ['202'] 
    },
    "361":{
        'name': 'Snorunt',
        'hp': [210,304],
        'lvl': [1,41],
        'atk': [94,218],
        'speed': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ice'],
        'upgrade': ['362']
    },
    "362":{
        'name': 'Dusclops',
        'hp': [270,364],
        'lvl': [42,100],
        'atk': [148,284],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ice'],
        'upgrade': [''] 
    },
    "363":{
        'name': 'Spheal',
        'hp': [250,344],
        'lvl': [1,31],
        'atk': [76,196],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Ice','Water'],
        'upgrade': ['364']
    },
    "364":{
        'name': 'Sealeo',
        'hp': [290,384],
        'lvl': [32,43],
        'atk': [112,240],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Ice','Water'],
        'upgrade': ['365']
    },
    "365":{
        'name': 'Walrein',
        'hp': [330,424],
        'lvl': [44,100],
        'atk': [148,284],
        'speed': [121,251],
        'Catch rate': [45,60,75,100],
        'pktype': ['Ice','Water'],
        'upgrade': ['']
    },
    "366":{
        'name': 'Clamperl',
        'hp': [180,274],
        'lvl': [1,100],
        'atk': [119,249],
        'speed': [62,179],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': ['367','368']
    },
    "367":{
        'name': 'Huntail',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [191,337],
        'speed': [98,223],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': [''] 
    },
    "368":{
        'name': 'Gorebyss',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [155,293],
        'speed': [98,223],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water'],
        'upgrade': [''] 
    },
    "369":{
        'name': 'Relicanth',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [103,229],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Rock'],
        'upgrade': [''] 
    },
    "370":{
        'name': 'Luvdisc',
        'hp': [196,290],
        'lvl': [1,100],
        'atk': [58,174],
        'speed': [179,322],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water'],
        'upgrade': [''] 
    },
    "371":{
        'name': 'Bagon',
        'hp': [200,294],
        'lvl': [1,29],
        'atk': [139,273],
        'speed': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': ['Dragon'],
        'upgrade': ['372']
    },
    "372":{
        'name': 'Shelgon',
        'hp': [240,334],
        'lvl': [30,49],
        'atk': [175,317],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Dragon'],
        'upgrade': ['373']
    },
    "373":{
        'name': 'Salamence',
        'hp': [300,394],
        'lvl': [50,100],
        'atk': [247,405],
        'speed': [184,328],
        'Catch rate': [25,40,55,100],
        'pktype': ['Dragon','Flying'],
        'upgrade': ['']
    },
    "374":{
        'name': 'Beldum',
        'hp': [190,284],
        'lvl': [1,19],
        'atk': [103,229],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Steel','Psychic'],
        'upgrade': ['375']
    },
    "375":{
        'name': 'Metang',
        'hp': [230,324],
        'lvl': [20,44],
        'atk': [139,273],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Steel','Psychic'],
        'upgrade': ['376']
    },
    "376":{
        'name': 'Metagross',
        'hp': [270,364],
        'lvl': [45,100],
        'atk': [247,405],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Steel','Psychic'],
        'upgrade': ['']
    },
    "377":{
        'name': 'Regirock',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [94,218],
        'Catch rate': [5,20,35,100],
        'pktype': ['Rock'],
        'upgrade': ['']
    },
    "378":{
        'name': 'Regice',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [94,218],
        'speed': [94,218],
        'Catch rate': [5,20,35,100],
        'pktype': ['Rock'],
        'upgrade': ['']
    },
    "379":{
        'name': 'Registeel',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [139,273],
        'speed': [94,218],
        'Catch rate': [5,20,35,100],
        'pktype': ['Rock'],
        'upgrade': ['']
    },
    "380":{
        'name': 'Latias',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [148,284],
        'speed': [202,350],
        'Catch rate': [5,20,35,100],
        'pktype': ['Dragon','Psychic'],
        'upgrade': ['']
    },
    "381":{
        'name': 'Latios',
        'hp': [270,364],
        'lvl': [1,100],
        'atk': [166,306],
        'speed': [202,350],
        'Catch rate': [5,20,35,100],
        'pktype': ['Dragon','Psychic'],
        'upgrade': ['']
    },
    "382":{
        'name': 'Kyogre',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [166,306],
        'Catch rate': [5,20,35,100],
        'pktype': ['Water'],
        'upgrade': ['']
    },
    "383":{
        'name': 'Groudon',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [274,438],
        'speed': [166,306],
        'Catch rate': [5,20,35,100],
        'pktype': ['Ground'],
        'upgrade': ['']
    },
    "384":{
        'name': 'Rayquaza',
        'hp': [320,414],
        'lvl': [1,100],
        'atk': [274,438],
        'speed': [175,317],
        'Catch rate': [5,20,35,100],
        'pktype': ['Dragon','Flying'],
        'upgrade': ['']
    },
    "385":{
        'name': 'Jirachi',
        'hp': [310,404],
        'lvl': [1,100],
        'atk': [184,328],
        'speed': [184,328],
        'Catch rate': [5,20,35,100],
        'pktype': ['Psychic','Steel'],
        'upgrade': ['']
    },
    "386":{
        'name': 'Deoxys',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [274,438],
        'speed': [274,438],
        'Catch rate': [5,20,35,100],
        'pktype': ['Psychic'],
        'upgrade': ['']
    },
    '387':{
        'name': 'Turtwig',
        'hp': [220,314],
        'lvl': [1,17],
        'atk': [126,258],
        'speed': [60,177],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass'],
        'upgrade': ['388']
    },
    '388':{
        'name': 'Grotle',
        'hp': [260,354],
        'lvl': [18,31],
        'atk': [164,304],
        'speed': [69,188],
        'Catch rate': [45,60,75,100],
        'pktype': ['Grass'],
        'upgrade': ['389']
    },
    '389':{
        'name': 'Torterra',
        'hp': [300,394],
        'lvl': [32,100],
        'atk': [200,348],
        'speed': [105,232],
        'Catch rate': [25,40,55,100],
        'pktype': ['Grass','Ground'],
        'upgrade': ['']
    },
    '390':{
        'name': 'Chimchar',
        'hp': [198,292],
        'lvl': [1,13],
        'atk': [108,236],
        'speed': [114,243],
        'Catch rate': [65,80,90,100],
        'pktype': ['Fire'],
        'upgrade': ['391']
    },
    "391":{
        'name': 'Monferno',
        'hp': [238,332],
        'lvl': [14,35],
        'atk': [144,280],
        'speed': [150,287],
        'Catch rate': [45,60,75,100],
        'pktype': ['Fire','Fighting'],
        'upgrade': ['392']
    },
    "392":{
        'name': 'Infernape',
        'hp': [262,356],
        'lvl': [36,100],
        'atk': [191,337],
        'speed': [198,346],
        'Catch rate': [25,40,55,100],
        'pktype': ['Fire','Fighting'],
        'upgrade': ['']
    },
    "393":{
        'name': 'Piplup',
        'hp': [216,310],
        'lvl': [1,15],
        'atk': [96,221],
        'speed': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': ['Water','Ice'],
        'upgrade': ['394']
    },
    "394":{
        'name': 'Prinplup',
        'hp': [238,332],
        'lvl': [16,35],
        'atk': [123,254],
        'speed': [94,218],
        'Catch rate': [45,60,75,100],
        'pktype': ['Water','Ice'],
        'upgrade': ['395']
    },
    '395':{
        'name': 'Empoleon',
        'hp': [278,372],
        'lvl': [36,100],
        'atk': [159,298],
        'speed': [112,240],
        'Catch rate': [25,40,55,100],
        'pktype': ['Water','Steel'],
        'upgrade': ['']
    },
    "396":{
        'name': 'Starly',
        'hp': [190,284],
        'lvl': [1,13],
        'atk': [103,229],
        'speed': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['397']
    },
    "397":{
        'name': 'Staravia',
        'hp': [220,314],
        'lvl': [14,33],
        'atk': [139,273],
        'speed': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['398']
    },
    "398":{
        'name': 'Staraptor',
        'hp': [280,374],
        'lvl': [34,100],
        'atk': [220,372],
        'speed': [184,328],
        'Catch rate': [45,60,75,100],
        'pktype': ['Normal','Flying'],
        'upgrade': ['']
    },
    "399":{
        'name': 'Bidoof',
        'hp': [228,322],
        'lvl': [1,14],
        'atk': [85,207],
        'speed': [60,177],
        'Catch rate': [75,85,95,100],
        'pktype': ['Normal'],
        'upgrade': ['400']
    },
    "400":{
        'name': 'Furret',
        'hp': [268,362],
        'lvl': [15,100],
        'atk': [157,295],
        'speed': [132,265],
        'Catch rate': [65,80,90,100],
        'pktype': ['Normal','Water'],
        'upgrade': ['']
    },
    "401":{
        'name': 'Kricketot',
        'hp': [184,278],
        'lvl': [1,6],
        'atk': [49,163],
        'speed': [49,163],
        'Catch rate': [75,85,95,100],
        'pktype': ['Bug'],
        'upgrade': ['402']
    },
    "402":{
        'name': 'Kricketune',
        'hp': [264,358],
        'lvl': [7,9],
        'atk': [157,295],
        'speed': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': ['Bug'],
        'upgrade': ['']
    },
    "403":{
        'name': 'Shinx',
        'hp': [200,294],
        'lvl': [1,14],
        'atk': [121,251],
        'speed': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': ['Electric'],
        'upgrade': ['404']
    },
    "404":{
        'name': 'Luxio',
        'hp': [230,324],
        'lvl': [15,29],
        'atk': [157,295],
        'speed': [112,240],
        'Catch rate': [45,60,75,100],
        'pktype': ['Electric'],
        'upgrade': ['405']
    },
    "405":{
        'name': 'Luxray',
        'hp': [270,364],
        'lvl': [30,100],
        'atk': [220,372],
        'speed': [130,262],
        'Catch rate': [25,40,55,100],
        'pktype': ['Electric'],
        'upgrade': ['']
    },
    "406":{
        'name': 'Budew',
        'hp': [190,284],
        'lvl': [1,100],
        'atk': [58,174],
        'speed': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['315']
    },
    '407':{
        'name': 'Roserade',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [130,262],
        'speed': [166,306],
        'Catch rate': [25,40,55,100],
        'pktype': ['Grass','Poison'],
        'upgrade': ['']
    },
    "408":{
        'name': 'Cranidos',
        'hp': [244,338],
        'lvl': [1,29],
        'atk': [229,383],
        'speed': [108,236],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock'],
        'upgrade': ['409']
    },
    "409":{
        'name': 'Rampardos',
        'hp': [304,398],
        'lvl': [30,100],
        'atk': [308,471],
        'speed': [108,236],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock'],
        'upgrade': [''] 
    },
    "410":{
        'name': 'Shieldon',
        'hp': [170,264],
        'lvl': [1,29],
        'atk': [80,201],
        'speed': [58,174],
        'Catch rate': [65,80,90,100],
        'pktype': ['Rock'],
        'upgrade': ['411']
    },
    "411":{
        'name': 'Bastiodon',
        'hp': [230,324],
        'lvl': [30,100],
        'atk': [98,223],
        'speed': [58,174],
        'Catch rate': [45,60,75,100],
        'pktype': ['Rock'],
        'upgrade': [''] 
    }
}

class Pokemon():
    id = ''
    name = ''
    hp = 0
    lvl = 0
    atk = 0
    catchrate = []
    pktype = []
    upgrade = ''
    speed = 0
    xp = 0

    def getPhoto(self):
        file_name = f"{config.run_path}/images/{self.id}.jpg"
        return file_name

    def __init__(self,id:str,lvl:int):
        self.id = id
        self.name = pokemon[id]['name']
        self.lvl = lvl
        maxhp = random.randint(pokemon[id]['hp'][0],pokemon[id]['hp'][1])
        lvlnum = pokemon[id]['lvl'][1] - pokemon[id]['lvl'][0]
        hpperlvl = int(maxhp / lvlnum)
        self.hp = hpperlvl * self.lvl
        maxatk = random.randint(pokemon[id]['atk'][0],pokemon[id]['atk'][1])
        atkperlvl = int(maxatk / lvlnum)
        self.atk = atkperlvl * self.lvl
        maxspeed = random.randint(pokemon[id]['speed'][0],pokemon[id]['speed'][1])
        spdperlvl = int(maxspeed / lvlnum)
        self.speed = spdperlvl * self.lvl
        self.catchrate = pokemon[id]['Catch rate']
        self.pktype = pokemon[id]['pktype']
        self.upgrade = random.choice(pokemon[id]['upgrade'])
        self.xp = (self.lvl-1) * 1000
    
    @classmethod
    def init(self,id:str,name:str,lvl:int,hp:int,atk:int,catchrate:list,pktype:str,upgrade:str,speed:int,xp:int):
        p = Pokemon(id,lvl)
        p.hp = hp
        p.atk = atk
        p.catchrate = catchrate
        p.pktype = pktype
        p.upgrade = upgrade
        p.speed = speed
        return p
    
    @classmethod
    def init_from_dict(self,pdict):
        p = Pokemon(pdict['id'],pdict['lvl'])
        p.hp = pdict['hp']
        p.atk = pdict['atk']
        p.catchrate = pdict['catchrate']
        p.pktype = pdict['pktype']
        p.upgrade = pdict['upgrade']
        p.speed = pdict['speed']
        p.xp = pdict['xp']
        return p

    def __str__(self):
        return str(self.__dict__)