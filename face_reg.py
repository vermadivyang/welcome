import face_recognition
import cv2
import sys
import os
from tkinter import *

from PIL import ImageTk, Image

try:
root = Tk()
startingX=20
startingY=20
root.title('Technology Festival 2019')
root.geometry('650x550') # Size 200, 200
#root.configure(background='white')

versiontitle = Label(root, text="School Visitor Information Check")
versiontitle.pack()
versiontitle.config(font=("Courier", 20))
versiontitle.config(bg='black', fg='white')  
versiontitle.place(x=startingX,y=2)

errorLabel = Label(root, text="Record doesn't exist. Please publish the record.")


path = "school_image.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "no")

firstNameLabel = Label(root, text=" First Name ")
firstNameLabel.pack()
firstNameLabel.place(x=startingX,y=startingY+40)

firstName = StringVar()
entryfirstname = Entry(textvariable=firstName)
entryfirstname.pack()
entryfirstname.place(x=startingX+100,y=startingY+40)

lastNameLabel = Label(root, text=" Last Name ")
lastNameLabel.pack()
lastNameLabel.place(x=startingX,y=startingY+80)

lastName = StringVar()
entrylastname = Entry(textvariable=lastName)
entrylastname.pack()
entrylastname.place(x=startingX+100,y=startingY+80)

brithNameLabel = Label(root, text="Birth Date")
brithNameLabel.pack()
brithNameLabel.place(x=startingX,y=startingY+120)

birthYear = StringVar( value='Year')
brithentry = Entry(textvariable=birthYear)
brithentry.pack()
brithentry.place(x=startingX+100,y=startingY+120)


month = StringVar(root)

# Dictionary with options
monthChoices = {'12.Dec','11.Nov','10.Oct','09.Sep','08.Aug','07.July','06.Jun','05.May','04.Apr','03.Mar','02.Feb','01.Jan'}
month.set('Month') # set the default option

monthMenu = OptionMenu(root, month, *sorted(monthChoices))
monthMenu.pack()
monthMenu.place(x=startingX+240,y=startingY+120)

day = StringVar(root)

# Dictionary with options
dayChoices = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
day.set('Day') # set the default option

dayMenu = OptionMenu(root, day, *dayChoices)
dayMenu.pack()
dayMenu.place(x=startingX+340,y=startingY+120)

uname = str(entryfirstname)

flb=""
def publishRecord():
global flb
print("publishing ...")
hideLabel = Label(root, text="                                                                                                 ")
hideLabel.pack()
hideLabel.config(font=("",12))
hideLabel.config(fg='white')  
hideLabel.place(x=2,y=260)

flb = firstName.get() +"_"+ lastName.get() +"_"+ month.get()+day.get()
print("Identifier:"+flb)

camera_port = 0
camera = cv2.VideoCapture(camera_port)
ramp_frames=7
#camera.set(3, 1280)
#camera.set(4, 720)

for i in range(ramp_frames):
temp = camera.read()

#time.sleep(3)
return_value, image = camera.read()
cv2.imwrite(flb+".png", image)
del(camera)

imgName = flb+".png"

print("using OS this time : "+imgName)
#capturedImg = Image.open(imgName)
#capturedImg.show()
os.startfile(imgName)

def recognize_face( uname ):
print("  ")


def checkIfPublishedUser():
hideLabel = Label(root, text="                                                                                                 ")
hideLabel.pack()
hideLabel.config(font=("",12))
hideLabel.config(fg='white')  
hideLabel.place(x=2,y=270)
flb = firstName.get() +"_"+ lastName.get() +"_"+ month.get()+day.get()
try:
user_image = face_recognition.load_image_file(flb+".png")
user_encoding = face_recognition.face_encodings(user_image)[0]
check()
except:
errorLabel = Label(root, text="Record doesn't exist. Please publish the record.")
errorLabel.pack()
errorLabel.config(font=("",12))
errorLabel.config(fg='red')  
errorLabel.place(x=2,y=260)
print("User doesn't exist")

def check():
global flb
#hideLabel = Label(root, text="                                                                                                 ")
#hideLabel.pack()
#hideLabel.config(font=("",12))
#hideLabel.config(fg='white')  
#hideLabel.place(x=2,y=270)

flb = firstName.get() +"_"+ lastName.get() +"_"+ month.get()+day.get()
print("")
print("press s to stop")
video_capture = cv2.VideoCapture(0)

#def pub():
# print("sorry, you have to click republish first.")

user_image = face_recognition.load_image_file(flb+".png")
user_encoding = face_recognition.face_encodings(user_image)[0]

known_face_encodings = [user_encoding]

known_face_names = [firstName.get() +" "+ lastName.get()]

face_locations = []

face_encodings = []

face_names = []

process_this_frame = True
while True:
# Grab a frame of the video
ret, frame = video_capture.read()

# Resize frame of video to smaller size for faster  processing
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
rgb_small_frame = small_frame[:, :, ::-1]

# Only process every other frame of video to save time
if process_this_frame:
# Find all the faces and face encodings in the current frame of video
face_locations = face_recognition.face_locations(rgb_small_frame)
face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

face_names = []
for face_encoding in face_encodings:
# See if the face is a match for the known face(s)
matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
name = "Unknown"

# If a match was found in known_face_encodings, just use the first one.
if True in matches:
first_match_index = matches.index(True)
name = known_face_names[first_match_index]

face_names.append(name)

process_this_frame = not process_this_frame


# Display the results
for (top, right, bottom, left), name in zip(face_locations, face_names):
# Scale back up face locations since the frame we detected in was scaled to 1/4 size
top *= 4
right *= 4
bottom *= 4
left *= 4

# Draw a box around the face
cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

# Draw a label with a name below the face
cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# Display the resulting image
cv2.imshow('Video', frame)

# Hit 'q' on the keyboard to quit!
if cv2.waitKey(1) & 0xFF == ord('s') :
break

video_capture.release()

cv2.destroyAllWindows()

checkButton = Button(text='Check', command=checkIfPublishedUser)
checkButton.pack()
checkButton.place(x=startingX,y=startingY+200)

publishButton = Button(text='Publish', command=publishRecord)
publishButton.pack()
publishButton.place(x=startingX+70,y=startingY+200)

quitButton = Button(text='Quit', command=quit)
quitButton.pack()
quitButton.place(x=startingX+150,y=startingY+200)

root.mainloop()
except:
print(" Exception ")