from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox(executable_path=r"C:\Users\Ciusiek\Desktop\drivers\geckodriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# how to find how many inputboxes present in web page
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))

status = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print("Displayed or not", status) #True/False
status = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print("Enabled or not", status) #True/False

# providing values into text boxes
time.sleep(2)
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Maciej")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Bugaj")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("123456789")
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("Poland")
driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Wrocław")
driver.find_element(By.ID, "RESULT_TextField-6").send_keys("maciek@gmail.com")

# checking the checkbox and the radio
element = driver.find_element(By.ID, "RESULT_RadioButton-7_0")
driver.execute_script("arguments[0].click();", element)

element = driver.find_element(By.ID, "RESULT_CheckBox-8_1")
driver.execute_script("arguments[0].click();", element)

# sending results
time.sleep(2)
driver.find_element(By.ID, "FSsubmit").click()