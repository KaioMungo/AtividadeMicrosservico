from config import app, db
from controllers.atividade_controller import activity

app.register_blueprint(activity)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)