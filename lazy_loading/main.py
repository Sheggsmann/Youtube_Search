# from flask import Flask, render_template, jsonify, make_response, request
# import random
# import time

# app = Flask(__name__)

# heading = 'Lorem ipsum dolor sit amet'

# content = """
# lorem ipsum dolor sit amet consectetur adispicsing elit repellat inventore assumenda loboriturm
# obcateri saepe pariatur atque est quam moles init
# """

# db = list()

# posts = 200
# quantity = 10

# for i in range(posts):
#     heading_parts = heading.split(" ")
#     random.shuffle(heading_parts)

#     content_parts = content.split(" ")
#     random.shuffle(content_parts)

#     db.append([i, " ".join(heading_parts), " ".join(content_parts)])


# @app.route('')
# def index():
#     return render_template('index.html')


# @app.route('/load')
# def load():
#     time.sleep(0.2)
#     if request.args:
#         counter = int(request.args.get('c'))

#         if counter == 0:
#             res = make_response(jsonify(db[0: quantity]), 200)
#         elif counter == posts:
#             res.make_response(jsonify({}), 200)
#         else:
#             res = make_response(jsonify(db[counter: counter + quantity]), 200)

#     return res
    






from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim


longitude = []
latitude = []


def findGeocode(city):
    try:
        geolocator = Nominatim(user_agent='promise')
        return geolocator.geocode(city)
    except GeocoderTimedOut:
        return findGeocode(city)


city = input('City name: ')

print(findGeocode(city))

