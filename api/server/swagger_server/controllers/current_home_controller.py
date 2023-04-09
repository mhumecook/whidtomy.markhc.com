import connexion
import six

from swagger_server.models.home import Home  # noqa: E501
from swagger_server.models.particle import Particle  # noqa: E501
from swagger_server import util


def create_current_home(body):  # noqa: E501
    """Create the default home

    Create the basic information about the home for this installation of the application.  We create pretty fundamental information at this level, relating to the address and the purchase details. # noqa: E501

    :param body: The home that is being created
    :type body: dict | bytes

    :rtype: Home
    """
    if connexion.request.is_json:
        body = Home.from_dict(connexion.request.get_json())  # noqa: E501
    return body


def create_particle(body):  # noqa: E501
    """Create a particle in the home

    This is the way we create a new room, or a new garage, or a new yard, or a new stable in the current home. # noqa: E501

    :param body: The home that is being created
    :type body: dict | bytes

    :rtype: Particle
    """
    if connexion.request.is_json:
        body = Particle.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_particles():  # noqa: E501
    """Retrieve the particles of the home

    The particles of the home are what the home is made up of.  I admit that this is not a great name for the rooms and buildings and yards and other things that make up the home.  I wanted to call them components, but the OpenAPI document has components already in it, so I chose another name - particles. # noqa: E501


    :rtype: Particle
    """
    return 'do some magic!'


def get_current_home():  # noqa: E501
    """Retrieve information about the home

    Access the basic information about the home for this installation of the application.  We get pretty fundamental information at this level, relating to the address and the purchase details. # noqa: E501


    :rtype: Home
    """
    return 'do some magic!'


def get_particle_with_id(particle_id):  # noqa: E501
    """Retrieve a given particle of the home

    Get a given particle of the current home, given its id. # noqa: E501

    :param particle_id: Numeric id of the particle to update
    :type particle_id: int

    :rtype: Particle
    """
    return 'do some magic!'


def update_particle_with_id(body):  # noqa: E501
    """Update a particle in the home

    Update a particle in the current home. # noqa: E501

    :param body: The home that is being created
    :type body: dict | bytes

    :rtype: Particle
    """
    if connexion.request.is_json:
        body = Particle.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
