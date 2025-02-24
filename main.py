from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import pandas as pd

s = Service("C:/Users/HP/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service = s)

driver.get("https://www.google.com")

institution_name = []
results = []

def modify_institution_name(name):
    if '-' in name:
        parts = name.split('-')
        if len(parts) == 2:
            return parts[0].strip() + " latitude and longitude"
        else:
            return parts[0].strip() + " latitude and longitude"
    else:
        return name + " latitude and longitude"
    
data = {'Institution Name': ['Kumaraguru College Of Technology']}
institution_name = []
results = []

for institution in data['Institution Name']:
    institution_name.append(institution)
    modified_institution = modify_institution_name(institution)
    
    try:
        search = driver.find_element('name', 'q')
        search.clear() 
        search.send_keys(modified_institution)
        search.send_keys(Keys.ENTER)
        time.sleep(3)  

        try:
            lat_long = driver.find_element_by_class_name("Z0LcW.t2b5Cf.vMhfn").text
        except NoSuchElementException:
            search.clear()
            search.send_keys(institution + " latitude and longitude")
            search.send_keys(Keys.ENTER)
            time.sleep(3)  
            lat_long = driver.find_element_by_class_name("Z0LcW.t2b5Cf.vMhfn").text
        results.append({"Institution": institution, "Latitude and Longitude": lat_long})
        print(f"Latitude and Longitude for {institution}: {lat_long}")

    except (NoSuchElementException, ElementNotInteractableException):
        print(f"Latitude and Longitude for {institution} not found.")
        results.append({"Institution": institution, "Latitude and Longitude": "Not Found"})

df_results = pd.DataFrame(results)
df_results.to_csv("institution_lat_long.csv", index=False)

driver.quit()


