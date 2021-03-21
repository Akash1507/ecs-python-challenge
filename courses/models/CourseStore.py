from courses.models.Course import Course
from collections import OrderedDict
import json
import os

class CourseStore(object):
    """
    Course Store Loads the data from Json and make it available throughout the app.
    """

    def __init__(self):
        """
        Constructor
        """
        self.create_data_repository()
        self.create_search_repo()

    def create_data_repository(self):
        """
        Method of Course Store class used to load data.
        """
        course_list = json.load(
            open(os.path.join(os.path.dirname(os.path.abspath("run.py")),"json/course.json"))
        )
        data = OrderedDict()
        for course_data in course_list:
            course = Course(
                course_data["id"],
                course_data["title"],
                course_data["description"],
                course_data["price"],
                course_data["discount_price"],
                course_data["image_path"],
                course_data["on_discount"],
                course_data["date_created"],
                course_data["date_updated"],
            )
            data.update({course.id: course})
        self.last_course_id = course.id
        self.courses = data

    def create_search_repo(self):
        """
        Method of Course Store class used to create search repo for faster retrieval.
        """
        search_repo = {}
        for course_id, course in self.courses.items():
            for word in course.title.split(" "):
                word = word.lower().strip()
                if word not in search_repo:
                    search_repo[word] = [course_id]
                else:
                    if course_id not in search_repo[word]:
                        search_repo[word].append(course_id)
        self.searchRepo = search_repo
