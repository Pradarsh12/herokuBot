import os

class Config:
    BOT_TOKEN = "1406408953:AAHOuBQocs7-HsexyYyc_rprbt0C-S368sw"
    HEROKU_API_KEY = "14824f88-3cea-4b69-8ebe-e1899a835893"
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = "kaliwebs"
