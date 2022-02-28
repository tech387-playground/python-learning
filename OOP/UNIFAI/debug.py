from location import Location
from hotel import Hotel



hotel = Hotel('test','test')
hotel.add_location('Sprat 1')
hotel.add_location('Sprat 2')
hotel.edit_location_sublocations(0,'Soba 1')
hotel.edit_location_sublocations(1,'Soba 2')

x: Location
for x in hotel.get_locations():
    x.get_location()