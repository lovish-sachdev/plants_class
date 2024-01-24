# import streamlit as st
# import cv2,requests,os,base64,json
# import matplotlib.pyplot as plt
# from PIL import Image
# import numpy as np
# from io import BytesIO
# import tensorflow as tf

# dir_name=os.path.dirname(__file__)
# saved_model_path=os.path.join(dir_name,"saved models")
# saved_model_path=os.path.join(saved_model_path,"saved models")
# img_path=os.path.join(dir_name,"image.png")
# st.write(dir_name+"____"+saved_model_path+"___"+img_path)

# def run(image_url,model_name):
    
#     if image_url.startswith("data"):
#         _,encoded_data=image_url.split(",",1)
#         decoded_data=base64.b64decode(encoded_data)
#         # Convert the binary data to an image
#         img=Image.open(BytesIO(decoded_data))
#         np_img=np.array(img)
#         np_img=cv2.resize(np_img,(224,224),interpolation=cv2.INTER_NEAREST)
#         np_img=np.expand_dims(np_img,axis=0)
#         model,description,class_label=get_model(model_name)
#         prediction,label=make_predictions(model,np_img,class_label)
#         st.write(prediction,label)
#         st.image(np_img, caption="Your Image Caption", use_column_width=True)
#     else:
#         img=cv2.imread(image_url)
#         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         np_img=cv2.resize(img,(224,224),interpolation=cv2.INTER_NEAREST)

#         model,description,class_label=get_model(model_name)
#         prediction,label=make_predictions(model,np_img,)
#         st.write(prediction,label)
#         st.image(np_img, caption="Your Image Caption", use_column_width=True)

# def  get_model(name,model_path=saved_model_path):
#     folder=os.path.join(model_path,name)
#     descri_label=os.path.join(folder,"description.json")
#     with open (descri_label,"r") as f:
#         descri_label=json.load(f)
#     description=descri_label["description"]
#     class_label=descri_label["class_label"]
#     model=tf.keras.models.load_model(os.path.join(folder,"model.h5"))
#     return model,description,class_label

# def make_predictions(model,image,class_label):
#     prediction=(model.predict(image,verbose=0))
#     return prediction,class_label[np.argmax(prediction)]

# def main():
    
#     st.title("OM NAMAH SHIVAY")
#     image_url=st.text_input("inter image url")
    
#     model_names=os.listdir(saved_model_path)
    
#     model_name=st.selectbox("select model",model_names)
#     st.button("run",on_click=lambda:run(image_url,model_name))

#     access_camera = st.button("Start Camera")
#     capture = st.button("Capture Last Frame")
#     frame_placeholder = st.empty()
#     if access_camera:
#         # cap = cv2.VideoCapture(0)
#         # while True:
#         #     ret, frame = cap.read()
#         #     img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#         #     frame_placeholder.image(img, caption="Live Camera Feed", use_column_width=True)
#         #     frame=cv2.resize(frame,(224,224),interpolation=cv2.INTER_NEAREST)
#         #     cv2.imwrite(img_path,frame)
#         # cap.release()
#         img_file_buffer = st.camera_input("Take a picture")

#         if img_file_buffer is not None:
#             img = Image.open(img_file_buffer)
#             img_array = np.array(img)
#             st.write(type(img_array))
#             st.write(img_array.shape)


#     st_image=st.empty()
#     st_text=st.empty()
#     if capture:
#         img=Image.open(img_path)
#         st_image.image(img)
#         np_img=np.array(img)
#         np_img=np.expand_dims(np_img,axis=0)
#         model,description,class_label=get_model(model_name)
#         prediction,predicted=make_predictions(model,np_img,class_label)
#         st_text.text(str(prediction)+"__"+str(predicted))



# if __name__ == "__main__":
#     main()


import streamlit as st
from PIL import Image
import numpy as np

def capture_image():
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is
 
not
 
None:
        img = Image.open(img_file_buffer)
        img_array = np.array(img)

        st.write(type(img_array))
        st.write(img_array.shape)

if st.button("Capture Image"):
    capture_image()
