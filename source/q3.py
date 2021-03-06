import cv2
import numpy as np
import q2


def conv_BGR2binary(img, threshold: int):
    """BGR画像をしきい値に応じて2値画像に変換します。

    Arguments:
        img {numpy.ndarray} -- BGR画像
        threshold {[type]} -- しきい値（0～255）

    Returns:
        numpy.ndarray -- 2値画像（1ch）

    Notes:
        ndarrayのdtypeは入力画像と同じものを返します。
    """

    gray_img = q2.conv_BGR2gray(img)

    gray_img[gray_img < threshold] = 0
    gray_img[gray_img >= threshold] = 255

    return gray_img

def _main():  # pragma: no cover
    img = cv2.imread(r"img/imori.jpg")

    binary_img = conv_BGR2binary(img, 128)

    cv2.imshow("result", binary_img)
    cv2.waitKey(0)

    cv2.imwrite(r"img/answer_3.jpg", binary_img)

if __name__ == "__main__":  # pragma: no cover
    _main()
