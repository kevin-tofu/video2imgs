'''
@author : Kohei Watanabe
@contact : koheitech001[at]gmail.com
'''

import os
import shutil
import cv2

def make_directory(path):
    print(path)

    if os.path.exists(path):
        os.makedirs(path)
    else:
        #os.rmdir(path)
        #shutil.rmtree(path)
        pass

def remove_files(directory):
    if os.path.exists(directory) == True:
        shutil.rmtree(directory)
    
def save_all_frames(video_path, dir_path, basename, digit, ext='jpg'):

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    
    remove_files(dir_path)
    make_directory(dir_path)
    base_path = os.path.join(dir_path, basename)

    loop = 0
    while True:
        print(loop)
        ret, frame = cap.read()
        if ret:
            fname = '{}{}.{}'.format(base_path, str(loop).zfill(digit), ext)
            print(fname)
            cv2.imwrite(fname, frame)
            loop += 1
        else:
            return

if __name__ == '__main__':

    import argparse
    print("start")

    parser = argparse.ArgumentParser()
    parser.add_argument('--video', '-V', type=str, default='video.mp4', help='')
    parser.add_argument('--dir_image', '-D', type=str, default='./images', help='')
    parser.add_argument('--basename', '-BN', type=str, default='', help='')
    parser.add_argument('--digit', '-DG', type=int, default=8, help='')
    parser.add_argument('--fmt', '-F', type=str, default='jpg', help='')

    args = parser.parse_args()

    save_all_frames(args.video, args.dir_image, args.basename, args.digit, ext=args.fmt)

    print("end")