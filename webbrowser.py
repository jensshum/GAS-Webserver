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

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://gans.epreop.com/OfficeAdmin/clientLogin.aspx")
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
try:
    html_path = '''//div[@onclick="javascript:window.parent.showLoader();reDirectTo('/OfficeAdmin/reports2.aspx')"]'''
    search = driver.switch_to.frame("RAD_SPLITTER_PANE_EXT_CONTENT_ContentPane")
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, html_path))
    )
    search = driver.find_element(By.XPATH, html_path)
    print('path found')
except Exception as e:
    print(f"Could not locate element: {e}")
    driver.close()
print("Entered Analytics")
search.click()
sleep(2)
try:
    search = driver.find_element(By.XPATH, '''//table[@id="ctl00_ctl00_ContentPlaceHolder_BodyPlaceHolder_dlReports"]/tbody/tr[5]/td[2]/div[2]/span/span''')
    print("Found run element")
except Exception as e:
    print(f"Could not locate element. Error: {e}")
    driver.close()
print('finished search')





