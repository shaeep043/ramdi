import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "11796331"))
API_HASH = getenv("API_HASH", "a089161b52f234bb90a6eb915551e8c0")

BOT_TOKEN = getenv("BOT_TOKEN", "5663640542:AAGef1cfDgpwGgN0szhtpiUC2DJ4C0LHMso")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://pikachu:randi@cluster0.tndvlel.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001772857132"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Iro ダ ᴍᴜsɪᴄ")

OWNER_ID = list(map(int, getenv("OWNER_ID", " 5518757491").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Iro09/ramdi")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_bot_support")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/iro_x_support")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://telegra.ph/file/f84d28d91512a445ecce1.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQBclApF8cJnIX2nigWjqaGuRGF0MjXiJeo0eaZjnRIUQEbLNDEu95AQp-MFcRGnZfgaRe1yl22M00MV6wRJUuk2XdLivv41fH3Issjvcykyf1Wp33f3aluzcZmw6UYMRrVS3k_11Ls7xRtgquMkjssI9hxzZ6frJSFyyQsA55kv-Vjf3oh1NNj-drs8TGFZhmwC4oHIBxczwkziHEAiZ9dnM5_IipKXTFlet6a9t3ePBRNCbJ82fB_S-NEZjcbvXvuM-W-H-B11VfOHLOqXDOftZC2PRE9ZSht1wzN1Px94B2hcBb5L7qIH1nfVH8jdQeUXfIr7J527ppFDtce5I8YiAAAAAUQE2CIA")
STRING2 = getenv("STRING_SESSION2", "AQDE8jPSqKWglSNNzsIbIFwTwhHECZCOsbk65j2s6sbvyQn9puoQ4nstWDX3aLXocj47uYInPzc80VTX_FE5AjtJUWLqcN1jf4_uh3sFX_dw23FC5ai8-cVcJ5nNfPiS6NNFhKcAAhUgCmmGD_WfyVLpAe9fu1HOz54rFtBPdIslJ5FVTLUoYw3Dh3-bWKMhBO9UbHHXz5B4PSX-G_9-UKwtqHgHZh6zFoijANS_qSSAVGsBw6bbLNzZ6gf6l9a-q7usVxFr_Lr6nzFMzmFZXi5jiV6bzYprxOM6333rckOBO-rRqE2JRbK3mLo9COHUsdVbfRgX7BksQwT4XkA6dTn8AAAAAUbd6DAA")
STRING3 = getenv("STRING_SESSION3", "AQDFgEzpfGyfZhk1NRzsyxs2H_A5f3K4kVSK027HheJHkn_m_lG7IoL-yV4BmXRwP87v9SlPOkWcRw5Pj32hUfhZZ0jop9WotXeuPz2a1Dsrych1XyrnDWA5g79pS0ZXvbMu7cwPe_XU3ncFMxnFPiijPU7vck4Bu9SjduaGeXWFfTJ0chn-ukZn5oMonMKGNmflHr8IdpZ4yGVkC40nznuq9LKQ_gWE4kWX8-0npoaYxgiLUzYtCgPs15Z1yE0KwieJROfE_Ydu_wyxN6FDbKOt_kG2b0rJ5iP6GbXutaX5wEzy1-8koo86u2b0_qBt_UksW9LGnIr8DAgi0BnzsylEAAAAAVEmqJkA")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Iro.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/7c8a61882e4d9f5cf8f58.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/eee5e3d03dbfcf6514595.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/67ba43e3082b6e1ffa301.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/5afe84b93f9286e374116.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/6c471c9d087f24255d03e.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/3eade15762e7b448b3213.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/4f2864d18f53cb17bc923.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/854777fa09c90ef6ab192.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/897636168791e9eb2870e.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/8a81b61bce572fcc190e4.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/076f0e9b66661dbdb7ded.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/26d87da32d7f9bc176612.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/4d73990528b9c4ad43487.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/eee5e3d03dbfcf6514595.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/7c8a61882e4d9f5cf8f58.jpg"
