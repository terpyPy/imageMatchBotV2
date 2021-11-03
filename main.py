from botFuncs import botMethods
from objectDepends import imagesDict

bot = botMethods.botObj(imagesDict)
#
# ways to access bot image objects
#
# bot.returnImgObj('Restore')
# bot.clickImage(bot.images['Restore'].screenShot)
#
# or this below:
def clickAnyObj(objName):
    screenShot = bot.returnImgObj(objName)
    #
    # test code changing between images that rep the image located in other places
    print(screenShot,'1_________')
    if screenShot != None:
        bot.clickImage(screenShot)
    else:
        # images['GEguy'].searchFObj('newImg', newImg='GEguy1')

        bot.changeImgFile(objName)
        bot.returnImgObj(objName)
        bot.clickImage(bot.images[objName].screenShot)
        print(bot.images[objName].screenShot,'2______')

clickAnyObj('hydraDoor')
#clickAnyObj('GEguy')