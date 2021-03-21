from flask import jsonify, Response
from collections import OrderedDict
from courses.models.CourseStore import CourseStore
from courses.models.Course import Course
import json
import datetime


class CourseAccessor(object):
    """
    Course Accessor class that implements functions that are responsible for the
    communication between the database and the api.
    """

    def __init__(self):
        """
        Course Accessor class on initiation loads course store object.
        """
        self.courseStore = CourseStore()

    def get_all_courses(self, page_number, page_size, title):
        """
        Method of Data Accessor class used to fetch courses based on
        page_number, page_size and title words.
        """
        try:
            id_list = []
            results = list(
                map(lambda x: x.to_dict(), self.courseStore.courses.values())
            )
            results = results[
                ((page_number - 1) * page_size if page_number is not 1 else 0) : (
                    (page_number - 1) * page_size + page_size
                    if page_number is not 1
                    else page_size
                )
            ]
            if title is not None:
                for word in title.split(","):
                    word = word.lower().strip()
                    possible_course = self.courseStore.searchRepo.get(word, None)
                    if possible_course is not None:
                        id_list.extend(possible_course)
                results = list(
                    filter(
                        lambda x: x["id"] in set(id_list),
                        results,
                    )
                )
            count = len(results)
            obj = {"metadata": {}}
            obj["metadata"]["page_number"] = page_number
            obj["metadata"]["page_size"] = page_size
            obj["metadata"]["page_count"] = max(1, count // page_size)
            obj["metadata"]["record_count"] = count
            obj["data"] = results
            response = jsonify(obj)
            response.status_code = 200
            return response
        except Exception as e:
            print(e)
            response = jsonify({"message": "Some backend error occured"})
            response.status_code = 500
            return response

    def get_course_by_id(self, id):
        """
        Method of Data Accessor class used to fetch  a single course based on
        course id.
        """
        try:
            course = self.courseStore.courses.get(int(id))
            if course is None:
                response = jsonify({"messge": f"Course {id} does not exist"})
                response.status_code = 404
                return response
            response = jsonify(
                {"data": self.courseStore.courses.get(int(id)).to_dict()}
            )
            response.status_code = 200
            return response
        except Exception as e:
            response = jsonify({"message": "Some backend error occured"})
            response.status_code = 500
            return response

    def add_course(self, course_data):
        """
        Method of Data Accessor class used to add a new course to database.
        """
        try:
            id = self.courseStore.last_course_id + 1
            course = Course(
                id,
                course_data.get("title", None),
                course_data["description"]
                if course_data.get("description", None)
                else "",
                course_data.get("price", None),
                course_data.get("discount_price", None),
                course_data["image_path"]
                if course_data.get("image_path", None)
                else "",
                course_data.get("on_discount", None),
                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )
            self.courseStore.courses.update({id: course})
            self.courseStore.last_course_id = course.id
            response = jsonify({"data": course.to_dict()})
            response.status_code = 201
            return response
        except Exception as e:
            response = jsonify({"message": "Some backend error occured"})
            response.status_code = 500
            return response

    def update_course_by_id(self, id, course_data):
        """
        Method of Data Accessor class used to update course based on course id.
        """
        try:
            current_obj = self.courseStore.courses.get(int(id))
            id = int(id)
            if current_obj is None:
                response = jsonify({"messge": f"Course {id} does not exist"})
                response.status_code = 404
                return response
            if course_data.get("id") != int(id):
                response = jsonify({"message": "The id does match the payload"})
                response.status_code = 400
                return response
            current_obj.title = course_data.get("title")
            current_obj.description = (
                course_data["description"]
                if course_data.get("description", None)
                else ""
            )
            current_obj.price = course_data.get("price", None)
            current_obj.discount_price = course_data.get("discount_price", None)
            current_obj.image_path = (
                course_data.get("image_path", None)
                if course_data.get("image_path", None)
                else ""
            )
            current_obj.on_discount = course_data.get("on_discount", None)
            current_obj.date_updated = str(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            new_obj = dict(current_obj.to_dict())
            new_obj.pop('date_created')
            response = jsonify(new_obj)
            return response
        except Exception as e:
            response = jsonify({"message": "Some backend error occured"})
            response.status_code = 500
            return response

    def delete_course_by_id(self, id):
        """
        Method of Data Accessor class used to delete course from database.
        """
        try:
            course = self.courseStore.courses.get(int(id))
            if course is not None:
                self.courseStore.courses.pop(int(id))
                response = jsonify({"message": "The specified course was deleted"})
                response.status_code = 200
            else:
                response = jsonify({"message": f"Course {id} does not exist"})
                response.status_code = 404
            return response
        except Exception as e:
            response = jsonify({"message": "Some backend error occured"})
            response.status_code = 500
            return response