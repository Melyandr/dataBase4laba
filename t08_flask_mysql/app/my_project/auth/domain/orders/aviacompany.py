"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.airplane import Airplane


class ClientType(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "aviacompany"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(30))
    country_of_company: str = db.Column(db.String(30))
    airplanes = db.relationship('Airplane', backref='aviacompany')

    def __repr__(self) -> str:
        return f"Aviacompany({self.id}, '{self.name}' , {self.country_of_company})"

    # def put_into_dto(self) -> Dict[str, Any]:
    #     """
    #     Puts domain object into DTO without relationship
    #     :return: DTO object as dictionary
    #     """
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "country_of_company": self.country_of_company,
    #         "airplanes": self.airplanes,
    #     }

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO with handled relationship
        :return: DTO object as dictionary
        """
        airplanes_info = []
        for airplane in self.airplanes:
            airplane_dto = Airplane.put_into_dto(airplane)
            airplanes_info.append(airplane_dto)

        return {
            "id": self.id,
            "name": self.name,
            "country_of_company": self.country_of_company,
            "airplanes": airplanes_info,
        }
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ClientType:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ClientType(
            name=dto_dict.get("name"),
            country_of_company=dto_dict.get("country_of_company"),

)
        return obj
