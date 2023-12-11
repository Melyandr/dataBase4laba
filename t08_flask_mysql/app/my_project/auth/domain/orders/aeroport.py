"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto
from t08_flask_mysql.app.my_project.auth.domain.orders.dispatcher import Dispatcher

class Aeroport(db.Model, IDto):
    """
    Model declaration for Airport entity.
    """
    __tablename__ = "aeroport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    name = db.Column(db.String(100))
    # maarshruts = db.relationship('Marshrut', backref='aeroport')
    maarshruts_1 = db.relationship('Marshrut', foreign_keys='Marshrut.aeroport_id', backref='aeroport_from_1')
    maarshruts_2 = db.relationship('Marshrut', foreign_keys='Marshrut.aeroport_id2', backref='aeroport_from_2')
    dispatchers = db.relationship('Dispatcher', backref='aeroport')

    def __repr__(self) -> str:
        return f"Airport({self.id}, '{self.name}', '{self.city}', '{self.country}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        dispatchers_info = []
        for dispatcher in self.dispatchers:
            dispatcher_dto = Dispatcher.put_into_dto(dispatcher)
            dispatchers_info.append(dispatcher_dto)

        return {
            "id": self.id,
            "country": self.country,
            "city": self.city,
            "name": self.name,
            "dispatchers": dispatchers_info,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Aeroport:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Aeroport(
            country=dto_dict.get("country"),
            city=dto_dict.get("city"),
            name=dto_dict.get("name"),

        )
        return obj
