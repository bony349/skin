from helper import *
from flask import Flask
app = Flask(__name__)
from PIL import Image

@app.route('/')
def index():
    new_test = []  # new images
    img = Image.open('psoriasis.jpg')
    resized_img = resize(img, (128, 64))
    fd_img, hog_img = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True,
                          multichannel=True)
    new_test.append(fd_img)
    ############################################
    svm_model = load_model('SVM.sav')
    prediction = svm_model.predict(new_test)
    if (prediction == 0):
        return ("Skin Disease is vitiligo")
    elif (prediction == 1):
        return ("Deployed ")
    elif (prediction == 2):
        return ("Skin Disease is melanoma")


if __name__ == '__main__':
    app.run()

