"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Airplane(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "airplane"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lift_weight = db.Column(db.Integer)
    number_of_passenger = db.Column(db.Integer)
    plain_mileage = db.Column(db.String(30))
    average_speed = db.Column(db.String(30))
    aviacompany_id = db.Column(db.Integer, db.ForeignKey('aviacompany.id'), nullable=True)
    registration_id = db.Column(db.Integer, db.ForeignKey('registration.id'), nullable=True)


    # Relationship 1:M
    # client_type_id = db.Column(db.Integer, db.ForeignKey('client_type.id'), nullable=True)
    # client_type = db.relationship("ClientType", backref="clients")  # only on the child class

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.lift_weight}', '{self.number_of_passenger}, '{self.plain_mileage}," \
               f" '{self.average_speed}', '{self.aviacompany_id}', '{self.registration_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "lift_weight": self.lift_weight,
            "number_of_passenger": self.number_of_passenger,
            "plain_mileage": self.plain_mileage,
            "average_speed": self.average_speed,
            "aviacompany_id": self.aviacompany_id,
            "registration_id": self.registration_id,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Airplane:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Airplane(
            lift_weight=dto_dict.get("lift_weight"),
            number_of_passenger=dto_dict.get("number_of_passenger"),
            plain_mileage=dto_dict.get("plain_mileage"),
            average_speed=dto_dict.get("average_speed"),
            aviacompany_id=dto_dict.get("aviacompany_id"),
            registration_id=dto_dict.get("registration_id"),
        )
        return obj
