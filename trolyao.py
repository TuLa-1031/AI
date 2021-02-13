import speech_recognition
import pyttsx3
from datetime import date, datetime
import webbrowser

robot_ear = speech_recognition.Recognizer()   # KHỞI TẠO-----
robot_mouth = pyttsx3.init()
robot_brain = ""
gg = 'https://www.google.com/'
yt = 'https://www.youtube.com/'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


while True:           # NGHE-----
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)
	try:
	    you = robot_ear.recognize_google(audio)
	except:
		you = ""
		print("You: " + you)

	
	print("Robot: ...")      #   HIỂU-----
	if you == "":
	   robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello Tung Lam"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "goodbye" in you:
		robot_brain = "Bye Tung Lam"
		print("robot: " + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif "open" in you:                #  MỞ CHROME
		robot_brain = "OK"
		if "Google" in you:
			webbrowser.get(chrome_path).open(gg)
		elif "YouTube" in you:
			webbrowser.get(chrome_path).open(yt)
	else:
		robot_brain = "I'm fine thank you and you"

	print("robot: " + robot_brain)    # NÓI-----
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()