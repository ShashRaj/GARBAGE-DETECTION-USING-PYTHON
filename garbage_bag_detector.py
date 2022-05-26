import cv2 as cv

###################################################

path = r"C:\Users\KIIT\PycharmProjects\pythonProject\venv\garbage_cascade.xml"
#cameraNo = 1
objectName = 'Garbage bag'
frameWidth = 640
frameHeight = 480
color = (255, 0, 255)

################## Capturing Video ###################

cap = cv.VideoCapture(0)
address = "http://192.168.43.1:4747/video"
cap.open(address)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

########### Trackbar ################################

cv.namedWindow("Result")
cv.resizeWindow("Result", frameWidth, frameHeight+100)
cv.createTrackbar("Scale", "Result", 400, 1000, empty)
cv.createTrackbar("Neighbour", "Result", 8, 20, empty)
cv.createTrackbar("Min Area", "Result", 0, 100000, empty)
cv.createTrackbar("Brightness", "Result", 180, 255, empty)

############# Load the classifier ####################

cascade = cv.CascadeClassifier(path)

while True:
    # Set camera brightness from trackbar
    cameraBrightness = cv.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)

    # Get image from camera and convert it to grayscale
    success, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Detecting the object using cascade
    scaleVal = 1 + (cv.getTrackbarPos("Scale", "Result")/1000)
    neig = cv.getTrackbarPos("Neighbour", "Result")
    objects = cascade.detectMultiScale(gray, scaleVal, neig)

    # Displaying the detected object
    for (x, y, w, h) in objects:
        area = w*h
        minArea = cv.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            cv.rectangle(img, (x, y), (x+w, y+h), color, 3)
            cv.putText(img, objectName, (x, y-5), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            roi_color = img[y:y+h, x:x+w]

cv.imshow("Result", img)
#cv.waitKey(1)

#cv.waitKey(0)
if cv.waitKey(1) & 0xFF == ord('q'):
    sys.exit()

