import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
@pytest.fixture()
def setUp():
    global movie_name,driver,yor,director_name,distributor,producer
    movie_name=input("enter your movie name: ")
    yor=input("enter year of release: ")
    director_name=input("enter director name: ")
    distributor=input("enter distributor: ")
    producer=input("enter producer: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(movie_name)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(yor)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(director_name)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(10)