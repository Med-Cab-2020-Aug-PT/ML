""" MedCab Project
Data Science Unit 4 Build Week
Robert Sharp
August 2020
"""
from flask import Flask, jsonify, request, make_response
from app.data import StrainData


""" One Ring to rule them all, and in the darkness - bind them! """
filename = 'data/cannabis.csv'
Ring = Flask(__name__)
Ring.data = StrainData(filename)


@Ring.route('/search/<user_input>')
def recommend(user_input):
    """ Search Route """
    return jsonify(Ring.data.recommend(user_input))


@Ring.route('/')
@Ring.route('/random')
def index():
    """ Returns a random Strain
    @return: JSON object
    """
    return jsonify(Ring.data.random_strain())


@Ring.route('/id/<idx>')
def strain_by_id(idx: str):
    """ Strain Details, Id Lookup Table
    @param idx: String, index of desired strain
    @return: JSON object, Strain Details
    """
    return jsonify(Ring.data.strain_by_id(idx))


@Ring.route('/<name>')
def strain_by_name(name: str):
    """ Strain Details, Name Lookup Table.
    @param name: String
    @return: JSON Obj: dict
    """
    clean_name = name.replace('-', ' ').title()
    return jsonify(Ring.data.strain_by_name(clean_name))


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


@Ring.route('/strains-by-effect/<effect>')
def strains_by_effect(effect):
    """ Returns a list of Strain names.
    @param effect: str
    @return: JSON Obj: List[str]
    """
    clean_name = effect.replace('-', ' ').title()
    return jsonify(Ring.data.strains_by_effect(clean_name))


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
    return jsonify(Ring.data.strains_by_type(strain_type.title()))


@Ring.route('/random-by-type/<strain_type>')
def random_by_type(strain_type):
    """ Random Strain by Type
    @param strain_type: str
    @return: JSON Obj
    """
    return jsonify(
        Ring.data.strain_by_name(Ring.data.random_by_type(strain_type.title()))
    )


@Ring.route('/random-by-effect/<effect>')
def random_by_effect(effect):
    """ Random Strain by Effect
    @param effect: str
    @return: JSON Obj
    """
    clean_name = effect.replace('-', ' ').title()
    return jsonify(
        Ring.data.strain_by_name(Ring.data.random_by_effect(clean_name))
    )


@Ring.route('/random-by-flavor/<flavor>')
def random_by_flavor(flavor):
    """ Random Strain by Flavor
    @param flavor: str
    @return: JSON Obj
    """
    return jsonify(
        Ring.data.strain_by_name(Ring.data.random_by_flavor(flavor.title()))
    )


@Ring.route('/nearest/<name>')
def nearest(name: str):
    """ Returns the 5 Nearest Strains
    @param name: str
    @return: JSON List[Dict]
    """
    clean_name = name.replace('-', ' ').title()
    if clean_name in Ring.data.name_lookup.keys():
        strain_names = Ring.data.strain_by_name(clean_name)['Nearest']
        return jsonify([
            Ring.data.strain_by_name(strain)
            for strain in strain_names
        ])
    else:
        return jsonify(f"Unknown Strain: {clean_name}")


@Ring.before_request
def before_request():
    """ CORS preflight, required for off-server access """

    def _build_cors_prelight_response():
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    if request.method == "OPTIONS":
        return _build_cors_prelight_response()


@Ring.after_request
def after_request(response):
    """ CORS headers, required for off-server access """
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    """
    ## Local Routes:
    
    ### Primary URL
    - http://127.0.0.1:5000/
    
    ### Strain Object Lookup Tables
    - http://127.0.0.1:5000/strain-by-id/381
    - http://127.0.0.1:5000/strain-by-name/fruit-loops
    
    ### Random Strain Object
    - http://127.0.0.1:5000/random-by-type/sativa
    - http://127.0.0.1:5000/random-by-effect/happy
    - http://127.0.0.1:5000/random-by-flavor/sweet
    
    ### List of Names by Category
    - http://127.0.0.1:5000/types
    - http://127.0.0.1:5000/effects
    - http://127.0.0.1:5000/flavors
    
    ### List of Names by Subcategory
    - http://127.0.0.1:5000/strains-by-effect/happy
    - http://127.0.0.1:5000/strains-by-flavor/sweet
    - http://127.0.0.1:5000/strains-by-type/sativa
    
    ### Five Most Similar Strains - NLP KNN Model
    - http://127.0.0.1:5000/nearest/wedding-cake
    """
    Ring.run(debug=True, port=5050)
