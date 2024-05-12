from app.database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    picture_url = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    environmental_impact = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.price}')"