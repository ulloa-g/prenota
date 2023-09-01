"""
    Esta aplicación está destinada únicamente a fines educativos.
    La razón principal y única por la que he desarrolado esta app
    es porque quiero poner en práctica los conceptos aprendidos en
    la documentación oficial de Selenium.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://prenotami.esteri.it/")
driver.find_element(by=By.ID, value="login-email").send_keys("my_personal_email@gmail.com")
driver.find_element(by=By.ID, value="login-password").send_keys("my_custom_pswd")
driver.find_element(by=By.CLASS_NAME, value="button.primary.g-recaptcha").click()
