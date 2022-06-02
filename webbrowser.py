from argparse import Action
from cgitb import html
from gettext import find
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.WebElement;
# import org.openqa.selenium.chrome.ChromeDriver;
from time import sleep
from datetime import timedelta
import datetime

#%% OPEN PROVATION
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://gans.epreop.com/OfficeAdmin/clientLogin.aspx")

#%% LOGIN 
try: 
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ctl00_ContentPlaceHolder_ContentPlaceHolder_LoginForm_ctl05_MALogin_login_UserName"))
    )
except:
    driver.quit()
search = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder_ContentPlaceHolder_LoginForm_ctl05_MALogin_login_UserName")
search.send_keys("shshumway")
search2 = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder_ContentPlaceHolder_LoginForm_ctl05_MALogin_login_Password")
search2.send_keys("Gofastgas22")
search2.send_keys(Keys.RETURN)
sleep(3)
#%% ENTER ANALYTICS
try:
    Xpath = '''//div[@onclick="javascript:window.parent.showLoader();reDirectTo('/OfficeAdmin/reports2.aspx')"]'''
    search = driver.switch_to.frame("RAD_SPLITTER_PANE_EXT_CONTENT_ContentPane")
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, Xpath))
    )
    search = driver.find_element(By.XPATH, Xpath)
    print('path found')
except Exception as e:
    print(f"Could not locate element: {e}")
    driver.close()
print("Entered Analytics")
search.click()
sleep(2)
#%% ENTER QA SECTION
try:
    search = driver.find_element(By.XPATH, '''//table[@id="ctl00_ctl00_ContentPlaceHolder_BodyPlaceHolder_dlReports"]/tbody/tr[5]/td[2]/div[2]/span''')
    print("Found run element")
except Exception as e:
    print(f"Error loading page. Error: {e}")
    driver.close()
sleep(1)
search.click()
try:
    Xpath = '''//div[@id="divParams"]/div/table/tbody/tr[2]/td[1]/input'''
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, Xpath))
    )
    search = driver.find_element(By.XPATH, Xpath)
except Exception as e:
    print(f"Error loading page: {e}")
#%% ENTER DATES AND DOWNLOAD XML
now = datetime.datetime.now()
todays_date = (now.strftime('%m/%d/%Y'))
yesterday = now - timedelta(days = 1)
yesterdays_date = yesterday.strftime('%m/%d/%Y')
search.send_keys(str(yesterdays_date))
search = driver.find_element(By.XPATH, '''//div[@id="divParams"]/div/table/tbody/tr[2]/td[2]/input''')
search.send_keys(str(todays_date))
search = driver.find_element(By.ID, "ctl00_ctl00_ContentPlaceHolder_BodyPlaceHolder_btnRunReport")
search.click()
sleep(3)
search = driver.find_element(By.ID, "ctl00_ctl00_ContentPlaceHolder_BodyPlaceHolder_rptMSRSViewer_ctl05_ctl04_ctl00_ButtonLink")
search.click()
search = driver.find_element(By.XPATH, '''//div[@id="ctl00_ctl00_ContentPlaceHolder_BodyPlaceHolder_rptMSRSViewer_ctl05_ctl04_ctl00_Menu"]/div/a''')
search.send_keys(Keys.RETURN)

#%% CONNECT TO STEP ONE WEBPAGE

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://dataportal.greatergas.com/login?next=%2Fprofile")
try:

    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "inputUsername"))
    )
    search = driver.find_element(By.ID, "inputUsername")
    search.send_keys("sheldon")
except Exception as e:
    print(f'There was an error locating the element: {e}')

search = driver.find_element(By.ID, "inputPassword")
search.send_keys("Gofastgas22")
search.send_keys(Keys.RETURN)

try:
    sleep(3)
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '''//a[@href="/automation-step1"]'''))
    )
    search = driver.find_element(By.XPATH, '''//a[@href="/automation-step1"]''')
    search.click()

except Exception as e:
    print(f'There was an error locating the element: {e}')

search = driver.find_element(By.NAME, "archivo")
search.send_keys("C:/Users/noahs/Downloads/BillingQualityExportReport.xml")
search = driver.find_element(By.ID, "btnFetch")
search.click()


print('finished search.')




# %%
