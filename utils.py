import configparser
from datetime import datetime
from colorama import Fore, Style
import pymongo
import time

def log(content):
    print(f'[{datetime.now()}] {Fore.LIGHTBLUE_EX}{content}{Style.RESET_ALL}')
def log_success(content):
    print(f'[{datetime.now()}] {Fore.LIGHTGREEN_EX}{content}{Style.RESET_ALL}')
def log_error(content):
    print(f'[{datetime.now()}] {Fore.LIGHTRED_EX}{content}{Style.RESET_ALL}')   

# Read DB config
def readDBConfig() -> dict:
    config = configparser.ConfigParser()
    config.read('CONFIG.ini')
    username = config['DATABASE']['USERNAME']
    passwd = config['DATABASE']['PASSWORD']

    if username and passwd:
        return {'username':username,'password':passwd}
    else:
        return {'message':'Fill data to MongoDB!'}
    
def mongo_check_db()-> str:
    username = readDBConfig().get('username')
    password = readDBConfig().get('password')
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@kurierzyaio.3p9sozk.mongodb.net/?retryWrites=true&w=majority")
    try:
        client.admin.command('ping')
        return '200'
    except Exception as e:
        return e
