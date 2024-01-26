import streamlit as st
import cv2,requests,os,base64,json
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from io import BytesIO
import tensorflow as tf
import tensorflow_hub as hub

dir_name=os.path.dirname(__file__)
saved_model_path=os.path.join(dir_name,"saved models")
saved_model_path=os.path.join(saved_model_path,"saved models")
img_path=os.path.join(dir_name,"image.png")

def run(image_url,model_name,st_image,st_text):
    if type(image_url)==str:
        if image_url.startswith("data"):
            _,encoded_data=image_url.split(",",1)
            decoded_data=base64.b64decode(encoded_data)
            # Convert the binary data to an image
            img=Image.open(BytesIO(decoded_data))
            np_img=np.array(img)
            np_img=cv2.resize(np_img,(224,224),interpolation=cv2.INTER_NEAREST)
            img_array_expanded=np.expand_dims(np_img,axis=0)
            img_array_expanded=img_array_expanded/255.
            model,description,class_label=get_model(model_name)
            prediction,predicted=make_predictions(model,img_array_expanded,class_label)
            st_image.image(np_img)
            st_text.text(str(predicted)+"__"+str(prediction))
        elif image_url.startswith("http"):
            response=requests.get(image_url)
            if response.status_code==200:
                img = np.frombuffer(response.content, np.uint8)
                img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                np_img=cv2.resize(img,(224,224),interpolation=cv2.INTER_NEAREST)
                img_array_expanded=np.expand_dims(np_img,axis=0)
                img_array_expanded=img_array_expanded/255.
                model,description,class_label=get_model(model_name)
                prediction,predicted=make_predictions(model,img_array_expanded,class_label)
                st_image.image(np_img)
                st_text.text(str(predicted)+"__"+str(prediction))
            else:
                st_text.text("cannot access url")
        else:
            st.error('This is an error there is problem with url pass url starting with data or http only')
    else:
        
        bytes_data = image_url.getvalue()
        img=Image.open(BytesIO(bytes_data))
        np_img=np.array(img)
        np_img=cv2.resize(np_img,(224,224),interpolation=cv2.INTER_NEAREST)
        img_array_expanded=np.expand_dims(np_img,axis=0)
        img_array_expanded=img_array_expanded/255.
        
        model,description,class_label=get_model(model_name)
        prediction,predicted=make_predictions(model,img_array_expanded,class_label)
        st_image.image(np_img)
        st_text.text(str(predicted)+"__"+str(prediction))
def  get_model(name,model_path=saved_model_path):
    folder=os.path.join(model_path,name)
    descri_label_path=os.path.join(folder,"description.json")
    
    with open (descri_label_path,"r") as f:
        descri_label=json.load(f)
    description=descri_label["description"]
    class_label=descri_label["class_label"]
    model=tf.keras.models.load_model(os.path.join(folder,"model.h5"),custom_objects={'KerasLayer':hub.KerasLayer})
    return model,description,class_label

def make_predictions(model,image,class_label):
    prediction=(model.predict(image,verbose=0))
    return prediction,class_label[np.argmax(prediction)]

def main():
    
    st.title("OM NAMAH SHIVAY")
    image_url=st.text_input("inter image url")
    uploaded_file=st.file_uploader("upload a file containing a flower or fruit",type=["png","jpg"])
    
    model_names=os.listdir(saved_model_path)
    if image_url!=None and image_url.strip()!="":
        runner=image_url
    else:
        runner=uploaded_file
    model_name=st.selectbox("select model",model_names)
    st_image=st.empty()
    st_text=st.empty()
    button=st.button("run")
    if button:
        run(runner,model_name,st_image=st_image,st_text=st_text)
    img_file_buffer=None
    camera_on=st.button("camera on")
    camera_off=st.button("camera off")
    if "camera_on" not in st.session_state:
        st.session_state.camera_on=False
        
    if camera_off:
        st.session_state.camera_on=False
    if camera_on:
        st.session_state.camera_on=True
    if st.session_state.camera_on:
        img_file_buffer = st.camera_input("Take a picture")
    
        if img_file_buffer is not None:
                img = Image.open(img_file_buffer)
                img_array = np.array(img)
                img_array=cv2.resize(img_array,(224,224),interpolation=cv2.INTER_NEAREST)
                img_array_expanded=np.expand_dims(img_array,axis=0)
                img_array_expanded=img_array_expanded/255.

                model,description,class_label=get_model(model_name)
                prediction,predicted=make_predictions(model,img_array_expanded,class_label)
                st_image.image(img_array)
                st_text.text(str(predicted)+"__"+str(prediction))
    

main()
