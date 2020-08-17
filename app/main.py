from flask import Flask, jsonify
from app.data import StrainData


""" One Ring to rule them all, and in the darkness - bind them! """
Ring = Flask(__name__)
Ring.data = StrainData(filename='data/cannabis.csv')


@Ring.route('/')
@Ring.route('/index.html')
def index():
    """ Default Endpoint - Returns a random Strain
    @return: JSON object
    """
    return jsonify(Ring.data.random_strain())


@Ring.route('/strain-by-id/<idx>', methods=['GET'])
def strain_by_id(idx: str):
    """ Strain Details, Id Lookup Table
    @param idx: id of desired strain
    @return: JSON object, Strain Details
    """
    return jsonify(Ring.data.strain_by_id(idx))


@Ring.route('/strain-by-name/<name>', methods=['GET'])
def strain_by_name(name: str):
    """ Strain Details, Name Lookup Table.
    @param name: str
    @return: JSON Obj: dict
    """
    return jsonify(Ring.data.strain_by_name(name))


@Ring.route('/types')
def strain_types():
    """ Returns a list of all types
    @return: JSON Obj: List[str]
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


@Ring.route('/strains-by-effect/<effect>')
def strains_by_effect(effect):
    """ Returns a list of Strain names.
    @param effect: str
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.strains_by_effect(effect.title()))


@Ring.route('/strains-by-flavor/<flavor>')
def strains_by_flavor(flavor):
    """ Returns a list of Strain names.
    @param flavor: str
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.strains_by_flavor(flavor.title()))


@Ring.route('/strains-by-type/<strain_type>')
def strains_by_type(strain_type):
    """ Returns a list of Strain names.
    @param strain_type: str
    @return: JSON Obj: List[str]
    """
    return jsonify(Ring.data.strains_by_type(strain_type.lower()))


if __name__ == '__main__':
    """
    # Local Routes:
    
    # Random Strain Object
    http://127.0.0.1:5000/
    
    # List of Names
    http://127.0.0.1:5000/types
    http://127.0.0.1:5000/effects
    http://127.0.0.1:5000/flavors
    
    # Strain Object Lookup Tables
    http://127.0.0.1:5000/strain-by-id/42
    http://127.0.0.1:5000/strain-by-name/Wedding%20Cake
    
    # List of Names:
    http://127.0.0.1:5000/strains-by-effect/Happy
    http://127.0.0.1:5000/strains-by-flavor/Sweet
    http://127.0.0.1:5000/strains-by-type/Sativa
    """
    Ring.run(debug=True)
