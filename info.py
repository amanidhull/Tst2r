import os
import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '22511326'))
API_HASH = environ.get('API_HASH', '9be0b06eabff6c9132955954064a67b2')
BOT_TOKEN = environ.get('BOT_TOKEN', '7701224120:AAEjtp9IE9hXvEWsVDkQcil-XzsA5TLXDsg')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7309705064 1393092521').split()]
USERNAME = environ.get('USERNAME', "https://t.me/IMDbFileTGBot") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001651812610'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/SB_Movie_Group')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001917260095').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://primebricks941:bholaverma7788@cluster0.zjjov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'okfiles')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001963473990'))  # set shortner log channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002043465084')) # The movie you upload in it will be deleted from the bot.
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002023751348'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001764238165'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001625752177'))
request_channel = environ.get('REQUEST_CHANNEL', '-1001838363129') # If anyone sends a request message to your bot, you will get it in this channel.
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002176919909')) # 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+Vegv963Nf2kzYzBl') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/SB_Botz_Update/104")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/SB_Botz_Update/104")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/SB_Botz_Update/104")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "23b723c2db0550b4a9dab4b9f5c04d3dddab6534")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'onepageyam.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "23b723c2db0550b4a9dab4b9f5c04d3dddab6534")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'onepageyam.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "23b723c2db0550b4a9dab4b9f5c04d3dddab6534")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'onepageyam.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://telegra.ph/file/4bd2d0c2cc16d5cb4e3a7.jpg https://telegra.ph/file/0979efecb6566faaa9574.jpg https://telegra.ph/file/2db8eb71a07525be79ab5.jpg https://telegra.ph/file/b94dc2f40e95476385d95.jpg https://telegra.ph/file/c68743010ff1d9629df46.jpg https://telegra.ph/file/160d08c0ac26cf963cb51.jpg https://telegra.ph/file/9b9b657fc9112b8e3b912.jpg https://telegra.ph/file/53d3774666fc1a0fbe0c3.jpg https://telegra.ph/file/6911aaa34ac3f2ed9b2ed.jpg https://telegra.ph/file/a62e2e3b0394195c20e8a.jpg https://telegra.ph/file/9e3c9d5f4026b300b3c66.jpg https://telegra.ph/file/23fc6d5956ef8936abbcb.jpg')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://envs.sh/PSI.jpg")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://i.ibb.co/7yVMN00/photo-2024-11-22-01-36-17-7439911550367825948.jpg')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/9f3f47c690bbcc67633c2.jpg'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
IGNORE_WORDS = (list(os.environ.get("IGNORE_WORDS").split(",")) if os.environ.get("IGNORE_WORDS") else [])
IGNORE_WORDS=["movies", "Movies", ",", "episode", "Episode", "episodes", "Episodes", "south indian", "south indian movie", "South Indian Movie", "south movie", "South Movie", "South Indian", "web-series", "punjabi", "marathi", "hindi me bhejo", "hindi", "gujrati", "combined", "!", "kro", "jaldi", "Audio", "audio", "movi", "language", "Language", "Hollywood", "All", "all", "bollywood", "Bollywood", "South", "south", "HD", "hd", "karo", "Karo", "fullepisode", "please", "plz", "Please", "Plz", "send", "link", "Link", "full", "Full", "dabbed", "dubbed", "gujarati", "gujrati", "Gujarati", "Gujrati", "season", "Season", "web", "series", "Web", "Series", "webseries", "WebSeries", "upload", "HD", "Hd", "bhejo", "ful", "Send", "Bhejo", "movie"]
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', True) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "https://elderly-brinna-webhosting-dd2eb40f.koyeb.app/")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'tutorial_2': TUTORIAL_2,
            'tutorial_3': TUTORIAL_3,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}

admin_cmds = [
    "/add_premium", "/premium_users", "/remove_premium", "/add_redeem",
    "/refresh", "/set_muc", "/pm_search_on", "/pm_search_off",
    "/set_ads", "/del_ads", "/setlist", "/clearlist",
    "/verify_id", "/index", "/send", "/leave",
    "/ban", "/unban", "/broadcast", "/grp_broadcast",
    "/delreq", "/channel", "/del_file", "/delete",
    "/deletefiles", "/deleteall", 
    "All These Commands Can Be Used Only By Admins.", 
    "⚡ powered by @SB_Botz_Update"
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"}
]
