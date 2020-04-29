from .movement import ns as movement_namespace
from .camera import ns as camera_namespace


def initialise_routes(api):
    api.add_namespace(movement_namespace)
    api.add_namespace(camera_namespace)
