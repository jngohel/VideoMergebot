import os


class Config(object):
    API_HASH = os.environ.get("b2ec3ab8ed156e7a6782f3d7d1acbaf6")
    BOT_TOKEN = os.environ.get("7028334632:AAEXTOfWu3E9eXMrQbHzPKdtWroPRR3jelk")
    TELEGRAM_API = os.environ["24998279"]
    OWNER = os.environ.get("OWNER")
    OWNER_USERNAME = os.environ.get("JNGohell")
    PASSWORD = os.environ.get("Abhi96")
    DATABASE_URL = os.environ.get("mongodb+srv://Jng:jng@cluster0.vvrnobg.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001988014238")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"# tired of redeploying :(
UPSTREAM_REPO = "https://github.com/jngohel/VideoMergebot"
UPSTREAM_BRANCH = "master"
