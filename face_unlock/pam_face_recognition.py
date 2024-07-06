import face_recognition
import cv2
import pickle
import os
import pam

def pam_sm_authenticate(pamh, flags, argv):
    try:
        with open(os.path.expanduser("~/.face_unlock/known_face.dat"), "rb") as f:
            known_face_encoding = pickle.load(f)

        video_capture = cv2.VideoCapture(0)
        print("Looking at the camera for face authentication.")
        
        for _ in range(100):
            ret, frame = video_capture.read()
            rgb_frame = frame[:, :, ::-1]
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
                if True in matches:
                    print("Face recognized. Authentication successful.")
                    video_capture.release()
                    return pamh.PAM_SUCCESS

        video_capture.release()
        print("Face not recognized. Falling back to password authentication.")
        return pam.pam().authenticate(pamh.user, pamh.authtok)
    except Exception as e:
        print("Error during authentication:", e)
        return pam.pam().authenticate(pamh.user, pamh.authtok)

def pam_sm_setcred(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
    return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
    return pamh.PAM_SUCCESS
