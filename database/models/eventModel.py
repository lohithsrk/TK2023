from database.database import db
import uuid


class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    rules = db.Column(db.String(5000))

    def __init__(self, data):
        self.event_id = str(uuid.uuid4())
        self.event_name = data["event_name"]
        self.batches = data["batches"]
        self.rules = data["rules"]

    def getAllEvents():
        return Events.query.all()

    def getSingleEvent(event_id):
        return Events.query.filter(Events.event_id == event_id).first().toJSON()
