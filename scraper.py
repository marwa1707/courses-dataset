#%% 
import numpy as np
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

search_phrase = "machine learning"

driver = webdriver.Chrome('ChromeDriver/chromedriver')
driver.set_page_load_timeout(30)
try:
    driver.get("https://www.coursera.org/search?query=machine%20learning")
except:
    print("time out")
sleep(30)

data = {"Coure Title": [], "Offered By": [], "Course Type": [], "Rated": [], "Course Level": []}
sleep(30)

# "Rating (out of 5)": [], "Number of Students Who Rated" : [], "Enrolled Students" : [] 
#%%
pages = np.arange(2,10)
for page in pages:
  for i in range(1, 11):
    sleep(30)
    course_title = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//h2[@class='color-primary-text card-title headline-1-text']")
    data["Coure Title"].append(course_title.text)
    sleep(2)
    Offered_By = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div/div/div/div/div/div[2]/div[2]/span")
    data["Offered By"].append(Offered_By.text )
    sleep(2)    
    Course_Type = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div[@class='_jen3vs _1d8rgfy3']")
    data["Course Type"].append(Course_Type.text)
    sleep(2)
    Course_Level = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div/div/div/div/div/div[2]/div[4]/div[2]/span")
    data["Course Level"].append(Course_Level.text)
    sleep(2)
    try:
      course_Rated = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div[@class='rating-enroll-wrapper']")
      data["Rated"].append(course_Rated.text)
    except:
      data["Rated"].append(None)
    # try:
    #   Rating = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div[@class='ratings-text']")
    #   data["Rating (out of 5)"].append(Rating.text)
    # except:
    #   pass
    # sleep(2)
    # try:
    #   Number_Students_Rated = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div/div/div/div/div/div[2]/div[4]/div[1]/div[1]/div/span[2]/span")
    #   data["Number of Students Who Rated"].append(Number_Students_Rated.text)
    # except:
    #   pass
    # sleep(2)
    # try:
    #   Enrolled_Students = driver.find_element_by_xpath("//ul[@class='ais-InfiniteHits-list']/li["+str(i)+"]//div/div/div/div/div/div[2]/div[4]/div[1]/div[2]/span/span")
    #   data["Enrolled Students"].append(Enrolled_Students.text)
    # except:
    #   pass
    # sleep(2)
  link = driver.find_element_by_xpath("//div[@class='pagination-controls-container']/*[@type='button' and @aria-label='Next Page']")
  link.click()

#%%
print(data)
#%%
import pandas as pd
pf = pd.DataFrame.from_dict(data)
pf
#%%

driver.quit()
#%%

# element = driver.find_element_by_xpath("//input[@type='text']")
# element.send_keys(search_phrase)
# try:
#     element.send_keys(Keys.ENTER)

# except:
#     print("error")


# links = driver.find_elements_by_tag_name('a')
# sleep(3)
# links = [link.get_attribute('href') for link in links]
# for link in links:
  # try:
  #   if link.find('machine'and'learning') != -1 :
     # print(link)
      # data["Course Link"].append(link)
      # driver.get(link)

  #     title = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/h1')
  #     print(title)
  #     rate = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/ul/li/a/div/span') 
  #     print(rate)
  #     raters = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[3]/div/div/div/ul/li/a/div/div[2]/span')
  #     print(raters)
  #     instructor = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[4]/ul/li/a/div/div[1]/span')
  #     print(instructor)
  #     enrolled = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[5]/div/div[2]/div/div/span/strong/span')
  #     print(enrolled)
  #     recent_views = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/div/div/div[1]/div[1]/div/span/span')
  #     print(recent_views)
  #     hours_to_complete = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[4]/div[2]/div/span')
  #     print(hours_to_complete)
  #     language = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[5]/div[2]/div[1]')
  #     print(language)
  #     skills = driver.find_elements_by_xpath('//*[@id="main"]/div/div[2]/div/div/div/div/div[1]/div[4]')
  #     print(skills)
  #     skills=[skill.text for skill in skills]
  #     driver.close()
  # except:
  #   pass
