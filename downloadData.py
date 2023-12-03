from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from data_login import a, b

# lokasi download
downloadFilepath = "C:\\Users\\USER\\Desktop\\belajar\\ProjectDAS\\downloaded_files\\"
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': downloadFilepath}
chrome_options.add_experimental_option('prefs', prefs)

# lokasi chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=chrome_options)

# website tujuan scrapping
url = "https://connect.ihsmarkit.com/gta/my-saved"
driver.get(url)
driver.maximize_window()

# akun login
username = a
password = b

driver.implicitly_wait(1000)

# input email
SearchInput = driver.find_element(By.NAME, 'emailAddress')
SearchInput.send_keys(username + Keys.ENTER)

driver.implicitly_wait(1000)

# input password
SearchInput = driver.find_element(By.NAME, 'password')
SearchInput.send_keys(password + Keys.ENTER)

# alert
wait = WebDriverWait(driver,1000)
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-content']//span[contains(@class,'text')]"))).click()

driver.implicitly_wait(1000)

# download
SearchInput = driver.find_element(By.XPATH, '//tbody/tr[1]/td[7]/div[1]/cui-icon[1]')
SearchInput.click()

def latest_download_file():
      path = r'C:\\Users\\USER\\Desktop\\belajar\\ProjectDAS\\downloaded_files\\'
      os.chdir(path)
      files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
      newest = files[-1]

      return newest

fileends = "crdownload"
while "crdownload" == fileends:
    time.sleep(5)
    newest_file = latest_download_file()
    if "crdownload" in newest_file:
        fileends = "crdownload"
    else:
        fileends = "none"

# clear cookies and quit
driver.delete_all_cookies()
driver.quit()

# import urllib
# import time
# while True:
#     urllib.urlretrieve('file', 'file')
#     time.sleep(86400) # 86400 seconds = 24 hours.