"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Pilot


class PilotDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Pilot

    def ten_inserts_in_pilots(self):
        self._session.execute(text(
            f"call ten_inserts_in_pilot()"
        ))
        self._session.commit()
        return "inserted ten in_pilot "
