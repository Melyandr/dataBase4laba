"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Flight(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=True)
    airplane_id = db.Column(db.Integer, db.ForeignKey('airplane.id'), nullable=True)
    pilots_association = db.relationship("PilotHasFlight", backref="flight")
    dispatchers_association = db.relationship("DispatcherHasFlight", backref="flight")
    air_hostess_association = db.relationship("AirHostessHasFlight", backref="flight")

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.start_time}', '{self.end_time}, '{self.route_id}, '{self.airplane_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        flight_pilot = [{
            "id": flight_pilot.pilot.id,
            "calling": flight_pilot.pilot.calling,
            "age": flight_pilot.pilot.age,
            "experience": flight_pilot.pilot.experience,

        } for flight_pilot in self.pilots_association]
        return {
            "id": self.id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "route_id": self.route_id,
            "airplane_id": self.airplane_id,
            "flight_pilot": flight_pilot,
        }



    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Flight:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Flight(
            start_time=dto_dict.get("start_time"),
            end_time=dto_dict.get("end_time"),
            route_id=dto_dict.get("route_id"),
            airplane_id=dto_dict.get("airplane_id"),

        )
        return obj
