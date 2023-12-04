"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.aeroport import Aeroport


class Marshrut(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "marshrut"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(30))
    aeroport_id = db.Column(db.Integer, db.ForeignKey('aeroport.id'), nullable=False)
    aeroport_id2 = db.Column(db.Integer, db.ForeignKey('aeroport.id'), nullable=False)
    aeroport_1 = db.relationship('Aeroport', foreign_keys=[aeroport_id])
    aeroport_2 = db.relationship('Aeroport', foreign_keys=[aeroport_id2])

    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.country}', '{self.aeroport_id}, '{self.aeroport_id2})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        aeroports_info = Aeroport.put_into_dto(self.aeroport_1)

        aeroports2_info = Aeroport.put_into_dto(self.aeroport_2)

        return {
            "id": self.id,
            "country": self.country,
            "aeroport_id": aeroports_info,
            "aeroport_id2": aeroports2_info,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Marshrut:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Marshrut(
            country=dto_dict.get("country"),
            aeroport_id=dto_dict.get("aeroport_id"),
            aeroport_id2=dto_dict.get("aeroport_id2"),

        )
        return obj
