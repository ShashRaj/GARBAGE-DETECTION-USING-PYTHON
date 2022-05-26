# server script
import socket
import cv2
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.0.115', 10000))
hostname = socket.gethostname()
s.listen(2)
connection, client = s.accept()
    objectName = 'Garbage Bag'
    color = (255, 0, 255)
    cascPath = r"C:\Users\KIIT\PycharmProjects\pythonProject\venv\garbage_cascade.xml"
    garbageCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)
    address = "http://192.168.43.1:4747/video"
    video_capture.open(address)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        bags = garbageCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Draw a rectangle around the bag
        for (x, y, w, h) in bags:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, objectName, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    gpsdata = client.recv
    file = open("file2", "w")
    file.write(gpsdata())
    file.close()
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
