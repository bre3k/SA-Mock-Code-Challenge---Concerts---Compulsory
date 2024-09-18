class Band:
    def __init__(self, bands_id):
        self.bands_id = bands_id

    def concerts(self, conn):
        query = "SELECT * FROM concerts WHERE bands_id = %s"
        with conn.cursor() as cur:
            cur.execute(query, (self.bands_id,))
            return cur.fetchall()

    def venues(self, conn):
        query = """
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON concerts.venues_id = venues.id
        WHERE concerts.bands_id = %s
        """
        with conn.cursor() as cur:
            cur.execute(query, (self.bands_id,))
            return cur.fetchall()

    def play_in_venues(self, venues_title, date, conn):
        # Get the next available ID
        query_get_max_id = "SELECT COALESCE(MAX(id), 0) + 1 FROM concerts"
        with conn.cursor() as cur:
            cur.execute(query_get_max_id)
            new_id = cur.fetchone()[0]

        # Insert a new concert with the new ID
        query_insert = """
        INSERT INTO concerts (id, bands_id, venues_id, date)
        SELECT %s, %s, venues.id, %s
        FROM venues
        WHERE venues.title = %s
        """
        with conn.cursor() as cur:
            cur.execute(query_insert, (new_id, self.bands_id, date, venues_title))
            conn.commit()

    def all_introductions(self, conn):
        query = """
        SELECT bands.name, bands.hometown, venues.city 
        FROM concerts
        JOIN bands ON concerts.bands_id = bands.id
        JOIN venues ON concerts.venues_id = venues.id
        WHERE concerts.bands_id = %s
        """
        with conn.cursor() as cur:
            cur.execute(query, (self.bands_id,))
            introductions = cur.fetchall()
            return [
                f"Hello {intro[2]}!!!!! We are {intro[0]} and we're from {intro[1]}"
                for intro in introductions
            ]

    @staticmethod
    def most_performances(conn):
        query = """
        SELECT bands.*, COUNT(concerts.id) AS num_performances
        FROM concerts
        JOIN bands ON concerts.bands_id = bands.id
        GROUP BY bands.id
        ORDER BY num_performances DESC
        LIMIT 1
        """
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchone()