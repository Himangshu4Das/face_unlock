import cv2
import face_recognition
import pickle
import os

def capture_face():
    video_capture = cv2.VideoCapture(0)
    print("Capturing your face. Please look at the camera.")

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            os.makedirs(os.path.expanduser("~/.face_unlock"), exist_ok=True)
            with open(os.path.expanduser("~/.face_unlock/known_face.dat"), "wb") as f:
                pickle.dump(face_encoding, f)
            print("Face captured and encoding saved.")
            break

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()