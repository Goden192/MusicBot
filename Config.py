import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6173575930:AAErOJwoZa17oYaKQgSGUwmW9AkQchdSsS4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJwBu4y4za8biltrIE2eDOy2UMbgGHvtRYkQj3u772vwEsbhj4d4ykNV95U6LxqM76Ho-5ztcOgMh_yASoCeJj4M2g1YAqG__TqwUTV98YazLtQlwu3hn5iuyteeGmY36xeY3cemI2wlAXo8IbqsHcZwL7yAQ8doqrSBzzpI4bPWy04T1FZcwYFdbALpdxnbAB_RbTlxlEBfsQ0HVzx4fgWlkX93Gn7KY26Is089QSHEF7IBqPSufpVwp_VBc82t9Yd5q6ayhQS5KaRAAdizMQamp3Eeca9peeIK2qqq-tazXftFeDxeLuhDyvzK6zMuSXdNAmdzvDqn4TH-L2qg9N-tkE4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "GKmusicBestbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5919785744")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
