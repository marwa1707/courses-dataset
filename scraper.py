#%% 

from selenium import webdriver
from time import sleep

# k in import keys has to be Capital K
from selenium.webdriver.common.keys import Keys
search_phrase = "machine learning"

# Chrome has to be in Capital C
driver = webdriver.Chrome('ChromeDriver/chromedriver')
driver.set_page_load_timeout(30)
try:

    driver.get("https://www.coursera.org/search?query=machine%20learning&page=100&index=prod_all_products_term_optimization")
except:
    print("time out")
#%%
element = driver.find_element_by_xpath("//input[@type='text']")
element.send_keys(search_phrase)
try:
    element.send_keys(Keys.ENTER)

except:
    print("error")

'''
But what if i wanted to press the search button 
How can I find the path for it?
Tried the followwing xpaths but did not work!
'''
#//button[@type='button']
#"//button/div/sgv/g[@stroke='none']"
# search_button.click()

Data = {"Coure Title": [], "Offered By": [], "Course Type": [], "Rating (out of 5)": [], "Number of Students Who Rated": [], "Enrolled Students": [], "Course Level": []}

#%%
location = driver.find_element_by_css_selector("ul.ais-InfiniteHits-list")
list_of_courses = location.find_elements_by_css_selector("li")

for element in list_of_courses:
    text = element.text
    print(text)

#     course_title = e.find_element_by_class_name("color-primary-text card-title headline-1-text").text
#     Data["Coure Title"].append(course_title)
#     Offered_By = courses.find_element_by_css_selector("span.partner-name-m-b-1s")
#     Data["Offered By"].append(Offered_By.text )
#     Course_Type = courses.find_element_by_css_selector("div._jen3vs _1d8rgfy3")
#     Data["Course Type"].append(Course_Type.text)
#     Rating = courses.find_element_by_css_selector("span.ratings-text")
#     Data["Rating (out of 5)"].append(Rating.text)
#     Number_Students_Rated = courses.find_element_by_css_selector("span.ratings-count")
#     Data["Number of Students Who Rated"].append(Number_Students_Rated.text)
#     Enrolled_Students = courses.find_element_by_css_selector("span.enrollment-number")
#     Data["Enrolled Students"].append(Enrolled_Students.text)
#     Course_Level = courses.find_element_by_css_selector("span.product-difficulty")
#     Data["Enrolled Students"].append(Course_Level.text)

#%%
'''  Next Page Function '''
# def next_page(driver):

#     pagination = driver.find_element_by_xpath('')
#     link_to_nextpages = pagination.find_element_b_tag_name('')
#     for link in link_to_nextpages:
#         if link.text == "Next":
#             relevent_link = link
#     relevent_link.click()
