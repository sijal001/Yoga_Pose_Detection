import numpy as np
import mediapipe as mp
#mp_pose_lm = mp.solutions.pose

ANGLE_KEYS = [
    '0.11/12.23/24', '0.11.23', '0.12.24', # Nose to torso
    '11.23.-23', '12.24.-24', '11/12.23/24.-23/24',  # Torso to horizontal
    '12.11.13', '23.11.13', '23.11.12',  # Left shoulder ()
    '11.12.14', '24.12.14', '24.12.11',  # right shoulder # left elbow
    '11.13.15', '12.14.16',  # both elbows
    '11.23.25', '11.23.24', '25.23.24',  # left hip
    '12.24.26', '12.24.23', '26.24.23',  # right hip
    '23.25.27', '24.26.28',  # both knees
    '28.24.16', '27.23.15',  # wrist-hip-ankle
]


def calc_angle_from_2d_coords(a, b, c, full_circle=True):
    """:param

    """
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if not full_circle:
        if angle > 180.0:
            angle = 360 - angle

    return angle


def transform_landmarks(landmarks) -> dict:
    """
        landmarks come from the mediapipeline processing from an image and should look something like follows:
            results = MP_POSE.process(image)
            landmarks = results.pose_landmarks.landmark
    """

    landmark_dict = {}
    mp_pose_lm = mp.solutions.pose.PoseLandmark

    # Nose
    landmark_dict['0'] = [landmarks[mp_pose_lm.NOSE.value].x,
                          landmarks[mp_pose_lm.NOSE.value].y]
    # Shoulders
    landmark_dict['11'] = [landmarks[mp_pose_lm.LEFT_SHOULDER.value].x,
                           landmarks[mp_pose_lm.LEFT_SHOULDER.value].y]
    landmark_dict['12'] = [landmarks[mp_pose_lm.RIGHT_SHOULDER.value].x,
                           landmarks[mp_pose_lm.RIGHT_SHOULDER.value].y]
    # Sternum
    landmark_dict['11/12'] = (np.array(landmark_dict['11']) + np.array(landmark_dict['12'])) / 2
    # Elbows
    landmark_dict['13'] = [landmarks[mp_pose_lm.LEFT_ELBOW.value].x,
                           landmarks[mp_pose_lm.LEFT_ELBOW.value].y]
    landmark_dict['14'] = [landmarks[mp_pose_lm.RIGHT_ELBOW.value].x,
                           landmarks[mp_pose_lm.RIGHT_ELBOW.value].y]
    # Wrists
    landmark_dict['15'] = [landmarks[mp_pose_lm.LEFT_WRIST.value].x,
                           landmarks[mp_pose_lm.LEFT_WRIST.value].y]
    landmark_dict['16'] = [landmarks[mp_pose_lm.RIGHT_WRIST.value].x,
                           landmarks[mp_pose_lm.RIGHT_WRIST.value].y]
    # Hips
    landmark_dict['23'] = [landmarks[mp_pose_lm.LEFT_HIP.value].x,
                           landmarks[mp_pose_lm.LEFT_HIP.value].y]
    landmark_dict['24'] = [landmarks[mp_pose_lm.RIGHT_HIP.value].x,
                           landmarks[mp_pose_lm.RIGHT_HIP.value].y]
    # Pubic Bone
    landmark_dict['23/24'] = (np.array(landmark_dict['23']) + np.array(landmark_dict['24'])) / 2

    # Knees
    landmark_dict['25'] = [landmarks[mp_pose_lm.LEFT_KNEE.value].x,
                           landmarks[mp_pose_lm.LEFT_KNEE.value].y]
    landmark_dict['26'] = [landmarks[mp_pose_lm.RIGHT_KNEE.value].x,
                           landmarks[mp_pose_lm.RIGHT_KNEE.value].y]
    # Ankles
    landmark_dict['27'] = [landmarks[mp_pose_lm.LEFT_ANKLE.value].x,
                           landmarks[mp_pose_lm.LEFT_ANKLE.value].y]
    landmark_dict['28'] = [landmarks[mp_pose_lm.RIGHT_ANKLE.value].x,
                           landmarks[mp_pose_lm.RIGHT_ANKLE.value].y]
    # Horizontals points from the hip
    landmark_dict['-23'] = [landmarks[mp_pose_lm.LEFT_HIP.value].x + 1,
                            landmarks[mp_pose_lm.LEFT_HIP.value].y]
    landmark_dict['-24'] = [landmarks[mp_pose_lm.RIGHT_HIP.value].x + 1,
                            landmarks[mp_pose_lm.RIGHT_HIP.value].y]
    landmark_dict['-23/24'] = (np.array(landmark_dict['-23']) + np.array(landmark_dict['-24'])) / 2
    return landmark_dict

def calc_angles_from_landmarks(results, dictionary=False, full_circle=True) -> dict:
    """
                results = MP_POSE.process(image)
                landmarks = results.pose_landmarks.landmark
        """
    try:
        landmarks = results.pose_landmarks.landmark
    except:
        import time
        time.sleep(20)
    landmark_dict = transform_landmarks(landmarks)
    if dictionary:
        angles = {}
    else:
        angles = []

    for key in ANGLE_KEYS:
        a, b, c = (landmark_dict[number] for number in key.split('.'))
        angle = calc_angle_from_2d_coords(a, b, c, full_circle=full_circle)
        if dictionary:
            angles[key] = angle
        else:
            angles.append(angle)

    return angles
