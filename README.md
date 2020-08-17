# MedCab
## Cannabis Suggestion Bot
### Robert Sharp
- August 2020


## User Input: STRINGS
- Random Strain
- Strain id
- Strain Name
- Desired Effect
- Desired Flavor

## Strain Object: JSON dict
- Strain Name
- Strain Type
- User Rating
- Effects List
- Flavors List
- Description Text
- Index Number


## Local Routes:

### Random Strain
- http://127.0.0.1:5000/

### List of Category Names
- http://127.0.0.1:5000/types
- http://127.0.0.1:5000/effects
- http://127.0.0.1:5000/flavors

### Strain Object Lookup Tables
- http://127.0.0.1:5000/strain-by-id/42
- http://127.0.0.1:5000/strain-by-name/Wedding%20Cake

### List of Strain Names having a given trait
- http://127.0.0.1:5000/strains-by-effect/Happy
- http://127.0.0.1:5000/strains-by-flavor/Sweet
- http://127.0.0.1:5000/strains-by-type/Sativa
