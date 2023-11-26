"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Route(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "route"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_country = db.Column(db.String(30))
    last_country = db.Column(db.String(30))
    marshrut_id = db.Column(db.Integer, db.ForeignKey('marshrut.id'), nullable=True)


    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.start_country}', '{self.last_country}, '{self.marshrut_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "calling": self.start_country,
            "age": self.last_country,
            "experience": self.marshrut_id,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Route:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Route(
            start_country=dto_dict.get("start_country"),
            last_country=dto_dict.get("last_country"),
            marshrut_id=dto_dict.get("marshrut_id"),

        )
        return obj
