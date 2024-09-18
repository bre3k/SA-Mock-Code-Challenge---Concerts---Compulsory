# CONCERT MANAGEMENT SYSTEM
This is a Python-based command-line application designed to manage concerts, bands, and venues using a PostgreSQL database. It allows users to retrieve data about concerts, bands, and venues, as well as insert and update information related to these entities.

# Project Overview
The application manages relationships between the following tables:

Bands: Contains information about musical bands.
Venues: Contains details about venues where concerts are held.
Concerts: Links bands to venues on specific dates.

# Key Features
Retrieve a list of concerts for a specific band or venue.
Retrieve details about which bands played at a particular venue.
Check if a concert is a hometown show for the band.
Create new concerts for bands at different venues.
Aggregate methods to find the most frequent performers at a venue or the band with the most performances.

# DATABASE STRUCTURE

# Tables
Bands
Fields:

id: Primary key
name: Name of the band
hometown: The band's hometown
# Venues
Fields:

id: Primary key
title: Name of the venue
city: City where the venue is located

# Concerts
Fields:

id: Primary key
bands_id: Foreign key to the bands table
venues_id: Foreign key to the venues table
date: Date of the concert

# Relationships
A band can perform at many venues, and a venue can host many bands through concerts.
Each concert links a band to a venue on a specific date.
 
 # SETUP INSTRUCTIONS
 # 1. Prerequisites
 
 Python 3.x
 PostgresSQL
 psycopg2 library for PosgresSQL connection (psycopg2-binary)
 a virtual environment

# 2. Installation
Clone the reposiory
Set up a virtual environment
Install the required packages
Setting up PostgreSQL database
Updating PostgresSQL connection details in main.py
Run the application


# CREATE A NEW DATABASE 
# Create tables
# Run the application:
python3 main.py


# How to Use
Concert.band(conn): Returns the band playing in a specific concert.
Concert.venue(conn): Returns the venue where the concert is taking place.
Venue.concerts(conn): Returns all concerts at a specific venue.
Venue.bands(conn): Returns all bands that have performed at a venue.
Band.concerts(conn): Returns all concerts a band has played.
Band.venues(conn): Returns all venues where a band has performed.
Concert.hometown_show(conn): Checks if a concert is a hometown show for the band.
Band.play_in_venue(venue, date, conn): Adds a new concert for a band at a venue.


# Known Issues
Ensurring that all table names and field names are correctly defined.
Ensurring PostgreSQL is running and connection details are correct in main.py.

