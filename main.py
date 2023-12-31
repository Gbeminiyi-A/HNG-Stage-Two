from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI", "sqlite:///stage_two.db")


db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    value = db.Column(db.String, )

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify(status={"success": 200})


@app.route("/api")
def all_data():
    results = db.session.execute(db.select(User)).scalars().all()
    return jsonify(users=[user.to_dict() for user in results])


@app.route("/api", methods=['GET', 'POST'])
def add_user():
    name = request.args.get('name')
    value = request.args.get('value')
    new_user = User(name=name, value=value)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(
        status={
            "success": "successfully added the new user to the database"
        }
    )


@app.route("/api/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user=user.to_dict())
    return jsonify(
        status={"error": "User not found, Ensure the id is correct"}
    )


@app.route("/api/<int:user_id>", methods=['GET', 'DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            status={"success": "successfully deleted the user"}
        )
    return jsonify(
        status={"error": "Could not delete user, Check if user exists and confirm id."}
    )


@app.route("/api/<int:user_id>", methods=['GET', 'PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    name = request.args.get('name')
    value = request.args.get("value")

    if user:
        user.name = user.name if name is None else name
        user.value = user.value if value is None else value

        db.session.commit()
        return jsonify(
            status={"success": "successfully updated the user info."}
        )
    return jsonify(
        status={"error": "No user with that id was found"}
    )


if __name__ == "__main__":
    app.run(debug=True)
