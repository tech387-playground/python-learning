import unittest
import sys

from hotel import Hotel
sys.path.append(".")

class TestHotel(unittest.TestCase):
    def test_add_user_to_hotel(self):
        hotel = Hotel('Test','Adress 1')
        hotel.add_user('Vedin',24)
        self.assertEqual(len(hotel.get_users()),1)

    def test_add_department_to_hotel(self):
        hotel = Hotel('Test','Adress 1')
        hotel.add_department('Kitchen')
        hotel.add_department('Maintenance')
        self.assertEqual(len(hotel.get_departments()),2)

    def test_add_location_to_hotel(self):
        hotel = Hotel('Test','Adress 1')
        hotel.add_location('Floor 1')
        hotel.add_location('Floor 2')
        hotel.add_location('Floor 3')
        hotel.add_location('Floor 4')
        hotel.add_location('Floor 5')
        self.assertEqual(len(hotel.get_locations()),5)
    

if __name__ == '__main__':
       
    unittest.main()