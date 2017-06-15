# Flask Blog
A blog application written with Python, MySQL and Flask

## Getting Started

### Virtual Environment
In order to run this app you must create a virtual environment for Python.

More on virtualenv [here](https://virtualenv.pypa.io/en/stable/)

To install just use pip:

```bash
pip install virtualenv
```
Note: use pip for Python 2.7, use pip3 for Python 3.x

#### Initialize
```bash
virtualenv -p python3 venv
```

#### Activate venv
```bash
source venv/bin/activate
```

#### Exit venv
```bash
deactivate
```

## Install dependencies
Run the pip install inside your venv
```bash
pip install -r requirements.txt 
```

## Running migrations
Ensure you are in your venv. 

### migrate
```bash
python manage.py db migrate
```

### execute
```bash
python manage.py db upgrade
```

## Run Server
From your project root run the following in the terminal.
```bash
python manage.py runserver
```