import sqlite3
import json
import uuid

# ###################
# ###### DB section
# ###################

# connect to the database
conn = sqlite3.connect('data.db')

# create a table to store the data
def createTable(db):
    conn.execute('''CREATE TABLE IF NOT EXISTS '''+db+'''
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 data TEXT NOT NULL);''')

createTable('data')

def insert(_json):
    data = json.dumps(_json)

    db = _json['parent'] or 'data'

    createTable(db)
    
    conn.execute("INSERT INTO "+db+" (data) VALUES (?)", (data,))
    conn.commit()

    
def findAll(db = 'data'):
    data = conn.execute("SELECT * FROM "+db)

    allData = []
    
    # loop through the data and append each row to the result list
    for row in data:
        allData.append(json.loads(row[1]))

    return allData

def find(specs, db = 'data'):
    allData = findAll(db)
    foundData = []
    
    # loop through the data and check if it matches the given specifications
    for data in allData:
        if all(item in data.items() for item in specs.items()):
            foundData.append(data)
    
    return foundData


# ###################
# ###### Records Section
# ###################

class Record:
    def __init__(self):
        self.parent = ""
        self.label = ""
        self.id = str(uuid.uuid4())
        self.commonId = ""

    def setAttr(self, attr, data):
        setattr(self, attr, data)
        return self

    def setSubAttr(self, attr, subattr, data):
        getattr(self, attr)[subattr] = data
        return self

    def getAttr(self, attr, data=None, subattr=None):
        res = getattr(self, attr)
        if subattr:
            res = res[subattr]
        if data is not None:
            return res == data
        return res

    def toJsonString(self):
        return json.dumps(self.__dict__)

    def toJsonObject(self):
        return json.loads(self.toJsonString())

    def loadFromJSON(self, jsonData):
        for key, value in jsonData.items():
            self.setAttr(key, value)
        return self

    def loadFromJSONString(self, jsonString):
        self.loadFromJSON(json.loads(jsonString))
        return self


class Person(Record):
    def __init__(self):
        super().__init__()
        self.parent = "people"
        self.accounts = []
        self.records = []
        self.info = {
            "age": 0,
            "job": "",
            "likes": [],
            "dislikes": []
        }


class Paper(Record):
    def __init__(self):
        super().__init__()
        self.parent = "papers"
        self.content = ""
        self.indexes = []
        self.language = ""

class OtherRecord(Record):
    def __init__(self):
        super().__init__()
        self.parent = "data"
        self.content = ""
        self.indexes = []



# ###################
# ###### Accounts Section
# ###################


class Account:
    def __init__(self, url, identifier, name):
        self.name = name
        self.url = url
        self.identifier = identifier

        self.additionalInfo = {}
        
    def toJsonString(self):
        return json.dumps(self.__dict__)

    def toJsonObject(self):
        return json.loads(self.toJsonString())

def telegram(username):
    return Account('https://telegram.me/', username, 'telegram').toJsonObject()

def twitter(username):
    return Account('https://twitter.com/', username, 'twitter').toJsonObject()

def facebook(username):
    return Account('https://facebook.com/', username, 'facebook').toJsonObject()

def instagram(username):
    return Account('https://instagram.com/', username, 'instagram').toJsonObject()

def phone(phone):
    return Account('none', phone, 'phone').toJsonObject()

def email(email):
    return Account('none', email, 'email').toJsonObject()



# ###################
# ###### Search Section
# ###################

siteMaps = [
    "Twitter;twitter;twitter.com/<%un%>",
    "Facebook;facebook;facebook.com/<%un%>",
    "Instagram;instagram;instagram.com/<%un%>",
    "LinkedIn;linkedin;linkedin.com/in/<%un%>",
    "GitHub;github;github.com/<%un%>",
    "Reddit;reddit;reddit.com/user/<%un%>",
    "YouTube;youtube;youtube.com/channel/<%un%>",
    "YouTubeUser;youtubeuser;youtube.com/user/<%un%>",
    "Twitch;twitch;twitch.tv/<%un%>",
    "TikTok;tiktok;tiktok.com/@<%un%>",
    "Pinterest;pinterest;pinterest.com/<%un%>",
    "SoundCloud;soundcloud;soundcloud.com/<%un%>",
    "Vimeo;vimeo;vimeo.com/<%un%>",
    "Medium;medium;medium.com/@<%un%>",
    "Discord;discord;discord.com/<%un%>#<%d%>",
    "Snapchat;snapchat;snapchat.com/add/<%un%>",
    "WhatsApp;whatsapp;wa.me/<%un%>",
    "Skype;skype;skype.com/<%un%>",
    "Slack;slack;yourworkspace.slack.com/team/<%un%>",
    "Zoom;zoom;zoom.us/j/<%un%>",
    "Microsoft Teams;microsoft teams;teams.microsoft.com/l/persona/<%un%>",
    "Google Meet;google meet;meet.google.com/<%un%>",
    "Yahoo! Mail;yahoo! mail;mail.yahoo.com/d/<%un%>",
    "AOL Mail;aol mail;mail.aol.com/<%un%>"
]

def searchUsername(username):



