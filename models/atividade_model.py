from database import db
from errors import ProfessorNotExist, NoActivityRegistered
import requests

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    professor_id = db.Column(db.Integer, nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)
    delivery_date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __init__(self, professor_id, activity_type, delivery_date, title, description):
        self.professor_id = professor_id
        self.activity_type =  activity_type
        self.delivery_date = delivery_date
        self.title = title
        self.description = description

    def verify_professor(professor_id):
        res = requests.get(f"http://localhost:5000/professores/{professor_id}")
        if res.status_code != 200:
            raise ProfessorNotExist('Professor não encontrado.')

    def to_dict(self):
        return {
            "id": self.id,
            "professor_id": self.professor_id,
            "activity_type": self.activity_type,
            "delivery_date": self.delivery_date,
            "title": self.title,
            "description": self.description
        }
    
def addActivity(data):
    professor_id = data["professor_id"]

    Activity.verify_professor(professor_id)
    
    activity = Activity(
        professor_id=professor_id,
        activity_type=data["activity_type"],
        delivery_date=data["delivery_date"],
        title=data["title"],
        description=data["description"]
    )
    
    db.session.add(activity)
    db.session.commit()

def getActivities():
    activities = Activity.query.all()
    return [activity.to_dict() for activity in activities]

def getActivitiesByProfessorId(professor_id):
    Activity.verify_professor(professor_id)

    activities = Activity.query.filter_by(professor_id=professor_id).order_by(Activity.id.asc()).all()
    if len(activities) == 0:
        raise NoActivityRegistered('O professor ainda não registrou nenhuma atividade.')
    
    return [activity.to_dict() for activity in activities]