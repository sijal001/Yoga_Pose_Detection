import os
from utils.ml import pose_detection

training_pose = os.listdir('.\\pose_recognition_data\\training data\\training frames\\videos')
for pose in training_pose:
    print(pose)

    pose_detection(
        video_path=f'.\\pose_recognition_data\\training data\\training frames\\videos\\{pose}',
        train=True,
        class_name=f"{pose[:-4]}")