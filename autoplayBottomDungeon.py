import pyautogui
import pyscreeze
from time import sleep

# Variables used in script
dungeonRuns = input('How many runs of the dungeon? ')
totalRuns = dungeonRuns
dungeonTime = 90

print "Starting bot... Wait 3 seconds"
for i in list( reversed( range(3) ) ):
	print (i + 1)
	sleep(1)
print "Start"

"""
Removing the initial click from dungeon selection screen
in case desired dungeon cannot be at bottom of list
"""
# print "Click into bottom dungeon"
# pyautogui.click(x=1503, y=865)
# sleep(2)

while (dungeonRuns != 0):

	# Dungeon time re-initialized each loop
	currentDungeonTime = dungeonTime

	print "Start selected dungeon"
	pyscreeze.locateCenterOnScreen('pictures/start_button.png')
	
	print "Wait %d seconds for dungeon to finish..." % (dungeonTime)
	while(currentDungeonTime > 0):
		sleep(1)
		if currentDungeonTime == 10:
			print "10 seconds left before resetting"
		currentDungeonTime -= 1

	print "Dungeon done, restarting..."
	pyautogui.doubleClick(interval = 2)

	pyscreeze.locateOnScreen('pictures/closeDialog.png')
	sleep(2)
	pyscreeze.locateOnScreen('pictures/replay.png')
	sleep(2)

	dungeonRuns -= 1
	if dungeonRuns > 1:
		print "%d runs left" % (dungeonRuns)
	elif dungeonRuns == 1:
		print "Last Run"
	else:
		print "No more runs..."

print "Ran %s times." % (totalRuns)

# Output text to a log text file
with open("autoPlayLog.txt", "w") as outputText:
	outputText.write("The dungeon was run %d times" % (totalRuns))
