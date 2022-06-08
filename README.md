# product-review-analysis

## 1 Installation

### 1.1 Install python 3.6 or higher


### 1.2 Install pip3 & virtualenv

```bash
https://pip.pypa.io/en/stable/installation/
```

```bash
pip install virtualenv
```

### 1.3 Create and activate virtualenv

```bash
cd <project dir>

virtualenv .venv

source .venv/bin/activate
```

### 1.4 Install project dependencies

```bash
$ pip install -r requirements.txt
```

### 1.5 Initialize project

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

## 2 Run project

```bash
cd <project dir>

source .venv/bin/activate

python manage.py runserver
```

To Stop & deactivate virtualenv

```bash
CTRL+C

deactivate
```




