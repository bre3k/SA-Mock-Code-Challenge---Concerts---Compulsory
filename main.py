import psycopg2
from concerts import Concert
from venues import Venue
from bands import Band

# Establish the connection
conn = psycopg2.connect(
    dbname="concerts",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

# Example usage:

# For Concert methods
concerts = Concert(1)  # Assuming concert with id 1 exists
print(concerts.bands(conn))
print(concerts.venues(conn))
print(concerts.hometown_show(conn))
print(concerts.introduction(conn))

# For Venue methods
venues = Venue(1)  # Assuming venues with id 1 exists
print(venues.concerts(conn))
print(venues.bands(conn))
print(venues.concert_on('2024-09-21', conn))
print(venues.most_frequent_bands(conn))

# For Band methods
bands = Band(1)  # Assuming bands with id 1 exists
print(bands.concerts(conn))
print(bands.venues(conn))
bands.play_in_venues('Madison Square Garden', '2024-12-31', conn)
print(bands.all_introductions(conn))
print(Band.most_performances(conn))

# Don't forget to close the connection
conn.close()