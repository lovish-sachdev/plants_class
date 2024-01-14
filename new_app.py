from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
import json,requests
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
import os,time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from io import BytesIO

def logic(link_data,drive):
    
    ## dirs and paths
    dir=os.path.dirname(os.path.abspath(__file__))
    json_path=os.path.join(dir,"index.json")
    # data_path=os.path.join(dir,"data.xlsx")
    # data_save_folder=os.path.join(dir,"flower_leave_fruit_data")

    ## opening and reading index
    with open(json_path,"r") as json_file:
        index_file=json.load(json_file)
        index=index_file["index"]
    if index>=len(link_data):
        return index
    ## loading link_data
    # link_data=pd.read_excel(data_path,index_col=0)
    plant_data=link_data.iloc[index,:]
    plant_name=plant_data["name"]
    web_link=plant_data["link"]
    # imgs_save_path=os.path.join(data_save_folder,plant_name)
    # os.makedirs(imgs_save_path,exist_ok=True)
    


    # initializing driver
    options=Options()
    options.add_argument("--headless=new")
    # driver=webdriver.Chrome(options=options)
    try:
        chrome_driver_path = ChromeDriverManager().install()
        return ("ChromeDriver successfully installed at:"+ chrome_driver_path)
    except Exception as e:
        return ("Error during ChromeDriver installation:"+ str(e))
    return 0
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    chromedriver_path=os.path.join(dir,"chromedriver-win64\chromedriver-win64\chromedriver.exe")
    # driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
    # service = Service(executable_path=chromedriver_path)
    # driver = webdriver.Chrome(service=service, options=options)


    parent_folder_id = '17wFXsa_v_9sizZo-f4hDfMefZFusL9HM'
    # Create a folder inside the parent folder
    folder_metadata = {'title': plant_name, 'parents': [{'id': parent_folder_id}], 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    
    driver.get(web_link)

    ## getting desired tags and classes
    items=driver.find_element(By.CLASS_NAME,"card-header-tabs")
    item=items.find_elements(By.CLASS_NAME,"nav-item")
    card_body=driver.find_elements(By.CLASS_NAME,"card-body")
    card_body=card_body[-1]
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView(true);", item[0])
    listt=["flower","leaves","fruit"]
    for index,name in enumerate(listt):
        item[index].click()
        imgs=card_body.find_elements(By.TAG_NAME,"img")
        for i in range(10):
            lenn=len(imgs)
            if len(imgs)>2:
                break
            else:
                imgs=card_body.find_elements(By.TAG_NAME,"img")
                time.sleep(1)
        for k in range(2):
            # img_path=os.path.join(imgs_save_path,name+"_"+str(k)+".png")
            img_link=(imgs[k].get_attribute("src"))
            img=BytesIO(requests.get(img_link).content)

            file = drive.CreateFile({'title': plant_name+"_"+name+"_"+str(k),'mimeType': 'image/jpeg'})
            if folder:
                file['parents'] = [{'id': folder['id']}]
            
            file.content = img
            file.Upload()

            # with open(img_path,"wb") as file:
            #     file.write(img)/



    ## closing and updating index
    index_file["index"]+=1
    with open(json_path,"w") as json_file:
        json.dump(index_file,json_file)
    return index_file["index"]

        
