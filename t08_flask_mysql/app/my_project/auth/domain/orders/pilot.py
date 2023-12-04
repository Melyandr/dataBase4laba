"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.flight import Flight



class Pilot(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "pilot"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    calling = db.Column(db.String(30))
    age = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    flights_association = db.relationship("PilotHasFlight", backref="pilot")

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.calling}', '{self.age}, '{self.experience})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        pilot_flights = [Flight.put_into_dto(pilot_flight.flight) for pilot_flight in self.flights_association]
        return {
            "id": self.id,
            "calling": self.calling,
            "age": self.age,
            "experience": self.experience,
            "pilot_flights": pilot_flights,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Pilot:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Pilot(
            calling=dto_dict.get("calling"),
            age=dto_dict.get("age"),
            experience=dto_dict.get("experience"),
            pilot_flights=dto_dict.get("pilot_flights"),
        )
        return obj
