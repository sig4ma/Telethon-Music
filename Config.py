import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "20738210"))
    API_HASH = os.environ.get("API_HASH", "28ff0ff5e62f5e4acd3d887a8e91ba72")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6230445499:AAH3gFOXjieNj0Pwskkcqr25ey7EnTi5B90)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1AZWarzQBu2HvPGrAxxWHG0uDDYea1Uay2xyQPtKivk8uj3A4sZU5unU9aAMN5b5HzxaLTf0oPYqhVqR8MAuhDeuQPqSDr5YvfEz25CYHyaxIKSuoVPQHalp8FFTGUQxcdmBS9kPo39ajSGXopzDGjhsGcxF4_Dp0oHWdKYJxSsjA4Z-KmAQdR5s2d4mIVqhJ16ou3IjfnneDIn2mpurQ3qPoOhcJA1isVGIbhNUAitj_vXeZTiReVsacIAc9QULxHpJ2e5QkyMI6AAkqsyqXTq4n9FHUykvq7sM7_o8UU4sLkIDRKSc1EYzQ5jp1FB1p25mXoCeIz_FHLe6nd4tWUbfB4MkSau4=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RKMODER_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6133662746")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
