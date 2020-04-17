from .movement import ns as movement_namespace


def initialise_routes(api):
    api.add_namespace(movement_namespace)