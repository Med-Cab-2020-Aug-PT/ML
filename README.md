# MedCab
### Cannabis Suggestion Bot
#### Jisha Obukwelu & Robert Sharp
_August 2020_ 


## Cannabis Strain: JSON Object
- Strain: Name
- Type: Family (Sativa, Indica, Hybrid)
- Rating: Float (0.0 - 5.0)
- Effects: List
- Flavors: List
- Description: Text
- Index: Integer (0 - 2154)
- Nearest: List


## Public Endpoints:

### Primary URL
- https://medcabin.herokuapp.com/
- https://medcabin.herokuapp.com/search/<arbitrary_user_text>

### Strain Object Lookup Tables
- https://medcabin.herokuapp.com/id/381
- https://medcabin.herokuapp.com/fruit-loops

### Random Strain Object
- https://medcabin.herokuapp.com/random
- https://medcabin.herokuapp.com/random/type/sativa
- https://medcabin.herokuapp.com/random/effect/happy
- https://medcabin.herokuapp.com/random/flavor/sweet

### List of Names by Category
- https://medcabin.herokuapp.com/effects
- https://medcabin.herokuapp.com/flavors
- https://medcabin.herokuapp.com/types

### List of Names by Subcategory
- https://medcabin.herokuapp.com/effect/happy
- https://medcabin.herokuapp.com/flavor/sweet
- https://medcabin.herokuapp.com/type/sativa

### Five Most Similar Strains - NLP KNN Model
- https://medcabin.herokuapp.com/nearest/wedding-cake
