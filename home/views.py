from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
#from .forms import *
from django.core.files.storage import default_storage
import tensorflow as tf
import cv2
import numpy as np
import os


@csrf_exempt

@csrf_protect


def index(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render())
def test(request):
    template=loader.get_template("test.html")
    return HttpResponse(template.render())

def about(request):
    template=loader.get_template("about.html")
    return HttpResponse(template.render())

def kidney(request):
    template=loader.get_template("kidney_stone_and_can.html")
    return HttpResponse(template.render())

def pnemonia(request):
    template=loader.get_template("pnemonia.html")
    return HttpResponse(template.render())

def malaria(request):
    template=loader.get_template("malaria.html")
    return HttpResponse(template.render())

def skin_cancer(request):
    template=loader.get_template("skin_cancer.html")
    return HttpResponse(template.render())

def tb(request):
    template=loader.get_template("tb.html")
    return HttpResponse(template.render())
test_data=[]
tb_mod = tf.keras.models.load_model('./tb_model1')
skin_mod = tf.keras.models.load_model('./skin_cancer_model')
kidney_mod = tf.keras.models.load_model('./kidney_model')
pnemonia_mod = tf.keras.models.load_model('./pnemonia_model')
maleria_mod = tf.keras.models.load_model('./maleria_model')

def loading():
    image = './media/pic.jpg'
    img = cv2.imread(image)
    print('img', img)
    img = cv2.resize(img, (28, 28))
    if img.shape[2] == 1:
        img = np.dstack([img, img, img])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img)
    img = img / 255
    test_data.append(img)

    # Convert the list into numpy arrays

    test_data1 = np.array(test_data)
    print(test_data1.shape)
    return test_data1
response={}
def tb_result(request):
    if request.method == "POST":
        f = request.FILES['tbfile']  # here you get the files needed

        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        test_data1=loading()
        # Check its architecture
        #new_model.summary()
        a = tb_mod.predict(np.array(test_data1))
        ans=np.argmax(a)
        print('anser',ans)
        os.remove("./media/pic.jpg")
        if ans==0:
            response='no diseases'
        else:
            response='yes u have tb'
        print('response',response)
        #context = {'response': response}
        return render(request, 'tb_result.html', {'response': response})

    else:
        return render(request, 'tb_result.html',)

def skin_result(request):
    if request.method == "POST":
        f = request.FILES['skinfile']  # here you get the files needed

        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        test_data1=loading()
        # Check its architecture
        #new_model.summary()
        a = skin_mod.predict(np.array(test_data1))
        ans=np.argmax(a)
        print('anser',ans)
        os.remove("./media/pic.jpg")
        if ans==0:
            response='you have affected Actinic_keratosis'
        elif ans==1:
            response='you have affected basal cell carcinoma'
        elif ans==2:
            response='you have affected dermatofibroma'
        elif ans==3:
            response='you have affected melanoma'
        elif ans==4:
            response='you have affected nevus'
        elif ans==5:
            response='you have affected pigmented benign keratosis'
        elif ans==6:
            response='you have affected seborrheic keratosis'
        else:
            response='you have affected squamous cell carcinoma'

        print('response',response)
        #context = {'response': response}
        return render(request, 'skin_result.html', {'response': response})

    else:
        return render(request, 'skin_result.html',)

def kidney_result(request):
    if request.method == "POST":
        f = request.FILES['kidneyfile']  # here you get the files needed

        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        test_data1=loading()
        # Check its architecture
        #new_model.summary()
        a = kidney_mod.predict(np.array(test_data1))
        ans=np.argmax(a)
        print('anser',ans)
        os.remove("./media/pic.jpg")
        if ans==0:
            response='you affected with Cyst'
        elif ans==1:
            response='you are safe ,nothing to worry'
        elif ans==2:
            response='you affected with Stone'
        else:
            response='you affected with Tumor'
        print('response',response)
        #context = {'response': response}
        return render(request, 'kideney_result.html', {'response': response})

    else:
        return render(request, 'kideney_result.html',)

def pnemonia_result(request):
    if request.method == "POST":
        f = request.FILES['pnemoniafile']  # here you get the files needed

        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        test_data1=loading()
        # Check its architecture
        #new_model.summary()
        a = pnemonia_mod.predict(np.array(test_data1))
        ans=np.argmax(a)
        print('anser',ans)
        os.remove("./media/pic.jpg")
        if ans==0:
            response='no diseases'
        else:
            response='yes u have pneumonia '
        print('response',response)
        #context = {'response': response}
        return render(request, 'pnenonia_result.html', {'response': response})

    else:
        return render(request, 'pnenonia_result.html',)

def maleria_result(request):
    if request.method == "POST":
        f = request.FILES['maleriafile']  # here you get the files needed

        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        test_data1=loading()
        # Check its architecture
        #new_model.summary()
        a = maleria_mod.predict(np.array(test_data1))
        ans=np.argmax(a)
        print('anser',ans)
        os.remove("./media/pic.jpg")
        if ans==0:
            response='no diseases'
        else:
            response='yes u have maleria'
        print('response',response)
        #context = {'response': response}
        return render(request, 'maleria_result.html', {'response': response})

    else:
        return render(request, 'maleria_result.html',)