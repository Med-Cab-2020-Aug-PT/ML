# MedCab
### Cannabis Suggestion Bot
#### Robert Sharp
_August 2020_


## User Input: String
- Random Strain
- Strain id
- Strain Name
- Desired Effect
- Desired Flavor
- Desired Type

## Strain Object: JSON Dictionary
- Strain Name
- Strain Type
- User Rating (0.0 - 5.0)
- Effects List
- Flavors List
- Description Text
- Index Number (0 - 2154)
- Nearest: Similar Strain List


## Local Routes:

### Random Strain Object
- https://medcabin.herokuapp.com/
- https://medcabin.herokuapp.com/random-by-type/sativa
- https://medcabin.herokuapp.com/random-by-effect/happy
- https://medcabin.herokuapp.com/random-by-flavor/sweet

### List of all Strain Objects
- https://medcabin.herokuapp.com/strains

### List of Names
- https://medcabin.herokuapp.com/types
- https://medcabin.herokuapp.com/effects
- https://medcabin.herokuapp.com/flavors

### Strain Object Lookup Tables
- https://medcabin.herokuapp.com/strain-by-id/381
- https://medcabin.herokuapp.com/strain-by-name/fruit-loops

### List of Names
- https://medcabin.herokuapp.com/strains-by-effect/happy
- https://medcabin.herokuapp.com/strains-by-flavor/sweet
- https://medcabin.herokuapp.com/strains-by-type/sativa


# 4 Nearest Strains (NLP of Description KNN Model)
- https://medcabin.herokuapp.com/nearest/wedding-cake
