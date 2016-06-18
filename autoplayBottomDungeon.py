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

# print "Click into bottom dungeon"
# pyautogui.click(x=1503, y=865)
# sleep(2)

while (dungeonRuns != 0):
	currentDungeonTime = dungeonTime
	print "Start selected dungeon"
	pyscreeze.locateCenterOnScreen('pictures/start_button.png')
	# pyautogui.click(x=1599, y=709)
	
	print "Wait %d seconds for dungeon to finish..." % (dungeonTime)
	while(currentDungeonTime > 0):
		sleep(1)
		if currentDungeonTime == 10:
			print "10 seconds left before resetting"
		currentDungeonTime -= 1

	print "Dungeon done, restarting..."
	pyautogui.doubleClick(interval = 2)
	sleep(2)
	pyautogui.click(x=900, y=800)
	sleep(2)
	pyautogui.click(x=665, y=546)
	sleep(2)

	dungeonRuns -= 1
	if dungeonRuns > 1:
		print "%d runs left" % (dungeonRuns)
	elif dungeonRuns == 1:
		print "Last Run"
	else:
		print "No more runs..."

print "Ran %s times." % (totalRuns)
sleep(5)
pyautogui.click(x=1805, y=1054)
sleep(2)
pyautogui.doubleClick(x=42, y=243)
sleep(10000)