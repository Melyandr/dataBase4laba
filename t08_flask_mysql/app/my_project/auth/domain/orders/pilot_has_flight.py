"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class PilotHasFlight(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "pilot_has_flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pilot_id = db.Column(db.Integer, db.ForeignKey('pilot.id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'), nullable=False)
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"pilot_has_flight({self.id}, '{self.pilot_id}', '{self.flight_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "pilot_id": self.pilot_id,
            "flight_id": self.flight_id,


        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PilotHasFlight:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = PilotHasFlight(
            pilot_id=dto_dict.get("pilot_id"),
            flight_id=dto_dict.get("flight_id"),


        )
        return obj
