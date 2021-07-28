from botFuncs import botMethods
from objectDepends import imagesDict

bot = botMethods.botObj(imagesDict)
screenShot = bot.returnImgObj('Restore')
bot.clickImage(screenShot)
print(screenShot)
