import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "13194506"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fb241254ec347a40474ede09964401e6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kaushaly0541:kaushaly0541600@cluster0.mezlojc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
