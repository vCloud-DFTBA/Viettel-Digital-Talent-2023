import unittest
import requests

URL = "http://localhost:81"


class AppTestCase(unittest.TestCase):
    def test_get_all_attendees(self):
        response = requests.get(f"{URL}/list")
        self.assertEqual(response.status_code, 200)

    def test_add_student(self):
        data = {
            "id": "1",
            "name": "John Doe",
            "username": "johndoe",
            "birth": 1990,
            "sex": "Male",
            "university": "ABC University",
            "major": "Computer Science"
        }
        response = requests.post(f"{URL}/addStudent", json=data)
        self.assertEqual(response.status_code, 201)

        # Kiểm tra xem sinh viên đã được thêm thành công vào cơ sở dữ liệu chưa
        response = requests.get(f"{URL}/view/1")
        self.assertEqual(response.status_code, 200)

    def test_delete_student(self):
        # Thêm một sinh viên vào cơ sở dữ liệu để xóa sau đó
        data = {
            "id": "1",
            "name": "John Doe",
            "username": "johndoe",
            "birth": 1990,
            "sex": "Male",
            "university": "ABC University",
            "major": "Computer Science"
        }
        requests.post(f"{URL}/addStudent", json=data)

        response = requests.delete(f"{URL}/deleteStudent/1")
        self.assertEqual(response.status_code, 200)


    def test_update_student(self):
        # Thêm một sinh viên vào cơ sở dữ liệu để cập nhật sau đó
        data = {
            "id": "1",
            "name": "John Doe",
            "username": "johndoe",
            "birth": 1990,
            "sex": "Male",
            "university": "ABC University",
            "major": "Computer Science"
        }
        requests.post(f"{URL}/addStudent", json=data)

        updated_data = {
            "name": "Jane Doe",
            "username": "janedoe",
            "birth": 1991,
            "sex": "Female",
            "university": "XYZ University",
            "major": "Data Science"
        }
        response = requests.post(f"{URL}/updateStudent/1", json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Kiểm tra xem sinh viên đã được cập nhật thành công trong cơ sở dữ liệu chưa
        response = requests.get(f"{URL}/view/1")
        self.assertEqual(response.status_code, 200)
        student = response.json()[0]
        self.assertEqual(student["name"], "Jane Doe")
        self.assertEqual(student["username"], "janedoe")
        self.assertEqual(student["birth"], 1991)
        self.assertEqual(student["sex"], "Female")
        self.assertEqual(student["university"], "XYZ University")
        self.assertEqual(student["major"], "Data Science")




if __name__ == '__main__':
    unittest.main()
