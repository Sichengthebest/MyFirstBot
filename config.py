import json
import os

def load_config():
   global CONFIG
   with open(config_file, 'r') as configfile:
      CONFIG = json.load(configfile)
   if not "token" in CONFIG:
      CONFIG["token"] = ""
   if not "coins" in CONFIG:
      CONFIG["coins"] = {}
   if not "hunt" in CONFIG:
      CONFIG["hunt"] = {}
   if not "fish" in CONFIG:
      CONFIG["fish"] = {}
   if not "pk" in CONFIG:
      CONFIG["pk"] = {}
   
   return CONFIG

def save_config():
   with open(config_file, 'w') as configfile:
         json.dump(CONFIG, configfile, indent=4,ensure_ascii=False)

CONFIG = {}
config_file = 'my.json'

run_path = os.getcwd()
# load_config()
# CONFIG = migration.migration(CONFIG)   # version.新的
# save_config()


def save_backup_config():
   # config_file = f"my{datetime.now().strftime("YYMMDD")}.json"  # my20201213.json

   with open(config_file, 'w') as configfile:
      json.dump(CONFIG, configfile, indent=4,ensure_ascii=False)

# a = ""
# now = datetime.now()
# print(now)
# snow = now.strftime("%Y/%m/%d %H:%M:%S")
# print(snow)
# now2 = datetime.strptime(snow,"%Y/%m/%d %H:%M:%S")
# print(now2)