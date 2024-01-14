# import streamlit as st
# import time
# import os,json,io
# import pandas as pd
# from pydrive.drive import GoogleDrive
# from pydrive.auth import GoogleAuth
# from new_app import logic
# def main():

#     file_path=os.path.abspath(__file__)
#     file_dir=os.path.dirname(file_path)
#     mycreds=os.path.join(file_dir,"mycreds.txt")
#     authenticate(mycreds)

# def authenticate(mycreds):
#     gauth=GoogleAuth()
#     gauth.LoadCredentialsFile(mycreds)

#     if gauth.credentials is None:
#         gauth.LocalWebserverAuth()
    
#     elif gauth.access_token_expired:
#         gauth.Refresh()
#     else:
#         gauth.Authorize()
#     gauth.SaveCredentialsFile(mycreds) 
    
#     drive=GoogleDrive(gauth)
#     file_id="1m_fvJXVRWBc038xmLyVXFrQeF7PFCkSk"
#     file = drive.CreateFile({'id': file_id})
#     content = file.GetContentString()
#     df = pd.read_csv(io.StringIO(content))
#     app(df,drive)
# def app(df,drive):

#     # streamlit app
#     # title 
#     st.title("ॐ नमः शिवाय")
#     df.rename(columns={"Unnamed: 0":"index"},inplace=True)
#     st.dataframe(df,hide_index=True)
#     sleep_time=st.slider(label="time difference in minute",min_value=2,max_value=8,value=5)
#     progress_bar=st.progress(0,text="work_done")
#     st.button(label="run",on_click=lambda:start(progress_bar,df,drive,sleep_time))


# def start(progress_bar,df,drive,sleep_time):
#     # print("running")
#     index=logic(df,drive)
#     if index>=len(df):
#         return 
#     progress_bar.progress((index+1)/len(df),text=f"done {index+1} out of {len(df)}")

# if __name__=="__main__":
#     main()






import streamlit as st
import json,os
st.title("om nama shivay")

dir=os.path.dirname(os.path.abspath(__file__))
json_path=os.path.join(dir,"index.json")
# data_path=os.path.join(dir,"data.xlsx")
# data_save_folder=os.path.join(dir,"flower_leave_fruit_data")
## opening and reading index
def function():
    with open(json_path,"r") as json_file:
        index_file=json.load(json_file)
        index=index_file["index"]
    st.write(index)
    index_file["index"]+=1
    with open(json_path,"w") as json_file:
        json.dump(index_file,json_file)
    st.write(index_file["index"])
st.button(label="run",on_change=lambda:function()
