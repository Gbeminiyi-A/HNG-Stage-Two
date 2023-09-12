from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stage_two.db"

db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)
    school = db.Column(db.String)
    d_o_b = db.Column(db.String)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return jsonify(status={"success": 200})


@app.route("/users")
def all_data():
    results = db.session.execute(db.select(User)).scalars().all()
    api_key = request.args.get("api_key")
    if api_key == "supersupersecretkey":
        return jsonify(users=[user.to_dict() for user in results])
    return jsonify(
        status={"error": "You can't access this data. You either have a wrong api key or none at all"}
    )


@app.route("/api", methods=['GET', 'POST'])
def add_user():
    name = request.args.get('name')
    email = request.args.get('email')
    age = request.args.get('age')
    school = request.args.get('school')
    d_o_b = request.args.get("D_O_B")

    check_email = User.query.get(email)

    if check_email:
        return jsonify(
            status={"error": "A user with that email already exists."}
        )

    new_user = User(
        name=name,
        email=email,
        age=age,
        school=school,
        d_o_b=d_o_b
    )

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


@app.route("/api/delete/<int:user_id>", methods=['GET', 'DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    api_key = request.args.get("api_key")
    if api_key == "supersupersecretkey":
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify(
                status={"success": "successfully deleted the user"}
            )
        return jsonify(
            status={"error": "Could not delete user, Check if user exists and confirm id."}
        )
    return jsonify(
        status={"error": "You are not authorized to delete a users data. You either have a wrong apikey or none at all"}
    )


@app.route("/api/update-user/<int:user_id>", methods=['GET', 'PATCH'])
def update_user(user_id):
    user = User.query.get(user_id)
    name = request.args.get('name')
    email = request.args.get('email')
    age = request.args.get('age')
    school = request.args.get('school')
    d_o_b = request.args.get('D_O_B')

    if user:
        user.name = user.name if name is None else name
        user.email = user.email if email is None else email
        user.age = user.age if age is None else age
        user.school = user.school if school is None else school
        user.d_o_b = user.d_o_b if d_o_b is None else d_o_b

        db.session.commit()
        return jsonify(
            status={"success": "successfully updated the user info."}
        )
    return jsonify(
        status={"error": "No user with that id was found"}
    )


if __name__ == "__main__":
    app.run(debug=True)
