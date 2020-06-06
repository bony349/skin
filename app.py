import PIL
import numpy

from helper import *
from flask import Flask, request, render_template

app = Flask(__name__)
from PIL import Image

svm_model = load_model('SVM.sav')
@app.route('/')
def index():
    new_test = []  # new images

    pil_image = PIL.Image.open("AUG_0_0.jpeg").convert('RGB')
    open_cv_image = numpy.array(pil_image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    resized_img = resize(open_cv_image, (128, 64))

    fd_img, hog_img = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True,
                          multichannel=True)
    new_test.append(fd_img)
    ############################################
    svm_model = load_model('SVM.sav')
    prediction = svm_model.predict(new_test)
    if (prediction == 0):
        return ("Skin Disease is vitiligo")
    elif (prediction == 1):
        return ("Mario Has Deployeeed and this prediction is Psoriasis ")
    elif (prediction == 2):
        return ("Skin Disease is melanoma")


@app.route('/RequestImageWithMetadata', methods=['POST'])
def post():
    new_test = []

    imagefile = request.files.get('imagefile', '')
    pil_image = PIL.Image.open(imagefile).convert('RGB')
    open_cv_image = numpy.array(pil_image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    resized_img = resize(open_cv_image,(128,64))

    fd_img, hog_img = hog(resized_img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True,
                          multichannel=True)
    new_test.append(fd_img)


    prediction = svm_model.predict(new_test)
    if (prediction == 0):
        return ("Skin Disease is vitiligo")
    elif (prediction == 1):
        return ("Skin Diseas is Psoriasis ")
    elif (prediction == 2):
        return ("Skin Disease is melanoma")


if __name__ == '__main__':
    app.run()
