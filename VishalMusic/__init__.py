





















from VishalMusic.core.bot import Nand
from VishalMusic.core.dir import dirr
from VishalMusic.core.git import git
from VishalMusic.core.userbot import Userbot
from VishalMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Nand()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()












