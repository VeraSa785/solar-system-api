from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    distance_from_sun_million_mi = db.Column(db.Float)
    length_of_year_earth_days = db.Column(db.Float)