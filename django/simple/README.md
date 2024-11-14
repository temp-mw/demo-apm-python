# Python Django Application Instrumentation Guide
Follow our [documentation](https://docs.middleware.io/docs/apm-configuration/python/python-apm-setup) to setup APM for your Python Django application.

[![PyPI - Version](https://img.shields.io/pypi/v/middleware-apm)](https://pypi.org/project/middleware-apm/)


|  Traces  |  Metrics  |  Profiling  |  Logs (App/Custom)  |
|:--------:|:---------:|:-----------:|:-------------------:|
|   Yes    |    Yes    |     Yes     |       Yes/Yes       |

## Prerequisites
Ensure that you have the Middleware Host Agent installed to view Python demo data on your dashboard.

---------------------

## Installing Pre-Requirements

You need install the pre-requirements for run this Hello World example.

Update repositories of available packages to install, with
the following command:

```shell
sudo apt update
```

Install necessary minimum dependencies, with the following command:

```shell
sudo apt install python3-dev python3-pip python3-virtualenv sqlitebrowser
```

For run this example need to install Django
framework execute the follow command:

```python
virtualenv django_instrumentation
source django_instrumentation/bin/activate
pip install -r requirements.txt
```

And later followed by:

```python
python3 manage.py migrate
```


For use the Django Admin Interface, it's needed to create a superuser 
for management, with the following command:

```python
python3 manage.py createsuperuser --username admin --email admin@mail.com
```
## Run Your Application

Now, you can go ahead to run your application, by using:
```python
DJANGO_SETTINGS_MODULE='helloworld.settings' middleware-run python3 manage.py runserver
```

If you are running this application in a serverless setup consider adding `MW_API_KEY` and `MW_TARGET` as mentioned in the command below :
```python
MW_API_KEY=********** MW_TARGET=https://*****.middleware.io:443 DJANGO_SETTINGS_MODULE='helloworld.settings' middleware-run python3 manage.py runserver
```

Then, you can open the URL http://127.0.0.1:8000/ in your web browser.

Also you can open in your web browser the URL http://127.0.0.1:8000/admin for access to 
the *Django Admin Interface*.
