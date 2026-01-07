from bs4 import BeautifulSoup
import requests
from Course import Course


class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self, url="http://learn-co-curriculum.github.io/site-for-scraping/courses"):
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course_element in self.get_courses():
            title = course_element.select("h2")[0].text if course_element.select("h2") else ''
            schedule = course_element.select(".date")[0].text if course_element.select(".date") else ''
            description = course_element.select("p")[0].text if course_element.select("p") else ''
            
            new_course = Course(title, schedule, description)
            self.courses.append(new_course)
        
        return self.courses

