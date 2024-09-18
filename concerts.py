import psycopg2

class Concert:
    def __init__(self, concerts_id):
        self.concerts_id = concerts_id

    def bands(self, conn):
        query = """
        SELECT bands.* FROM bands
        JOIN concerts ON concerts.bands_id = bands.id
        WHERE concerts.id = %s
        """
        with conn.cursor() as cur:
            cur.execute(query, (self.concerts_id,))
            return cur.fetchone()

    def venues(self, conn):
        query = """
        SELECT venues.* FROM venues
        JOIN concerts ON concerts.venues_id = venues.id
        WHERE concerts.id = %s
        """
        with conn.cursor() as cur:
            cur.execute(query, (self.concert_id,))
            return cur.fetchone()

    def hometown_show(self, conn):
        query = """
        SELECT bands.hometown, venues.city 
        FROM concerts
        JOIN bands ON concerts.bands_id = bands.id
        JOIN venues ON concerts.venues_id = venues.id
        WHERE concerts.id = %s
        """
        with conn.cursor() as cur:
            cur.execute(query, (self.concerts_id,))
            result = cur.fetchone()
            return result[0] == result[1]

    def introduction(self, conn):
        query = """
        SELECT bands.name, bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.bands_id = bands.id
        JOIN venues ON concerts.venues_id = venues.id
        WHERE concerts.id = %s
        """
        with conn.cursor() as cur:
            cur.execute(query, (self.concerts_id,))
            result = cur.fetchone()
            return f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}"