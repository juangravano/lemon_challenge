# lemon_challenge :lemon:
api nasa automation 
- python
- pytest

## :robot: instalaci贸n, ejecuci贸n de test y creaci贸n de reporte autom谩tico:
1. git clone https://github.com/juangravano/lemon_challenge.git
2. cd lemon_challenge
3. pip install -r requirements.txt
4. python -m pytest test/ --html=report/report.html --self-contained-html

## :pushpin: estructura del proyecto:

  ## 馃搷src:
  - api.api_client: Clase para invocar a los m茅todos http
  - api.nasa_api: Clase base de la API a testear
  - api.helpers: Abstracci贸n de l贸gica para los test
  
  ## 馃搷 test:
  - archivo con test por cada endpoint a testear
  
  ## 馃搷 report:
  - reporte html generado autom谩ticamente en la ejecuci贸n.

https://docs.google.com/presentation/d/1Oa33t4nSa3T408oLL66yrL3PByrP-ju8-McWOWXsO2c/edit?usp=sharing
