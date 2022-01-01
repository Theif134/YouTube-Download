import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5065805596:AAFQyMYIdsws0wPpzUoLfVkMxmyOpbzJtbo")

    APP_ID = int(os.environ.get("APP_ID", 4773639 ))

    API_HASH = os.environ.get("API_HASH", "493cb7cb8428c5de4490ab47e936fb96")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "no")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "yes")
