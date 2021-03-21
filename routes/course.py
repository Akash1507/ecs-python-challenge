"""Routes for the course resource.
"""

from run import app
from flask import request, jsonify
from http import HTTPStatus
from courses.accessors.CourseAccessor import CourseAccessor
from courses.validators.Validator import (
    CoursePostSchema,
    CoursePutSchema,
    CourseGetSchema,
)

accessor = CourseAccessor()
course_post_schema = CoursePostSchema()
course_put_schema = CoursePutSchema()
course_get_schema = CourseGetSchema()


@app.route("/course/<int:id>", methods=["GET"])
def get_course(id):
    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE
    response = accessor.get_course_by_id(id)
    return response


@app.route("/course", methods=["GET"])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    course_data = request.args
    errors = course_get_schema.validate(course_data)
    if errors:
        response = jsonify({"errors": errors})
        response.status_code = 422
        return response
    page_number = int(request.args.get("page-number", 1))
    page_size = int(request.args.get("page-size", 5))
    title = request.args.get("title", None)
    response = accessor.get_all_courses(page_number, page_size, title)
    return response


@app.route("/course", methods=["POST"])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    course_data = request.json
    errors = course_post_schema.validate(course_data)
    if errors:
        response = jsonify({"errors": errors})
        response.status_code = 422
        return response
    response = accessor.add_course(course_data)
    return response


@app.route("/course/<int:id>", methods=["PUT"])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    course_data = request.json
    errors = course_put_schema.validate(course_data)
    if errors:
        response = jsonify({"errors": errors})
        response.status_code = 422
        return response
    response = accessor.update_course_by_id(id, course_data)
    return response


@app.route("/course/<int:id>", methods=["DELETE"])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    response = accessor.delete_course_by_id(id)
    return response