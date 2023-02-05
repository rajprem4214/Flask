from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "rajprem3230@gmail.com"
password = "Pr69MR@7425!"
# if email and password isnt given, it'll prompt in terminal
actions.login(driver, email, password)
person = Person(
    "https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver)
