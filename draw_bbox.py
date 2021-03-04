import cv2
import os

file_name = "images/1613635278594.jpg"

annotations = [{"label":"dad", "bbox":(450, 100, 920, 950)}, {"label":"mam", "bbox":(1080, 90, 1575, 825)}]

def draw_bbox(img, left_top, right_bottom, color = (0, 0, 0), label = None):
    fontFace = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.rectangle(img, left_top, right_bottom, color, thickness = 1)
    retval, baseLine = cv2.getTextSize(label, fontFace, 8, 1)
    cv2.putText(img, label, left_top, fontFace, 1, color)


def main():
    img = cv2.imread(file_name)
    out_file_name = os.path.splitext(file_name)[0] + "_out.jpg"

    for anno in annotations:
        left, top, right, bottom = anno["bbox"]
        draw_bbox(img, (left, top), (right, bottom), color = (128, 128, 0), label = anno["label"])

    cv2.imwrite(out_file_name, img)
    
if __name__=="__main__":
    main()