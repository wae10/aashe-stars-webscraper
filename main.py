import csv
from csv import reader
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import os
from dotenv import load_dotenv

# Load environment variables form the .env file
load_dotenv()

# access environment variables
CSV_PATH = os.getenv('CSV_PATH')
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')

url = "https://reports.aashe.org/institutions/participants-and-reports/?sort=-country"


driver = webdriver.Chrome(CHROMEDRIVER_PATH)


# Prepare CSV file to add new data 
csvFile = open(CSV_PATH, "a", newline='', encoding="utf-8")
csvWriter = csv.writer(csvFile)



length = 1083

# loop through each institution
for id in range(0, length):
    # initialize to 0, default
    num_reports = 0
    past_reports_dates = []

    driver.get(url)
    # # wait for page to load
    delay = 10
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="institution_list"]/tbody/tr['+str(id+1)+']/td[1]')))
    except TimeoutException:
        print("Loading took too much time!")
        driver.get(url)
    institution = driver.find_element_by_xpath('//*[@id="institution_list"]/tbody/tr['+str(id+1)+']/td[1]').text

    try:

        # next page
        driver.find_element_by_xpath('//*[@id="institution_list"]/tbody/tr['+str(id+1)+']/td[4]').click()


        # only one report
        ## initialize
        past_reports_dates = []
        try:
            location = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/h4').text
            rating = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[1]').text
            score = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[2]').text
            valid_through = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[3]').text
            liaison = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[4]').text
            submitted = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[5]').text

        # multiple reports, years past    
        except:
            # initialize to 0, default
            num_reports = 0
            rows = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div/section/div/div/table/tbody/tr')
            num_reports = len(rows)

            if num_reports == 1083:
                num_reports = 0

            # which years are the reports?
            ## past reports submission and valid through dates

            if num_reports != 0:
                for year in range(1, num_reports+1):
                    past_reports_dates.append((driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div/table/tbody/tr['+str(year)+']/td[2]/a').text) + " - " + (driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div/table/tbody/tr['+str(year)+']/td[3]').text))

            driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div/table/tbody/tr[1]/td[2]').click()

            location = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/h4').text
            rating = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[1]').text
            score = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[2]').text
            valid_through = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[3]').text
            liaison = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[4]').text
            submitted = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[5]').text

        # convert lit of dates to comma separated strings
        past_reports_dates = [str(element) for element in past_reports_dates]
        past_reports_dates = "; ".join(past_reports_dates)

        # dining service rep
        ## initialize 
        reusable = False
        sustainability_rep = ""
        try:
            driver.find_element_by_xpath("//a[contains(text(), 'Food & Dining')]").click()
            driver.find_element_by_xpath("//a[contains(text(), 'Sustainable Dining')]").click()

            # # wait for page to load
            delay = 10
            try:
                myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[3]/b')))
            except TimeoutException:
                print("Loading took too much time!")
            
            sustainability_rep = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/section/div/div[2]/table/tbody/tr/td[3]/b').text


            # is keyword 'reusable' present?
            keyword = "reusable"

            if keyword in driver.page_source:
                reusable = True

        except:
            print("No Food & Dining")


        # Save to CSV
        csvWriter.writerow((institution, location, rating, score, valid_through, liaison, submitted, sustainability_rep, reusable, num_reports, past_reports_dates))

        print("Institution #" + str(id+1),institution,location,rating,score,valid_through,liaison,submitted,sustainability_rep,reusable,num_reports,past_reports_dates)


    except:
        print("Institution #" + str(id+1))



# Close CSV file and browser
csvFile.close()
driver.close()
