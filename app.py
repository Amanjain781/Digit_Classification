import warnings
warnings.filterwarnings('ignore')
import numpy as np
from PIL import Image,ImageEnhance
import os
import cv2 as cv
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
#from win32com.client import Dispatch

# for gpu use
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
'''
def speak(text):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(text)
    
model = load_model('model.h5')
'''
def preprocessing(img):
    try:
        img = img.astype('uint8')
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.equalizeHist(img)
        img = img/255
        return img
    except Exception as e:
        img =img.astype('uint8')
        img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.equalizeHist(img)
        img = img/255
        return img 


   
def main():
    st.title("Digit Classification Apps Using CNN")
    st.write("Build  with streamlit, keras, Tensorflow & python")
    st.set_option('deprecation.showfileUploaderEncoding',False)
    activities = ["Classification","About"]
    choices = st.sidebar.selectbox("Select Activities",activities)
    if choices=="Classification":
        st.subheader("Digit Classification")
        img_file =st.file_uploader("Upload_file",type=["png","jpg","jpeg"])
        if img_file is not None:
            up_img = Image.open(img_file)
            st.image(up_img)
        if st.button("Process"):
            try:
                img = np.asarray(up_img)
                img = cv.resize(img, (28,28))
                img = preprocessing(img)
                img = img.reshape(1,28,28,1)
                pred = model.predict(img)
                classIndex = model.predict_classes(img)
                prob_value = np.amax(pred)
                if prob_value  > 0.90:
                    if classIndex == 0:
                        st.success("ZERO")
                        #speak("Predicted Number is ZERO")
                    elif classIndex == 1:
                        st.success("ONE")
                        #speak("Predicted Number is ONE")
                    elif classIndex == 2:
                        st.success("TWO")
                        #speak("Predicted Number is TWO")
                    elif classIndex == 3:
                        st.success("THREE")
                        #speak("Predicted Number is THREE")
                    elif classIndex == 4:
                        st.success("FOUR")
                        #speak("Predicted Number is FOUR")
                    elif classIndex == 5:
                        st.success("FIVE")
                        #speak("Predicted Number is FIVE")
                    elif classIndex == 6:
                        st.success("SIX")
                        #speak("Predicted Number is SIX")
                    elif classIndex == 7:
                        st.success("SEVEN")
                        #speak("Predicted Number is SEVEN")
                    elif classIndex == 8:
                        st.success("EIGHT")
                        #speak("Predicted Number is EIGHT")
                    elif classIndex == 9:
                        st.success("NINE")
                        #speak("Predicted Number is NINE")
            except Exception as e:
                st.error("Connection Problem, Refresh Again")
                
    elif choices == "About":
            st.write("This Application is Developed By Aman Jain")
            
            
if __name__ =="__main__" :
    main()
                    
                        
                
                
                
                
