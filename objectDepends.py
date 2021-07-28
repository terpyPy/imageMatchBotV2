from imageObj import image, findFile
from pygetwindow import getWindowsWithTitle

gameWindow = getWindowsWithTitle('Runelite')[0]
gameWindowReg = [gameWindow.left,
                    gameWindow.top,
                    gameWindow.width,
                    gameWindow.height]

imagesDict = {
'Hp' : image.imageObj(findFile.getFile('health'), 0.9,gameWindowReg, True),
'Prayer' : image.imageObj(findFile.getFile('prayer'), 0.9,gameWindowReg, True),
'specs' : image.imageObj(findFile.getFile('fullSpec'), 0.9,gameWindowReg, True),
'ovl' : image.imageObj(findFile.getFile('overload'), 0.62,gameWindowReg),
'brew' : image.imageObj(findFile.getFile('saraBrew'), 0.65,gameWindowReg),
'Restore' : image.imageObj(findFile.getFile('superRestore'), 0.7,gameWindowReg),
'notification' : image.imageObj(findFile.getFile('potionNotification'), 0.85,gameWindowReg,True),
'killText' : image.imageObj(findFile.getFile('hydraKills'), 0.5,gameWindowReg,True),
'door' : image.imageObj(findFile.getFile('hdoor_v2'), 0.60, gameWindowReg, True),
'Tile' : image.imageObj(findFile.getFile('teleObject'), 0.80, gameWindowReg, True),
'bossName' : image.imageObj(findFile.getFile('hydrasName'), 0.75, gameWindowReg, True),
'bankStall' : image.imageObj(findFile.getFile('bankStall'), 0.8, gameWindowReg, True),
'presetLeftclick' : image.imageObj(findFile.getFile('presetsLeftClick'), 0.85, gameWindowReg, False),
'presetFive' : image.imageObj(findFile.getFile('presetFive'),0.8, gameWindowReg, False),
'loadPreset' : image.imageObj(findFile.getFile('loadPreset'), 0.8, gameWindowReg, False),
'presetExit' : image.imageObj(findFile.getFile('presetExit'), 0.9, gameWindowReg, False),
}

