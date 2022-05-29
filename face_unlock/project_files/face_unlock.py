# !pip install face_recognition opencv-python
import cv2
import face_recognition
cam = cv2.VideoCapture(0)

def face_recog(imgSys, test_image):
    # copy the images
    img = imgSys.copy()
    imgTest = test_image.copy()

    # encoding the list face encodings
    encodeImg = face_recognition.face_encodings(img)[0]

    # getting list of all the faces and encodings
    encodeTest = face_recognition.face_encodings(imgTest)
    
    # searching all faces one by one
    for i in range(len(encodeTest)):
        #comparing faces
        result = face_recognition.compare_faces([encodeImg],encodeTest[i])
        
        if result[0] is True:
            return True
    return False 

def face_recog_start():
    imgSys = face_recognition.load_image_file('./photo.jpeg')
    result, imgCam = cam.read()
    return face_recog(imgSys, imgCam)