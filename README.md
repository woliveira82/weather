# Weather

This is a simple application that works as a wrapper for the [Open Weather API](https://openweathermap.org/current) that returns a city's current temperature.

This application was coded in **[Python 3.8](https://www.python.org/)** and **[Flask](https://flask.palletsprojects.com/)**.

## 1. Instalation
You can clone the repository localy with *Git*. Follow this [link](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) if you need some help with the basic Git commands.
You must have Python 3.8 installed to use this app and the **[Python Package Index](https://pypi.org/)** to install the dependencies.

### 1.1 Requirements
Create a virtual environment for the application and activate it.
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
Install all requirements listed in the `requirements.txt` file:
```bash
(venv)$ pip3 install -m requirements.txt
```
Duplicate the `.env.example` cahnge its name for `.env` and set up the variables on it. You will need a Open Weather API key. You wanting a development environment, the `.env` file should looks like this:
```bash
FLASK_ENV=development
FLASK_DEBUG=1
CACHE_DEFAULT_TIMEOUT=300
DEFAULT_MAX_NUMBER=5
OPEN_WEATHER_API_KEY=0123456789abcdef0123456789abcdef
```

### 1.2 Running
Start the application executing the `run.py` file:
```bash
(venv) $ python run.py
 * Serving Flask app "app" (lazy loading)
 * Environment: develop
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```
In this case, the server was started locally, and can be accessed throw the port 5000.

## 2. Using
The application creates two endpoints:
#### GET `/api/v1/temperature/<city_name>`
This endpoint will search a city with the name `city_name` and returns a JSON with the current weather of the city.
##### Response format example
```json
{
  "avg": 281.06, 
  "city": {
    "country": "GB", 
    "name": "London"
  }, 
  "feels_like": 278.52, 
  "max": 282.53, 
  "min": 279.09
}
```

#### GET `/api/v1/temperature?max=<max_results>`
This endpoint will return a list with the lasts tempereatures retrieved by the first API, to a maximun of `max_results`.

##### Parameters

| Parameter     | Type      | required    | default    |
|---------------|-----------|-------------|------------|
| max_results   | integer   | no          | 5*         |

*The default value is setted in the `.env` file

### 2.1 Testing the application
The tests was created with **[pytest](https://docs.pytest.org/)**. You will need to pass the `OPEN_WEATHER_API_KEY` value to pytest before run the tests. The command will be like this:
```bash
(venv) $ OPEN_WEATHER_API_KEY='0123456789abcdef0123456789abcdef' pytest --cov=app
================================== test session starts ==================================
platform linux -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/weiner/projects/weather
plugins: cov-3.0.0, env-0.6.2
collected 5 items

tests/test_app.py                                                                  [ 20%]
tests/test_temperature.py ....                                                     [100%]

----------- coverage: platform linux, python 3.8.2-final-0 -----------
Name                                          Stmts   Miss  Cover
-----------------------------------------------------------------
app/__init__.py                                  10      0   100%
app/config.py                                     6      0   100%
app/controllers/__init__.py                       0      0   100%
app/controllers/temperature/__init__.py           3      0   100%
app/controllers/temperature/apis.py              26      0   100%
app/controllers/temperature/integrations.py      10      0   100%
-----------------------------------------------------------------
TOTAL                                            55      0   100%


================================== 5 passed in 6.66s ==================================
```