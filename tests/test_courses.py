import unittest
import os
import json
import requests


class CoursesTestCase(unittest.TestCase):
    """This class represents the courses test case"""

    def setUp(self):
        self.url = "http://127.0.0.1:5000/course"
        self.put_url = "http://127.0.0.1:5000/course/101"
        self.headers = {"Content-Type": "application/json"}
        self.add_course_data = '{"title" : "Brand new course","image_path" : "images/some/path/foo.jpg","price" : 25,"on_discount" : false,"discount_price" : 5.0,"description" : "This is a brand new course"}'
        self.add_course_data_error_title_5 = '{"title" : "test","image_path" : "images/some/path/foo.jpg","price" : 25,"on_discount" : false,"discount_price" : 5.0,"description" : "This is a brand new course"}'
        self.add_course_data_error_title_100 = '{"title" : "Donec sollicitudin enim ex, quis egestas velit placerat ac. Maecenas pharetra velit ac orci mattis, et blandit risus faucibus. Nulla in accumsan turpis. Mauris elit nisi, euismod id eros ut, tincidunt accumsan sem. Nunc venenatis id orci sit amet sollicitudin. Quisque aliquam venenatis diam, eget scelerisque odio tincidunt quis. Vivamus sodales ornare ultrices. Praesent et libero diam. Integer eros neque, tempor gravida lobortis id, eleifend non mauris. Vestibulum molestie lorem ac tellus cursus convallis. Donec lacinia, ipsum eu convallis fringilla, tellus justo aliquam erat, volutpat molestie quam purus non eros. Nunc metus metus, ornare id eleifend nec, ultrices non odio.Vivamus semper congue mauris eget gravida. Etiam varius, orci ullamcorper ultrices consectetur, est augue fermentum tellus, in consectetur dolor turpis quis eros. Etiam quam elit, faucibus vitae pharetra quis, congue id elit. Nullam egestas porta lorem ut ultricies. Vestibulum in iaculis ex, et consequat eros. Sed sit amet massa sit amet quam pulvinar maximus sed eget nisi. Morbi eleifend laoreet nulla, aliquam rhoncus ligula condimentum ac. Nulla at pretium sapien. Donec feugiat porta ipsum, eget tincidunt odio dignissim eu.Morbi condimentum porta ullamcorper. Fusce id lacus nec lectus mattis tempus. Quisque tempor molestie augue vel dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse vel vestibulum lacus. Sed pulvinar feugiat neque eu mollis. Maecenas ex dolor, vestibulum nec hendrerit vel, tristique vitae risus. Vivamus nisl ante, vehicula vel leo ut, luctus lacinia tortor. Praesent ac enim turpis. Etiam maximus egestas porta. Aenean vestibulum maximus imperdiet. Donec nec ligula finibus, tempus eros in, consectetur lectus.","image_path" : "images/some/path/foo.jpg","price" : 25,"on_discount" : false,"discount_price" : 5.0,"description" : "This is a brand new course"}'
        self.add_course_data_error_description_255 = '{"description" : "Donec sollicitudin enim ex, quis egestas velit placerat ac. Maecenas pharetra velit ac orci mattis, et blandit risus faucibus. Nulla in accumsan turpis. Mauris elit nisi, euismod id eros ut, tincidunt accumsan sem. Nunc venenatis id orci sit amet sollicitudin. Quisque aliquam venenatis diam, eget scelerisque odio tincidunt quis. Vivamus sodales ornare ultrices. Praesent et libero diam. Integer eros neque, tempor gravida lobortis id, eleifend non mauris. Vestibulum molestie lorem ac tellus cursus convallis. Donec lacinia, ipsum eu convallis fringilla, tellus justo aliquam erat, volutpat molestie quam purus non eros. Nunc metus metus, ornare id eleifend nec, ultrices non odio.Vivamus semper congue mauris eget gravida. Etiam varius, orci ullamcorper ultrices consectetur, est augue fermentum tellus, in consectetur dolor turpis quis eros. Etiam quam elit, faucibus vitae pharetra quis, congue id elit. Nullam egestas porta lorem ut ultricies. Vestibulum in iaculis ex, et consequat eros. Sed sit amet massa sit amet quam pulvinar maximus sed eget nisi. Morbi eleifend laoreet nulla, aliquam rhoncus ligula condimentum ac. Nulla at pretium sapien. Donec feugiat porta ipsum, eget tincidunt odio dignissim eu.Morbi condimentum porta ullamcorper. Fusce id lacus nec lectus mattis tempus. Quisque tempor molestie augue vel dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse vel vestibulum lacus. Sed pulvinar feugiat neque eu mollis. Maecenas ex dolor, vestibulum nec hendrerit vel, tristique vitae risus. Vivamus nisl ante, vehicula vel leo ut, luctus lacinia tortor. Praesent ac enim turpis. Etiam maximus egestas porta. Aenean vestibulum maximus imperdiet. Donec nec ligula finibus, tempus eros in, consectetur lectus.","image_path" : "images/some/path/foo.jpg","price" : 25,"on_discount" : false,"discount_price" : 5.0,"title" : "This is a title"}'
        self.add_course_data_error_image_path_100 = '{"title" : "Brand new course","image_path" : "Donec sollicitudin enim ex, quis egestas velit placerat ac. Maecenas pharetra velit ac orci mattis, et blandit risus faucibus. Nulla in accumsan turpis. Mauris elit nisi, euismod id eros ut, tincidunt accumsan sem. Nunc venenatis id orci sit amet sollicitudin. Quisque aliquam venenatis diam, eget scelerisque odio tincidunt quis. Vivamus sodales ornare ultrices. Praesent et libero diam. Integer eros neque, tempor gravida lobortis id, eleifend non mauris. Vestibulum molestie lorem ac tellus cursus convallis. Donec lacinia, ipsum eu convallis fringilla, tellus justo aliquam erat, volutpat molestie quam purus non eros. Nunc metus metus, ornare id eleifend nec, ultrices non odio.","price" : 25,"on_discount" : false,"discount_price" : 5.0,"description" : "This is a brand new course"}'
        self.add_course_data_check_required = "{}"
        self.add_course_data_check_not_required = '{"title" : "Brand new course","price" : 25,"on_discount" : false,"discount_price" : 5.0}'
        self.get_courses_negative_page_number = {"page-size": 1, "page-number": -3}
        self.get_courses_negative_page_size = {"page-size": -1, "page-number": 3}
        self.get_courses_correct_params = {"page-size": 10,"page-number": 3,"title-words": "django,python"}
        self.update_course_data_different_payload_id = '{"image_path": "images/some/path/foo.jpg","discount_price": 5,"id": 102,"price": 25,"title": "Blah blah blah","on_discount": false,"description": "New description"}'
        self.update_course_data = '{"image_path": "images/some/path/foo.jpg","discount_price": 5,"id": 101,"price": 25,"title": "Blah blah blah","on_discount": false,"description": "New description"}'
        self.update_course_data_error_title_5 = '{"image_path": "images/some/path/foo.jpg","discount_price": 5,"id": 101,"price": 25,"title": "Bla","on_discount": false,"description": "New description"}'
        self.update_course_data_error_title_100 = '{"image_path": "images/some/path/foo.jpg","discount_price": 5,"id": 101,"price": 25,"title": "Donec sollicitudin enim ex, quis egestas velit placerat ac. Maecenas pharetra velit ac orci mattis, et blandit risus faucibus. Nulla in accumsan turpis. Mauris elit nisi, euismod id eros ut, tincidunt accumsan sem. Nunc venenatis id orci sit amet sollicitudin. Quisque aliquam venenatis diam, eget scelerisque odio tincidunt quis. Vivamus sodales ornare ultrices. Praesent et libero diam. Integer eros neque, tempor gravida lobortis id, eleifend non mauris. Vestibulum molestie lorem ac tellus cursus convallis. Donec lacinia, ipsum eu convallis fringilla, tellus justo aliquam erat, volutpat molestie quam purus non eros. Nunc metus metus, ornare id eleifend nec, ultrices non odio.Vivamus semper congue mauris eget gravida. Etiam varius, orci ullamcorper ultrices consectetur, est augue fermentum tellus, in consectetur dolor turpis quis eros. Etiam quam elit, faucibus vitae pharetra quis, congue id elit. Nullam egestas porta lorem ut ultricies. Vestibulum in iaculis ex, et consequat eros. Sed sit amet massa sit amet quam pulvinar maximus sed eget nisi. Morbi eleifend laoreet nulla, aliquam rhoncus ligula condimentum ac. Nulla at pretium sapien. Donec feugiat porta ipsum, eget tincidunt odio dignissim eu.Morbi condimentum porta ullamcorper. Fusce id lacus nec lectus mattis tempus. Quisque tempor molestie augue vel dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse vel vestibulum lacus.","on_discount": false,"description": "New description"}'
        self.update_course_data_error_description_255 = '{"image_path": "images/some/path/foo.jpg","discount_price": 5,"id": 101,"price": 25,"title": "this is new title","on_discount": false,"description": "New description Donec sollicitudin enim ex, quis egestas velit placerat ac. Maecenas pharetra velit ac orci mattis, et blandit risus faucibus. Nulla in accumsan turpis. Mauris elit nisi, euismod id eros ut, tincidunt accumsan sem. Nunc venenatis id orci sit amet sollicitudin. Quisque aliquam venenatis diam, eget scelerisque odio tincidunt quis. Vivamus sodales ornare ultrices. Praesent et libero diam. Integer eros neque, tempor gravida lobortis id, eleifend non mauris. Vestibulum molestie lorem ac tellus cursus convallis. Donec lacinia, ipsum eu convallis fringilla, tellus justo aliquam erat, volutpat molestie quam purus non eros. Nunc metus metus, ornare id eleifend nec, ultrices non odio.Vivamus semper congue mauris eget gravida. Etiam varius, orci ullamcorper ultrices consectetur, est augue fermentum tellus, in consectetur dolor turpis quis eros. Etiam quam elit, faucibus vitae pharetra quis, congue id elit. Nullam egestas porta lorem ut ultricies. Vestibulum in iaculis ex, et consequat eros. Sed sit amet massa sit amet quam pulvinar maximus sed eget nisi. Morbi eleifend laoreet nulla, aliquam rhoncus ligula condimentum ac. Nulla at pretium sapien. Donec feugiat porta ipsum, eget tincidunt odio dignissim eu.Morbi condimentum porta ullamcorper. Fusce id lacus nec lectus mattis tempus. Quisque tempor molestie augue vel dignissim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse vel vestibulum lacus."}'
        self.update_course_data_error_image_path_100 = '{"image_path": "imageseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee/someeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee/pathhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh/fooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo.jpg","discount_price": 5,"id": 101,"price": 25,"title": "Blah blah blah","on_discount": false,"description": "New description"}'
        self.update_course_data_check_required = "{}"
        self.delete_course_valid_id = 101
        self.delete_course_invalid_id = 1001

    def test_courses_creation(self):
        res = requests.request(
            "POST", self.url, headers=self.headers, data=self.add_course_data
        )
        self.assertEqual(res.status_code, 201)

    def test_course_creation_error_title_length_less_than_5(self):
        res = requests.request(
            "POST",
            self.url,
            headers=self.headers,
            data=self.add_course_data_error_title_5,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("title", res.json()["errors"])
        self.assertEqual(
            "Length of title must be between 5 and 100",
            res.json()["errors"]["title"][0],
        )

    def test_course_creation_error_title_length_greater_than_100(self):
        res = requests.request(
            "POST",
            self.url,
            headers=self.headers,
            data=self.add_course_data_error_title_100,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("title", res.json()["errors"])
        self.assertEqual(
            "Length of title must be between 5 and 100",
            res.json()["errors"]["title"][0],
        )

    def test_course_creation_error_description_length_greater_than_255(self):
        res = requests.request(
            "POST",
            self.url,
            headers=self.headers,
            data=self.add_course_data_error_description_255,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("description", res.json()["errors"])
        self.assertEqual(
            "description should not exceed 255 characters",
            res.json()["errors"]["description"][0],
        )

    def test_course_creation_error_image_path_length_greater_than_100(self):
        res = requests.request(
            "POST",
            self.url,
            headers=self.headers,
            data=self.add_course_data_error_image_path_100,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("image_path", res.json()["errors"])
        self.assertEqual(
            "Length of image_path must be less than 100",
            res.json()["errors"]["image_path"][0],
        )

    def test_course_creation_check_required(self):
        res = requests.request(
            "POST",
            self.url,
            headers=self.headers,
            data=self.add_course_data_check_required,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("on_discount", res.json()["errors"])
        self.assertIn("price", res.json()["errors"])
        self.assertIn("title", res.json()["errors"])

    def test_course_creation_check_not_required(self):
        res = requests.request(
            "POST",
            self.url,
            headers=self.headers,
            data=self.add_course_data_check_not_required,
        )
        self.assertEqual(res.status_code, 201)

    def test_get_courses_default(self):
        res = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(res.status_code, 200)

    def test_get_courses_negative_page_number(self):
        res = requests.request(
            "GET",
            self.url,
            headers=self.headers,
            params=self.get_courses_negative_page_number,
        )
        self.assertEqual(res.status_code, 422)

    def test_get_courses_negative_size_number(self):
        res = requests.request(
            "GET",
            self.url,
            headers=self.headers,
            params=self.get_courses_negative_page_size,
        )
        self.assertEqual(res.status_code, 422)

    def test_get_courses_correct_parameters(self):
        res = requests.request(
            "GET",
            self.url,
            headers=self.headers,
            params=self.get_courses_correct_params,
        )
        self.assertEqual(res.status_code, 200)

    def test_course_updation_error_title_length_less_than_5(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data_error_title_5,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("title", res.json()["errors"])
        self.assertEqual(
            "Length of title must be between 5 and 100",
            res.json()["errors"]["title"][0],
        )

    def test_course_updation_error_title_length_greater_than_100(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data_error_title_100,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("title", res.json()["errors"])
        self.assertEqual(
            "Length of title must be between 5 and 100",
            res.json()["errors"]["title"][0],
        )

    def test_course_updation_error_description_length_greater_than_255(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data_error_description_255,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("description", res.json()["errors"])
        self.assertEqual(
            "description should not exceed 255 characters",
            res.json()["errors"]["description"][0],
        )

    def test_course_updation_error_image_path_length_greater_than_100(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data_error_image_path_100,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("image_path", res.json()["errors"])
        self.assertEqual(
            "Length of image_path must be less than 100",
            res.json()["errors"]["image_path"][0],
        )

    def test_course_updation_check_required(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data_check_required,
        )
        self.assertEqual(res.status_code, 422)
        self.assertIn("errors", res.json())
        self.assertIn("on_discount", res.json()["errors"])
        self.assertIn("price", res.json()["errors"])
        self.assertIn("title", res.json()["errors"])

    def test_course_updation_valid(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data,
        )
        self.assertEqual(res.status_code, 200)

    def test_course_updation_different_id(self):
        res = requests.request(
            "PUT",
            self.put_url,
            headers=self.headers,
            data=self.update_course_data_different_payload_id,
        )
        self.assertEqual(res.status_code, 400)

    def test_delete_course_valid(self):
        res = requests.request(
            "DELETE", f"{self.url}/{self.delete_course_valid_id}", headers=self.headers
        )
        self.assertEqual(res.status_code, 200)

    def test_delete_course_invalid(self):
        res = requests.request(
            "DELETE",
            f"{self.url}/{self.delete_course_invalid_id}",
            headers=self.headers,
        )
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()