# Team Name

Source code of Team Name's collaboration website

## Installation

```bash
git clone git@github.com:TeamNameBE/Ctf-Platform.git
python3 -m venv ve
source ve/bin/activate
pip install -r requirements.txt
./manage.py migrate
```

## Running a test server

```bash
export DEBUG=1
./manage.py runserver
```

A celery worker is also required to run the background tasks:

```bash
celery -A tooling.app worker -l info
```
