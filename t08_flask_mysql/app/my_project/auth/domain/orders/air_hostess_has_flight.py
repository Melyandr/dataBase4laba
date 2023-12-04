"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class AirHostessHasFlight(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "air_hostess_has_flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    air_hostess_id = db.Column(db.Integer, db.ForeignKey('air_hostess.id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"air_hostess_has_flight({self.id}, '{self.air_hostess_id}', '{self.flight_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "air_hostess_id": self.air_hostess.put_into_dto(), #переводить в словник і дозволяє побачити
            "flight_id": self.flight.put_into_dto(),


        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AirHostessHasFlight:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AirHostessHasFlight(
            air_hostess_id=dto_dict.get("air_hostess_id"),
            flight_id=dto_dict.get("flight_id"),


        )
        return obj
