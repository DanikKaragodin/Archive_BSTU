import idx2numpy
import numpy as np

def read_idxfile(path):
    images = idx2numpy.convert_from_file(path)
    # images = np.array(list(map(lambda x: x.flatten(), images)))
    return images

def get_labels(labels):
    return np.array(list(map(
            lambda el: [0 if x != el else 1 for x in range(10)], labels
    )))

if __name__ == '__main__':
    import cv2


    images = read_idxfile("train-images.idx3-ubyte")

    cv2.imshow("Image", images[4])
    cv2.waitKey(0)
