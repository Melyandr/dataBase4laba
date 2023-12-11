"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import ClientType


class ClientTypeDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = ClientType


    def create_database(self):

        try:
            self._session.execute(text(
                f"call create_database()"
            ))
            self._session.commit()
            print("if print")
            return "create_database"
        except Exception as e:
            self._session.rollback()
            print("except print")
            return f"Error: {str(e)}"