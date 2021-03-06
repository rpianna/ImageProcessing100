import cv2
import numpy as np


def conv_BGR2gray(img):
    """BGR画像をグレー画像に変換します。

    Arguments:
        img {numpy.ndarray} -- BGR画像

    Returns:
        [numpy.ndarray] -- グレー画像

    Notes:
        ndarrayのdtypeは入力画像と同じものを返します。
    """

    r = img[:, :, 2].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 0].copy()

    return np.array(0.2126 * r + 0.7152 * g + 0.0722 * b, dtype="uint8")


def _main():  # pragma: no cover
    img = cv2.imread(r"img/imori.jpg")

    gray_img = conv_BGR2gray(img)

    cv2.imshow("result", gray_img)
    cv2.waitKey(0)

    cv2.imwrite(r"img/answer_2.jpg", gray_img)

if __name__ == "__main__":  # pragma: no cover
    _main()
