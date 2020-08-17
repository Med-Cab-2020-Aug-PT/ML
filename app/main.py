from flask import Flask, jsonify
from app.data import StrainData


""" One Ring to rule them all, and in the darkness - bind them! """
Ring = Flask(__name__)
Ring.data = StrainData(filename='data/cannabis.csv')


@Ring.route('/')
@Ring.route('/random')
@Ring.route('/index.html')
def index():
    """ Default Endpoint - Returns a random Strain
    @return: JSON object
    """
    return jsonify(Ring.data.random_strain())


@Ring.route('/strain-by-id/<idx>', methods=['GET'])
def strain_by_id(idx: str):
    """ Strain Details, Id Lookup Table
    @param idx: String, index of desired strain
    @return: JSON object, Strain Details
    """
    return jsonify(Ring.data.strain_by_id(idx))


@Ring.route('/strain-by-name/<name>', methods=['GET'])
def strain_by_name(name: str):
    """ Strain Details, Name Lookup Table.
    @param name: String
    @return: JSON Obj: dict
    """
    return jsonify(Ring.data.strain_by_name(name))


@Ring.route('/strains')
def strains():
    """ Returns a JSON dictionary of Strains
    @return: JSON Obj: Dict[Dict] """
    return jsonify(Ring.data.name_lookup)


@Ring.route('/types')
def strain_types():
    """ Returns a list of all types
    @return: JSON Obj: List[String]
    """
    return jsonify(Ring.data.types_list())


@Ring.route('/effects')
def strain_effects():
    """ Returns a list of all effects
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.effects_list())


@Ring.route('/flavors')
def strain_flavors():
    """ Returns a list of all flavors
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.flavors_list())


@Ring.route('/strains-by-effect/<effect>', methods=['GET'])
def strains_by_effect(effect):
    """ Returns a list of Strain names.
    @param effect: str
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.strains_by_effect(effect.title()))


@Ring.route('/strains-by-flavor/<flavor>', methods=['GET'])
def strains_by_flavor(flavor):
    """ Returns a list of Strain names.
    @param flavor: str
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.strains_by_flavor(flavor.title()))


@Ring.route('/strains-by-type/<strain_type>', methods=['GET'])
def strains_by_type(strain_type):
    """ Returns a list of Strain names.
    @param strain_type: str
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.strains_by_type(strain_type.lower()))


@Ring.route('/random-by-type/<strain_type>', methods=['GET'])
def random_by_type(strain_type):
    """ Random Strain by Type

    @param strain_type: str
    @return: JSON Obj
    """
    return jsonify(
        Ring.data.strain_by_name(Ring.data.random_by_type(strain_type.title())))


@Ring.route('/random-by-effect/<effect>', methods=['GET'])
def random_by_effect(effect):
    """ Random Strain by Effect

    @param effect: str
    @return: JSON Obj
    """
    return jsonify(
        Ring.data.strain_by_name(Ring.data.random_by_effect(effect.title())))


@Ring.route('/random-by-flavor/<flavor>', methods=['GET'])
def random_by_flavor(flavor):
    """ Random Strain by Flavor

    @param flavor: str
    @return: JSON Obj
    """
    return jsonify(
        Ring.data.strain_by_name(Ring.data.random_by_flavor(flavor.title())))


if __name__ == '__main__':
    """
    # Local Routes:
    
    # Random Strain Object
    http://127.0.0.1:5000/
    http://127.0.0.1:5000/random-by-type/sativa
    http://127.0.0.1:5000/random-by-effect/happy
    http://127.0.0.1:5000/random-by-flavor/sweet
    
    # List of all Strains
    http://127.0.0.1:5000/strains

    # List of Names
    http://127.0.0.1:5000/types
    http://127.0.0.1:5000/effects
    http://127.0.0.1:5000/flavors
    
    # Strain Object Lookup Tables
    http://127.0.0.1:5000/strain-by-id/381
    http://127.0.0.1:5000/strain-by-name/Fruit%20Loops
    
    # List of Names:
    http://127.0.0.1:5000/strains-by-effect/happy
    http://127.0.0.1:5000/strains-by-flavor/sweet
    http://127.0.0.1:5000/strains-by-type/sativa
    """
    Ring.run(debug=True)
