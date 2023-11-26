"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.airplane import Airplane


class Client(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "registration"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String(30))
    country_of_registration = db.Column(db.String(50))
    airplanes = db.relationship('Airplane', backref='registrations')
    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.owner}', '{self.country_of_registration})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary

        """
        airplanes_info = []
        for airplane in self.airplanes:
            airplane_dto = Airplane.put_into_dto(airplane)
            airplanes_info.append(airplane_dto)
        return {
            "id": self.id,
            "name": self.owner,
            "country_of_registration": self.country_of_registration,
            "airplanes": airplanes_info,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Client(
            owner=dto_dict.get("owner"),
            country_of_registration=dto_dict.get("country_of_registration"),
            airplanes=dto_dict.get("airplanes"),

        )
        return obj
