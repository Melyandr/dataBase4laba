"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.registration_route import client_bp
    from .orders.aviacompany_route import client_type_bp
    from .orders.pilot_route import pilot_bp
    from .orders.air_hostess_route import air_hostess_bp
    from .orders.aeroport_route import aeroport_bp
    from .orders.dispatcher_route import dispatcher_bp
    from .orders.marshrut_route import marshrut_bp
    from .orders.route_route import route_bp
    from .orders.airplane_route import airplane_bp
    from .orders.flight_route import flight_bp
    from .orders.dispatcher_has_flight_route import dispatcherHasFlight_bp
    from .orders.pilot_has_flight_route import pilotHasFlight_bp
    from .orders.air_hostess_has_flight_route import airHostessHasFlight_bp
    # додати всі шляхи з ордерс

    app.register_blueprint(client_bp)
    app.register_blueprint(client_type_bp)
    app.register_blueprint(pilot_bp)
    app.register_blueprint(air_hostess_bp)
    app.register_blueprint(aeroport_bp)
    app.register_blueprint(dispatcher_bp)
    app.register_blueprint(marshrut_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(airplane_bp)
    app.register_blueprint(flight_bp)
    app.register_blueprint(dispatcherHasFlight_bp)
    app.register_blueprint(pilotHasFlight_bp)
    app.register_blueprint(airHostessHasFlight_bp)