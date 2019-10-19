import cv2
import numpy as np
import sys

# You should replace these 3 lines with the output in calibration step
DIM=(640, 480)
K=np.array([[315.7567614147568, 0.0, 325.2083937909489], [0.0, 314.863821615827, 236.03070258095818], [0.0, 0.0, 1.0]])
D=np.array([[0.013587199812888646], [-0.14484457345521587], [0.17909595106791984], [-0.08317093662848575]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)