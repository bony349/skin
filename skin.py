from helper import *
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    new_test = []  # new images
    img = cv2.imread("psoriasis.jpg")
    resized_img = cv2.resize(img, (128, 64))
    fd_img, hog_img = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True,
                          multichannel=True)
    new_test.append(fd_img)
    ############################################
    svm_model = load_model('SVM.sav')
    prediction = svm_model.predict(new_test)
    if (prediction == 0):
        return ("Skin Disease is vitiligo")
    elif (prediction == 1):
        return ("Mario Has Deployed ")
    elif (prediction == 2):
        return ("Skin Disease is melanoma")


if __name__ == '__main__':
    app.run()

