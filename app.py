"""
    Esta aplicación está destinada únicamente a fines educativos.
    La razón principal y única por la que he desarrolado esta app
    es porque quiero poner en práctica los conceptos aprendidos en
    la documentación oficial de Selenium.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

EMAIL = "x@gmail.com"
PSW = "y"
options = webdriver.ChromeOptions().add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


def login(user_email, usr_pwd):
    driver.get("https://prenotami.esteri.it/")
    driver.find_element(by=By.ID, value="login-email").send_keys(user_email)
    driver.find_element(by=By.ID, value="login-password").send_keys(usr_pwd)
    driver.find_element(by=By.CLASS_NAME, value="button.primary.g-recaptcha").click()
    return


login(EMAIL, PSW)
driver.find_element(by=By.LINK_TEXT, value="Prenota").click()
time.sleep(4)
driver.find_element(by=By.XPATH, value='//a[@href="/Services/Booking/791"]').click()
time.sleep(10)
driver.quit()
