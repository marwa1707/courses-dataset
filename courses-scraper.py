#%%
from bs4 import BeautifulSoup
import requests
from time import sleep

data = {"Coure Title": [], "School Name": [], "Rating (out of 5)": [], "Number of Students Who Rated": [], "Course Level": []}
# page = 1
for page in range(2, 100):
#     html_text = requests.get("https://www.coursera.org/search?query=machine%20learning&page={}&index=prod_all_products_term_optimization".format(page)).text
    html_text = requests.get("https://www.coursera.org/search?query=machine%20learning&page={}&index=prod_all_products_term_optimization".format(page)).text
    # print(html_text)
    sleep(5)
    soup = BeautifulSoup(html_text, 'lxml')
    courses = soup.find_all('li', class_ = "ais-InfiniteHits-item")

    for course in courses:                                                                               
        course_title = course.find('h2', class_ = 'color-primary-text card-title headline-1-text').text
        data["Coure Title"].append(course_title)
        school_title =  course.find('span', class_ = 'partner-name m-b-1s').text
        data["School Name"].append(school_title)
        # rating out of 5:
        rating = course.find('span', class_ = 'ratings-text').text
        data["Rating (out of 5)"].append(rating)
        # number ob people who rated:
        rating_count = course.find('span', class_ = 'ratings-count').text
        data["Number of Students Who Rated"].append(rating_count)
        course_difficulty = course.find('span', class_ = 'difficulty').text
        data["Course Level"].append(course_difficulty)

        print(f'''
                Course Title: {course_title}
                School Name:  {school_title}
                Rating:       {rating}
                Rating Count: {rating_count}
                Course Level: {course_difficulty} ''')

    print(data)

#%%
import pandas as pd
df = pd.DataFrame(data)
# pagination = soup.find_all('div', class_ = 'pagination-controls-container')
# if not pagination.find('button', class_ = 'label-text box arrow arrow-disabled'):

# %%

























































































































































































































