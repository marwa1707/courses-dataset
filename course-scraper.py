#%%
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.coursera.org/search?query=machine+str(%20le)+arning&').text
soup = BeautifulSoup(html_text, 'lxml')
courses = soup.find_all('li', class_ = "ais-InfiniteHits-item")



for course in courses:

    course_title = course.find('h2', class_ = 'color-primary-text card-title headline-1-text').text
    school_title = course.find('span', class_ = 'partner-name m-b-1s').text
    # rating out of 5:
    rating = course.find('span', class_ = 'ratings-text').text
    # number ob people who rated:
    rating_count = course.find('span', class_ = 'ratings-count').text
    course_difficulty = course.find('span', class_ = 'difficulty').text
    enrolled_students = course.find('span', class_='enrollment-number').text
    course_ratings = course.find('div', class_='rating-enroll-wrapper').text
    course_type = course.find('div', class_='_jen3vs _1d8rgfy3').text

    print(f'''
          Course Title {course_title}
           School Name  {school_title}
           Course Type {course_type}
           Rating       {rating}
           Rating Count {rating_count}
           Course Level {course_difficulty}
           Enrolled Students {enrolled_students} 
           Reviews {course_ratings}
           ''')
    # data["Course Title"].append(course_title)
    # data["School Name"].append(school_title)
    # data["Course Type"].append(course_type)
    # data["Rating "].append(rating)
    # data["Rating Count"].append(rating_count)
    # data["Course Level"].append(course_difficulty)
    # data["Enrolled Students"].append(enrolled_students)
    # data["Reviews"].append(course_ratings)

for i in range(2,10):

  html_text = requests.get("https://www.coursera.org/search?query=machine%20learning&page="+str(i)+"&index=prod_all_products_term_optimization").text
  soup = BeautifulSoup(html_text, 'lxml')
  courses = soup.find_all('li', class_ = "ais-InfiniteHits-item")
  dataset = {"Course Title"=[], "School Name"=[], "Course Type"=[], "Rating "=[], "Rating Count"=[], "Course Level"=[], "Enrolled Students"=[], "Reviews"=[]}  
  for course in courses:

      course_title = course.find('h2', class_ = 'color-primary-text card-title headline-1-text').text
      data["Course Title"].append(course_title)
      school_title = course.find('span', class_ = 'partner-name m-b-1s').text
      data["School Name"].append(school_title)
      try:
        rating = course.find('span', class_ = 'ratings-text').text
        data["Rating "].append(rating)
      except:
        data["Rating "].append(None)
      try:
        rating_count = course.find('span', class_ = 'ratings-count').text
        data["Rating Count"].append(rating_count)
      except:
        data["Rating Count"].append(None)
      course_difficulty = course.find('span', class_ = 'difficulty').text
      data["Course Level"].append(course_difficulty)
      try:
        enrolled_students = course.find('span', class_='enrollment-number').text
        data["Enrolled Students"].append(enrolled_students)
      except:
        data["Enrolled Students"].append(None)
      course_ratings = course.find('div', class_='rating-enroll-wrapper').text
      data["Reviews"].append(course_ratings)
      course_type = course.find('div', class_='_jen3vs _1d8rgfy3').text
      data["Course Type"].append(course_type)

      
      
      
      
      
      
      
      