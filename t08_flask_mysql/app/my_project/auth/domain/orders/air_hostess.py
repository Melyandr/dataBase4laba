"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db

from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Air_hostess(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "air_hostess"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(30))
    flights_association = db.relationship("AirHostessHasFlight", backref="air_hostess")
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.gender}', '{self.age}, '{self.email})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        air_hostess_flights = [air_hostess_flight.flight.put_into_dto() for air_hostess_flight in self.flights_association]
        return {
            "id": self.id,
            "gender": self.gender,
            "age": self.age,
            "email": self.email,
            "air_hostess_flights": air_hostess_flights,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Air_hostess:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Air_hostess(
            gender=dto_dict.get("gender"),
            age=dto_dict.get("age"),
            email=dto_dict.get("email"),
            air_hostess_flights=dto_dict.get("air_hostess_flights"),
        )
        return obj
