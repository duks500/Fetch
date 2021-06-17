# ITAY GOLDFADEN CODING EXERCISE

Here you can find my HTTP web service exercise.

Please follow the docs with all of the requests
#

## How to run the code

1. Install pip - 
* Windows:

```bash
py -m pip install
```
* Linux:
```bash
python3 -m pip install
```
#

2. Install virtual environment
* Windows:

```bash
py -m pip install --user virtualenv
```
* Linux:
```bash
python3 -m pip install --user virtualenv
```
#
3. create a virtual environment
* Windows:

```bash
python3 -m venv env
```
* Linux:
```bash
py -m venv env
```
#
4. Activate the virtual environment
* Windows:

```bash
source env/bin/activate
```
* Linux:
```bash
.\env\Scripts\activate
```
#
5. Clone the project

```bash
git clone https://github.com/duks500/Fetch.git
```
#
6. Installing the reuqiremtns.txt
```bash
pip install -r reuqiremtns.txt
```
#
7. Running Django
```bash
python manage.py runserver
```
#

## Testing
```bash
python manage.py test
```


## URLs

1. http://127.0.0.1:8000/app/add-transaction/
2. http://127.0.0.1:8000/app/spend-points/
3. http://127.0.0.1:8000/app/point-final-balance/
