import os


class Config(object):
    API_HASH = os.environ.get("")
    BOT_TOKEN = os.environ.get("")
    TELEGRAM_API = os.environ[""]
    OWNER = os.environ.get("")
    OWNER_USERNAME = os.environ.get("")
    PASSWORD = os.environ.get("")
    DATABASE_URL = os.environ.get("")
    LOGCHANNEL = os.environ.get("")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
