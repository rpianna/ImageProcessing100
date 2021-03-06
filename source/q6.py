import cv2
import numpy as np


def apply_color_reduction(bgr_img):
    """減色処理を適用します。

    Arguments:
        bgr_img {numpy.ndarray} -- BGR画像（3ch）

    Returns:
        numpy.ndarray -- 処理後のBGR画像（3ch）

    Notes:
        入力はRGB画像でも正常に動作します。
    """

    out_img = bgr_img.copy()
    out_img[(0 <= out_img) & (out_img < 63)] = 32
    out_img[(63 <= out_img) & (out_img < 127)] = 96
    out_img[(127 <= out_img) & (out_img < 191)] = 160
    out_img[(191 <= out_img) & (out_img < 256)] = 224

    return out_img


def _main():  # pragma: no cover
    img = cv2.imread(r"img/imori.jpg")

    img = apply_color_reduction(img)

    cv2.imshow("result", img)
    cv2.waitKey(0)

    cv2.imwrite(r"img/answer_6.jpg", img)

if __name__ == "__main__":  # pragma: no cover
    _main()
