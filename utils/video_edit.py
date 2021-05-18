from os.path import isfile, join
import os
import cv2


def convert_frames_to_video(pathIn, pathOut, fps, reverse=False):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    try:
        files.sort(key=lambda x: int(x[5:-4]))
    except:
        pass
    for i in range(len(files)):
        filename = pathIn + files[i]
        # reading each files
        img = cv2.imread(filename)
        if reverse:
            img = cv2.flip(img, 1)
        height, width, layers = img.shape
        size = (width, height)
        # print(filename)
        # inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

'''if __name__ == '__main__':
'''