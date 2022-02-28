import unittest
import sys

from hotel import Hotel
sys.path.append(".")

class TestHotel(unittest.TestCase):
    def test_hotel_name(self):
        hotel = Hotel('Test','Adress 1')
        name = 'Test'
        self.assertEqual(hotel.get_name(),name)

    def test_hotel_adress(self):
        hotel = Hotel('Test','Adress 1')
        adress = 'Adress 1'
        self.assertEqual(hotel.get_adress(), adress)

    def test_edit_hotel_name(self):
        hotel = Hotel('Test','Adress 1')
        name = 'HotelNameEdited'
        hotel.set_name('HotelNameEdited')
        self.assertEqual(hotel.get_name(),name)

    def test_edit_hotel_adress(self):
        hotel = Hotel('Test','Adress 1')
        adress = 'HotelAdressEdited'
        hotel.set_adress('HotelAdressEdited')
        self.assertEqual(hotel.get_adress(),adress)

    def test_hotel_bacic_info(self):
        hotel = Hotel('Test','Adress 1')
        info = 'Hotel name: Test. Hotel location: Adress 1'
        self.assertEqual(hotel.get_hotel_basic_info(),info)

    
    

if __name__ == '__main__':
       
    unittest.main()