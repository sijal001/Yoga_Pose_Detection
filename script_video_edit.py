from os.path import isfile, join
import os
import cv2

from utils.video_edit import convert_frames_to_video

poses = os.listdir(r"pose_recognition_data/training data/training frames/")
for fol in ['.DS_Store', 'videos', "Andrea's Cat"]:
    try:
        poses.remove(fol)
    except:
        print('except: ', fol)
for pose in poses:
    print(pose)
    # try:
    pathIn = f'./pose_recognition_data/training data/training frames/{pose}/'
    pathOut = f'./pose_recognition_data/training data/training frames/videos/{pose}.avi'
    pathOutReversed = f'./pose_recognition_data/training data/training frames/videos/{pose}_reversed.avi'
    fps = 0.25
    convert_frames_to_video(pathIn, pathOut, fps)
    convert_frames_to_video(pathIn, pathOutReversed, fps, reverse=True)