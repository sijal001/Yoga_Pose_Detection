import cv2
import mediapipe as mp
import numpy as np
from time import sleep
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

from glob import glob
import os
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders
directory = 'C:\\Users\\simon\\PycharmProjects\\yoga_gesture_detection\\pose_recognition_data\\training data\\training frames'
folders = fast_scandir(directory)[:2] + fast_scandir(directory)[4:]
poses = [pose.split('- ')[1] for pose in folders]
data = []

angle_keys = [
    '0.11-12.23-24',  # Nose to torso
    '12.11.13', '23.11.13', '23.11.12',  # Left shoulder ()
    '11.12.14', '24.12.14', '24.12.11',  # right shoulder # left elbow
    '11.13.15', '12.14.16',  # both elbows
    '11.23.25', '11.23.24', '25.23.24',  # left hip
    '12.24.26', '12.24.23', '26.24.23',  # right hip
    '23.25.27', '24.26.28',  # both knees
    '28.24.16', '27.23.15',  # wrist-hip-ankle
]
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as MP_POSE:
    for folder in folders:
        pose = folder.split('- ')[1]
        paths = glob(folders[0] + '/*')
        for path in paths:
            print(path.split('training frames')[1])
            imaage = cv2.imread(path)
            # Recolor image to RGB
            image = cv2.cvtColor(imaage, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = MP_POSE.process(image)
            landmarks = results.pose_landmarks.landmark
            landmark_dict = {}

            # Nose
            landmark_dict['0'] = [landmarks[mp_pose.PoseLandmark.NOSE.value].x,
                                  landmarks[mp_pose.PoseLandmark.NOSE.value].y]
            # Shoulders
            landmark_dict['11'] = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            landmark_dict['12'] = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            # Sternum
            landmark_dict['11-12'] = (np.array(landmark_dict['11']) + np.array(landmark_dict['12'])) / 2
            # Elbows
            landmark_dict['13'] = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            landmark_dict['14'] = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            # Wrists
            landmark_dict['15'] = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            landmark_dict['16'] = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            # Hips
            landmark_dict['23'] = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            landmark_dict['24'] = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
            # Pubic Bone
            landmark_dict['23-24'] = (np.array(landmark_dict['23']) + np.array(landmark_dict['24'])) / 2

            # Knees
            landmark_dict['25'] = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            landmark_dict['26'] = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            # Ankles
            landmark_dict['27'] = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                   landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            landmark_dict['28'] = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
            angles = {}

            for key in angle_keys:
                a, b, c = [landmark_dict[number] for number in key.split('.')]
                angles[key] = calculate_angle(a, b, c)
            angles['pose'] = pose
            data.append(angles)

print(data)
print(len(data))