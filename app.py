from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthfusion.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ---------------- MODELS ------------------

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationship to User (doctors)
    doctors = db.relationship(
        "User",
        back_populates="department",
        foreign_keys="User.department_id"
    )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(30))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)

    # Explicitly specify which foreign key this relationship uses
    department = db.relationship(
        "Department",
        back_populates="doctors",
        foreign_keys=[department_id]
    )

    # Relationship to appointments
    appointments = db.relationship(
        "Appointment",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Treatment(db.Model):
    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key=True)
    treat_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Relationship to appointment
    appointment = db.relationship(
        "Appointment",
        back_populates="treatment"
    )


class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    status = db.Column(db.String(50), default='Booked', nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    treatment_id = db.Column(db.Integer, db.ForeignKey("treatments.id"), unique=True)

    user = db.relationship("User", back_populates="appointments")
    treatment = db.relationship("Treatment", back_populates="appointment")


# ---------------- RUN APP ------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        existing_admin = User.query.filter_by(username='admin').first()
        if not existing_admin:
            admin_user = User(
                username='admin',
                password='adminpass',
                email='abc@gmail.com',
                role='admin'
            )
            db.session.add(admin_user)
            db.session.commit()
    app.run(debug=True)
