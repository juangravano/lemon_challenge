# lemon_challenge
api nasa automation 
- python
- pytest

instalación, ejecución de test y creación de reporte automático:
1. git clone https://github.com/juangravano/lemon_challenge.git
2. cd lemon_challenge
3. pip install -r requirements.txt
4. python -m pytest test/ --html=report/report.html --self-contained-html

estructura del proyecto:

  src:
  - api.api_client: Clase para invocar a los métodos http
  - api.nasa_api: Clase base de la API a testear
  - api.helpers: Abstracción de lógica para los test
  
  test:
  - archivo con test por cada endpoint a testear
  
  report:
  - reporte html generado automáticamente en la ejecución.
