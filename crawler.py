from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import time 
import pandas as pd


def cal_date(year, month, day):
    start_date = datetime(year, month, day)
    new_date = start_date - timedelta(days=30)
    new_date = new_date.strftime('%Y/%m/%d')
    new_date = new_date.split("/")
    return int(new_date[0]), int(new_date[1]), int(new_date[2])


def get_date(year, month, day):
    return f"{year}/{month}/{day}"


# Create webdriver object
driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.tgju.org/archive/price_dollar_rl")
time.sleep(5)


# Start Date
year, month, day = 1402, 4, 15
month_number = 111
data_dict = {'Date': [], 'Persian_Date': [], 'Open': [], 'Low': [], 'High': [], 'Close': []}

for i in range(month_number):
    date_element = driver.find_element(By.ID, 'history-to')
    date_element.send_keys(f"{get_date(year, month, day)}")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/button[1]').click()
    time.sleep(5)
    year, month, day = cal_date(year, month, day)
    print(get_date(year, month, day))

    table = driver.find_element(By.ID, 'table-list')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        
        data_dict['Date'].append(columns[6].text)
        data_dict['Persian_Date'].append(columns[7].text)
        data_dict['Open'].append(columns[0].text)
        data_dict['Low'].append(columns[1].text)
        data_dict['High'].append(columns[2].text)
        data_dict['Close'].append(columns[3].text)

    date_element.clear()


df = pd.DataFrame.from_dict(data_dict)
df.to_csv('C:/Users/AsusIran/Desktop/dollar_dataset.csv', index=True)

# driver.quit()