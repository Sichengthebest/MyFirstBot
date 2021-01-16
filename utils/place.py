from random import sample
import random
from telegram import InputMediaPhoto
import config

       
rarity = {
    'c':['010','013','016','019','021','023','027','029','032','041','043','046','048','050','052','054','056','060','063','066','069','074','079','081','086','088','090','092','096','098','100','102','104','109','111','116','118','120','129','137'],
    'u':['001','004','007','011','014','017','020','022','024','025','028','030','033','035','037','039','042','044','047','049','051','053','055','057','058','061','064','067','070','072','075','077','080','082','084','087','089','091','093','097','099','101','105','110','112','114','117','119','121','123','125','126','133','138','140','147'],
    'r':['002','005','008','012','015','018','026','031','034','036','040','045','059','062','071','073','078','085','095','103','106','107','108','113','122','124','139','141','148'],
    's':['003','006','009','038','065','068','076','083','094','115','127','128','130','131','132','134','135','136','142','143','149'],
    'l':['144','145','146','150','151']
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
    elif rarityroll > 950 and rarityroll <= 991:
        pokemons = rarity['s']
        rarityy = 's'
    elif rarityroll > 991 and rarityroll <= 1000:
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
        'Catch rate': [65,80,90,100],
        'pktype': 'Grass',
        'upgrade': '002'
    },
    '002':{
        'name': 'Ivysaur',
        'hp': [230,324],
        'lvl': [16,31],
        'atk': [116,245],
        'Catch rate': [45,60,75,100],
        'pktype': 'Grass',
        'upgrade': '003'
    },
    '003':{
        'name': 'Venusaur',
        'hp': [270,364],
        'lvl': [32,100],
        'atk': [152,289],
        'Catch rate': [25,40,55,100],
        'pktype': 'Grass',
        'upgrade': ''
    },
    "004":{
        'name': 'Charmander',
        'hp': [188,282],
        'lvl': [1,15],
        'atk': [98,223],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fire',
        'upgrade': '005'
    },
    "005":{
        'name': 'Charmeleon',
        'hp': [226,320],
        'lvl': [16,35],
        'atk': [119,249],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fire',
        'upgrade': '006'
    },
    "006":{
        'name': 'Charizard',
        'hp': [266,360],
        'lvl': [36,100],
        'atk': [155,293],
        'Catch rate': [25,40,55,100],
        'pktype': 'Fire',
        'upgrade': ''
    },
    "007":{
        'name': 'Squirtle',
        'hp': [198,292],
        'lvl': [1,15],
        'atk': [90,214],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': '008'
    },
    "008":{
        'name': 'Wartortle',
        'hp': [228,322],
        'lvl': [16,35],
        'atk': [117,247],
        'Catch rate': [45,60,75,100],
        'pktype': 'Water',
        'upgrade': '009'
    },
    "009":{
        'name': 'Blastoise',
        'hp': [268,362],
        'lvl': [36,100],
        'atk': [153,291],
        'Catch rate': [25,40,55,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "010":{
        'name': 'Caterpie',
        'hp': [200,294],
        'lvl': [1,6],
        'atk': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': 'Bug',
        'upgrade': '011'
    },
    "011":{
        'name': 'Metapod',
        'hp': [210,304],
        'lvl': [7,9],
        'atk': [40,152],
        'Catch rate': [65,80,90,100],
        'pktype': 'Bug',
        'upgrade': '012'
    },
    "012":{
        'name': 'Butterfree',
        'hp': [230,324],
        'lvl': [10,100],
        'atk': [85,207],
        'Catch rate': [45,60,75,100],
        'pktype': 'Bug',
        'upgrade': ''
    },
    "013":{
        'name': 'Weedle',
        'hp': [190,284],
        'lvl': [1,6],
        'atk': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': 'Bug',
        'upgrade': '014'
    },
    "014":{
        'name': 'Kakuna',
        'hp': [200,294],
        'lvl': [7,9],
        'atk': [49,163],
        'Catch rate': [65,80,90,100],
        'pktype': 'Bug',
        'upgrade': '015'
    },
    "015":{
        'name': 'Beedrill',
        'hp': [240,334],
        'lvl': [10,100],
        'atk': [166,306],
        'Catch rate': [45,60,75,100],
        'pktype': 'Bug',
        'upgrade': ''
    },
    "016":{
        'name': 'Pidgey',
        'hp': [190,284],
        'lvl': [1,17],
        'atk': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': 'Normal',
        'upgrade': '017'
    },
    "017":{
        'name': 'Pidgeotto',
        'hp': [236,330],
        'lvl': [18,35],
        'atk': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',
        'upgrade': '018'
    },
    "018":{
        'name': 'Pidgeot',
        'hp': [276,370],
        'lvl': [36,100],
        'atk': [148,284],
        'Catch rate': [45,60,75,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "019":{
        'name': 'Rattata',
        'hp': [170,264],
        'lvl': [1,19],
        'atk': [105,232],
        'Catch rate': [75,85,95,100],
        'pktype': 'Bug',
        'upgrade': '020'
    },
    "020":{
        'name': 'Raticate',
        'hp': [220,314],
        'lvl': [20,100],
        'atk': [150,287],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "021":{
        'name': 'Spearow',
        'hp': [190,284],
        'lvl': [1,19],
        'atk': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': 'Normal',
        'upgrade': '022'
    },
    "022":{
        'name': 'Fearow',
        'hp': [240,334],
        'lvl': [20,100],
        'atk': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "023":{
        'name': 'Ekans',
        'hp': [180,274],
        'lvl': [1,21],
        'atk': [112,240],
        'Catch rate': [75,85,95,100],
        'pktype': 'Poison',
        'upgrade': '024'
    },
    "024":{
        'name': 'Arbok',
        'hp': [230,324],
        'lvl': [22,100],
        'atk': [175,314],
        'Catch rate': [65,80,90,100],
        'pktype': 'Poison',
        'upgrade': ''
    },
    "025":{
        'name': 'Pikachu',
        'hp': [180,274],
        'lvl': [1,100],
        'atk': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': 'Electric',
        'upgrade': '026'
    },
    "026":{
        'name': 'Raichu',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [166,306],
        'Catch rate': [45,60,75,100],
        'pktype': 'Electric',
        'upgrade': ''
    },
    "027":{
        'name': 'Sandshrew',
        'hp': [210,304],
        'lvl': [1,21],
        'atk': [139,273],
        'Catch rate': [75,85,95,100],
        'pktype': 'Ground',
        'upgrade': '028'
    },
    "028":{
        'name': 'Sandslash',
        'hp': [260,354],
        'lvl': [22,100],
        'atk': [184,328],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "029":{
        'name': 'Nidoran-♀',
        'hp': [220,314],
        'lvl': [1,15],
        'atk': [89,212],
        'Catch rate': [75,85,95,100],
        'pktype': 'Poison',
        'upgrade': '030'
    },
    "030":{
        'name': 'Nidorina',
        'hp': [250,344],
        'lvl': [16,35],
        'atk': [116,245],
        'Catch rate': [65,80,90,100],
        'pktype': 'Poison',
        'upgrade': '031'
    },
    "031":{
        'name': 'Nidoqueen',
        'hp': [290,384],
        'lvl': [36,100],
        'atk': [170,311],
        'Catch rate': [45,60,75,100],
        'pktype': 'Poison',
        'upgrade': ''
    },
    "032":{
        'name': 'Nidoran-♂︎',
        'hp': [202,292],
        'lvl': [1,15],
        'atk': [107,234],
        'Catch rate': [75,85,95,100],
        'pktype': 'Poison',
        'upgrade': '033'
    },
    "033":{
        'name': 'Nidorino',
        'hp': [232,326],
        'lvl': [16,35],
        'atk': [134,267],
        'Catch rate': [65,80,90,100],
        'pktype': 'Poison',
        'upgrade': '034'
    },
    "034":{
        'name': 'Nidoking',
        'hp': [272,366],
        'lvl': [36,100],
        'atk': [188,333],
        'Catch rate': [45,60,75,100],
        'pktype': 'Poison',
        'upgrade': ''
    },
    "035":{
        'name': 'Clefairy',
        'hp': [250,344],
        'lvl': [1,100],
        'atk': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fairy',
        'upgrade': '036'
    },
    "036":{
        'name': 'Clefable',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fairy',
        'upgrade': ''
    },
    "037":{
        'name': 'Vulpix',
        'hp': [186,280],
        'lvl': [1,100],
        'atk': [78,199],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fire',
        'upgrade': '038'
    },
    "038":{
        'name': 'Ninetales',
        'hp': [256,350],
        'lvl': [1,100],
        'atk': [141,276],
        'Catch rate': [25,40,55,100],
        'pktype': 'Fire',
        'upgrade': ''
    },
    "039":{
        'name': 'Jigglypuff',
        'hp': [340,434],
        'lvl': [1,100],
        'atk': [85,207],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fairy',      
        'upgrade': '040'
    },
    "040":{
        'name': 'Wigglytuff',
        'hp': [390,484],
        'lvl': [1,100],
        'atk': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fairy',        
        'upgrade': ''
    },
    "041":{
        'name': 'Zubat',
        'hp': [190,284],
        'lvl': [1,21],
        'atk': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': 'Poison',        
        'upgrade': '042'
    },
    "042":{
        'name': 'Golbat',
        'hp': [260,354],
        'lvl': [22,100],
        'atk': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': 'Poison',
        'upgrade': ''
    },
    "043":{
        'name': 'Oddish',
        'hp': [200,294],
        'lvl': [1,20],
        'atk': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': 'Grass',  
        'upgrade': '044'
    },
    "044":{
        'name': 'Gloom',
        'hp': [230,324],
        'lvl': [21,100],
        'atk': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': 'Grass',         
        'upgrade': '045'
    },
    "045":{
        'name': 'Vileplume',
        'hp': [260,354],
        'lvl': [21,100],
        'atk': [148,284],
        'Catch rate': [45,60,75,100],
        'pktype': 'Grass',        
        'upgrade': ''
    },
    "046":{
        'name': 'Paras',
        'hp': [180,274],
        'lvl': [1,23],
        'atk': [130,262],
        'Catch rate': [75,85,95,100],
        'pktype': 'Grass',        
        'upgrade': '047'
    },
    "047":{
        'name': 'Parasect',
        'hp': [230,324],
        'lvl': [24,100],
        'atk': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': 'Grass',         
        'upgrade': ''
    },
    "048":{
        'name': 'Venonat',
        'hp': [230,324],
        'lvl': [1,30],
        'atk': [103,229],
        'Catch rate': [75,85,95,100],
        'pktype': 'Bug',         
        'upgrade': '049'
    },
    "049":{
        'name': 'Venomoth',
        'hp': [250,344],
        'lvl': [31,100],
        'atk': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': 'Bug',
        'upgrade': ''
    },
    "050":{
        'name': 'Diglett',
        'hp': [130,224],
        'lvl': [1,25],
        'atk': [103,229],
        'Catch rate': [75,85,95,100],
        'pktype': 'Ground',         
        'upgrade': '051'
    },
    "051":{
        'name': 'Dugtrio',
        'hp': [180,274],
        'lvl': [26,100],
        'atk': [184,328],
        'Catch rate': [65,80,90,100],
        'pktype': 'Ground',    
        'upgrade': ''
    },
    "052":{
        'name': 'Meowth',
        'hp': [190,284],
        'lvl': [1,27],
        'atk': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': 'Normal',         
        'upgrade': '053'
    },
    "053":{
        'name': 'Persian',
        'hp': [240,334],
        'lvl': [28,100],
        'atk': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',        
        'upgrade': ''
    },
    "054":{
        'name': 'Psyduck',
        'hp': [210,304],
        'lvl': [1,32],
        'atk': [98,223],
        'Catch rate': [75,85,95,100],
        'pktype': 'Water',
        'upgrade': '055'
    },
    "055":{
        'name': 'Golduck',
        'hp': [270,364],
        'lvl': [33,100],
        'atk': [152,289],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',        
        'upgrade': ''
    },
    "056":{
        'name': 'Mankey',
        'hp': [190,284],
        'lvl': [1,27],
        'atk': [148,284],
        'Catch rate': [75,85,95,100],
        'pktype': 'Fighting',         
        'upgrade': '057'
    },
    "057":{
        'name': 'Primeape',
        'hp': [240,334],
        'lvl': [28,100],
        'atk': [193,339],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fighting',        
        'upgrade': ''
    },
    "058":{
        'name': 'Growlithe',
        'hp': [220,314],
        'lvl': [1,100],
        'atk': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fire',      
        'upgrade': '059'
    },
    "059":{
        'name': 'Arcanine',
        'hp': [290,384],
        'lvl': [1,100],
        'atk': [202,350],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fire',        
        'upgrade': ''
    },
    "060":{
        'name': 'Poliwag',
        'hp': [190,284],
        'lvl': [1,24],
        'atk': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': 'Water',
        'upgrade': '061'
    },
    "061":{
        'name': 'Poliwhirl',
        'hp': [240,334],
        'lvl': [25,100],
        'atk': [121,251],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': '062'
    },
    "062":{
        'name': 'Poliwrath',
        'hp': [290,384],
        'lvl': [25,100],
        'atk': [175,317],
        'Catch rate': [45,60,75,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "063":{
        'name': 'Abra',
        'hp': [160,254],
        'lvl': [1,15],
        'atk': [40,152],
        'Catch rate': [75,85,95,100],
        'pktype': 'Psychic',
        'upgrade': '064'
    },
    "064":{
        'name': 'Kadabra',
        'hp': [190,284],
        'lvl': [16,100],
        'atk': [67,185],
        'Catch rate': [65,80,90,100],
        'pktype': 'Psychic',
        'upgrade': '065'
    },
    "065":{
        'name': 'Alakazam',
        'hp': [220,314],
        'lvl': [16,100],
        'atk': [94,218],
        'Catch rate': [25,40,55,100],
        'pktype': 'Psychic',
        'upgrade': ''
    },
    "066":{
        'name': 'Machop',
        'hp': [250,344],
        'lvl': [1,27],
        'atk': [148,284],
        'Catch rate': [75,85,95,100],
        'pktype': 'Fighting',
        'upgrade': '067'
    },
    "067":{
        'name': 'Machoke',
        'hp': [270,364],
        'lvl': [28,100],
        'atk': [184,328],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fighting',
        'upgrade': '068'
    },
    "068":{
        'name': 'Machamp',
        'hp': [290,384],
        'lvl': [28,100],
        'atk': [238,394],
        'Catch rate': [25,40,55,100],
        'pktype': 'Fighting',
        'upgrade': ''
    },
    "069":{
        'name': 'Bellsprout',
        'hp': [210,304],
        'lvl': [1,20],
        'atk': [139,273],
        'Catch rate': [75,85,95,100],
        'pktype': 'Grass',
        'upgrade': '070'
    },
    "070":{
        'name': 'Weepinbell',
        'hp': [240,334],
        'lvl': [21,100],
        'atk': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': 'Grass',
        'upgrade': '071'
    },
    "071":{
        'name': 'Victreebel',
        'hp': [270,364],
        'lvl': [21,100],
        'atk': [193,339],
        'Catch rate': [45,60,75,100],
        'pktype': 'Grass',
        'upgrade': ''
    },
    "072":{
        'name': 'Tentacool',
        'hp': [190,284],
        'lvl': [1,29],
        'atk': [76,196],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': '073'
    },
    "073":{
        'name': 'Tentacruel',
        'hp': [270,364],
        'lvl': [30,100],
        'atk': [130,262],
        'Catch rate': [45,60,75,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "074":{
        'name': 'Geodude',
        'hp': [190,284],
        'lvl': [1,24],
        'atk': [148,284],
        'Catch rate': [75,85,95,100],
        'pktype': 'Rock',
        'upgrade': '075'
    },
    "075":{
        'name': 'Graveler',
        'hp': [220,314],
        'lvl': [25,100],
        'atk': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': 'Rock',
        'upgrade': '076'
    },
    "076":{
        'name': 'Golem',
        'hp': [270,364],
        'lvl': [25,100],
        'atk': [220,372],
        'Catch rate': [25,40,55,100],
        'pktype': 'Rock',
        'upgrade': ''
    },
    "077":{
        'name': 'Ponyta',
        'hp': [210,304],
        'lvl': [1,39],
        'atk': [147,295],
        'Catch rate': [65,80,90,100],
        'pktype': 'Fire',
        'upgrade': '078'
    },
    "078":{
        'name': 'Rapidash',
        'hp': [240,334],
        'lvl': [40,100],
        'atk': [184,328],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fire',
        'upgrade': '079'
    },
    "079":{
        'name': 'Slowpoke',
        'hp': [290,384],
        'lvl': [1,36],
        'atk': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': 'Water',
        'upgrade': '080'
    },
    "080":{
        'name': 'Slobro',
        'hp': [300,394],
        'lvl': [37,100],
        'atk': [139,273],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "081":{
        'name': 'Magnemite',
        'hp': [160,254],
        'lvl': [1,29],
        'atk': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': 'Electric',
        'upgrade': '082'
    },
    "082":{
        'name': 'Magneton',
        'hp': [210,304],
        'lvl': [30,100],
        'atk': [112,240],
        'Catch rate': [65,80,90,100],
        'pktype': 'Electric',
        'upgrade': ''
    },
    "083":{
        'name': "Farfetch'd",
        'hp': [214,308],
        'lvl': [1,100],
        'atk': [166,306],
        'Catch rate': [25,40,55,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "084":{
        'name': 'Doduo',
        'hp': [180,274],
        'lvl': [1,30],
        'atk': [157,295],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',
        'upgrade': '085'
    },
    "085":{
        'name': 'Dodrio',
        'hp': [230,324],
        'lvl': [31,100],
        'atk': [202,350],
        'Catch rate': [45,60,75,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "086":{
        'name': 'Seel',
        'hp': [240,334],
        'lvl': [1,33],
        'atk': [85,207],
        'Catch rate': [75,85,95,100],
        'pktype': 'Water',
        'upgrade': '087'
    },
    "087":{
        'name': 'Dewgong',
        'hp': [294,384],
        'lvl': [34,100],
        'atk': [130,262],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "088":{
        'name': 'Grimer',
        'hp': [270,364],
        'lvl': [1,37],
        'atk': [148,284],
        'Catch rate': [75,85,95,100],
        'pktype': 'Poison',
        'upgrade': '089'
    },
    "089":{
        'name': 'Muk',
        'hp': [320,414],
        'lvl': [38,100],
        'atk': [193,339],
        'Catch rate': [65,80,90,100],
        'pktype': 'Poison',
        'upgrade': ''
    },
    "090":{
        'name': 'Shellder',
        'hp': [170,264],
        'lvl': [1,100],
        'atk': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': 'Water',
        'upgrade': '091'
    },
    "091":{
        'name': 'Cloyster',
        'hp': [210,304],
        'lvl': [1,100],
        'atk': [175,317],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "092":{
        'name': 'Gastly',
        'hp': [170,264],
        'lvl': [1,24],
        'atk': [67,185],
        'Catch rate': [75,85,95,100],
        'pktype': 'Ghost',
        'upgrade': '093'
    },
    "093":{
        'name': 'Haunter',
        'hp': [200,294],
        'lvl': [25,100],
        'atk': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': 'Ghost',
        'upgrade': '094'
    },
    "094":{
        'name': 'Gengar',
        'hp': [230,324],
        'lvl': [25,100],
        'atk': [121,251],
        'Catch rate': [25,40,55,100],
        'pktype': 'Ghost',
        'upgrade': ''
    },
    "095":{
        'name': 'Onix',
        'hp': [180,274],
        'lvl': [1,100],
        'atk': [85,207],
        'Catch rate': [45,60,75,100],
        'pktype': 'Rock',
        'upgrade': ''
    },
    "096":{
        'name': 'Drowzee',
        'hp': [230,324],
        'lvl': [1,25],
        'atk': [90,214],
        'Catch rate': [75,85,95,100],
        'pktype': 'Psychic',
        'upgrade': '097'
    },
    "097":{
        'name': 'Hypno',
        'hp': [280,374],
        'lvl': [26,100],
        'atk': [135,269],
        'Catch rate': [65,80,90,100],
        'pktype': 'Psychic',
        'upgrade': ''
    },
    "098":{
        'name': 'Krabby',
        'hp': [170,264],
        'lvl': [1,27],
        'atk': [193,339],
        'Catch rate': [75,85,95,100],
        'pktype': 'Water',
        'upgrade': '099'
    },
    "099":{
        'name': 'Kingler',
        'hp': [220,314],
        'lvl': [28,100],
        'atk': [238,394],
        'Catch rate': [65,80,90,100],
        'pktype': 'Water',
        'upgrade': ''
    },
    "100":{
        'name': 'Voltorb',
        'hp': [190,284],
        'lvl': [1,29],
        'atk': [58,174],
        'Catch rate': [75,85,95,100],
        'pktype': 'Electric',
        'upgrade': '101'
    },
    "101":{
        'name': 'Electrode',
        'hp': [230,324],
        'lvl': [30,100],
        'atk': [94,218],
        'Catch rate': [65,80,90,100],
        'pktype': 'Electric',
        'upgrade': ''
    },
    "102":{
        'name': 'Exeggcute',
        'hp': [230,324],
        'lvl': [1,100],
        'atk': [76,196],
        'Catch rate': [75,85,95,100],
        'pktype': 'Grass',
        'upgrade': '103'
    },
    "103":{
        'name': 'Exeggcutor',
        'hp': [300,394],
        'lvl': [1,100],
        'atk': [175,314],
        'Catch rate': [45,60,75,100],
        'pktype': 'Grass',
        'upgrade': ''
    },
    "104":{
        'name': 'Cubone',
        'hp': [210,304],
        'lvl': [1,27],
        'atk': [94,218],
        'Catch rate': [75,85,95,100],
        'pktype': 'Ground',
        'upgrade': '105'
    },
    "105":{
        'name': 'Marowak',
        'hp': [230,324],
        'lvl': [28,100],
        'atk': [148,284],
        'Catch rate': [65,80,90,100],
        'pktype': 'Ground',
        'upgrade': ''
    },
    "106":{
        'name': 'Hitmonlee',
        'hp': [210,304],
        'lvl': [20,100],
        'atk': [220,372],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fighting',
        'upgrade': ''
    },
    "107":{
        'name': 'Hitmonchan',
        'hp': [210,304],
        'lvl': [20,100],
        'atk': [193,339],
        'Catch rate': [45,60,75,100],
        'pktype': 'Fighting',
        'upgrade': ''
    },
    "108":{
        'name': 'Lickitung',
        'hp': [290,384],
        'lvl': [1,32],
        'atk': [103,229],
        'Catch rate': [45,60,75,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "109":{
        'name': 'Koffing',
        'hp': [190,284],
        'lvl': [1,34],
        'atk': [121,251],
        'Catch rate': [75,85,95,100],
        'pktype': 'Poison',
        'upgrade': '110'
    },
    "110":{
        'name': 'Weezing',
        'hp': [240,334],
        'lvl': [35,100],
        'atk': [166,306],
        'Catch rate': [65,80,90,100],
        'pktype': 'Poison',
        'upgrade': ''
    },
    "111":{
        'name': 'Rhyhorn',
        'hp': [270,364],
        'lvl': [1,41],
        'atk': [157,295],
        'Catch rate': [75,85,95,100],
        'pktype': 'Ground',
        'upgrade': '112'
    },
    "112":{
        'name': 'Rhydon',
        'hp': [320,414],
        'lvl': [42,100],
        'atk': [238,394],
        'Catch rate': [65,80,90,100],
        'pktype': 'Ground',
        'upgrade': ''
    },
    "113":{
        'name': 'Chansey',
        'hp': [610,704],
        'lvl': [1,100],
        'atk': [13,119],
        'Catch rate': [65,80,90,100],
        'pktype': 'Normal',
        'upgrade': ''
    },
    "114":{
        'name': 'Tangela',
        'hp': [240,334],
        'lvl': [1,37],
        'atk': [103,229],
        'Catch rate': [65,80,90,100],
        'pktype': 'Grass',
        'upgrade': ''
    },
    "150":{
        'name': 'Mewtwo',
        'hp': [322,416],
        'lvl': [1,100],
        'atk': [202,350],
        'Catch rate': [5,20,35,100],
        'pktype': 'Psychic',
        'upgrade': ''
    }
}

class Pokemon():
    id = ''
    name = ''
    hp = 0
    lvl = 0
    atk = 0
    catchrate = []
    pktype = ''
    upgrade = ''

    def getPhoto(self):
        file_name = f"{config.run_path}/images/{self.id}.jpg"
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
    def init(self,id:str,name:str,lvl:int,hp:int,atk:int,catchrate:list,pktype:str,upgrade:str):
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