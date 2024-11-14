# Python Django Application with Gunicorn Instrumentation Guide

Follow our [documentation](https://docs.middleware.io/docs/apm-configuration/python/python-apm-setup) to setup APM for Django python application with gunicorn.

[![PyPI - Version](https://img.shields.io/pypi/v/middleware-apm)](https://pypi.org/project/middleware-apm/)


|  Traces  |  Metrics  |  Profiling  |  Logs (App/Custom)  |
|:--------:|:---------:|:-----------:|:-------------------:|
|   Yes    |    Yes    |     Yes     |       Yes/Yes       |

## Prerequisites
Ensure that you have the Middleware Host Agent installed to view Python demo data on your dashboard.

---------------------
# Steps to Run the Project

Create and Activate Virtual Environment
```
python3 -m venv env
source env/bin/activate
```

Go to Project Root
```
cd demo
```

Install Dependencies
```
pip install -r requirements.txt
```

Install OpenTelemetry instrument libraries 
```shell
middleware-bootstrap -a install
```

Run the Application
```
DJANGO_SETTINGS_MODULE='demo.settings' middleware-run gunicorn -c conf/gunicorn.conf.py --workers=4  --bind 0.0.0.0:8000 --timeout 120 demo.wsgi
```

If you are running this application in a serverless setup consider adding `MW_API_KEY` and `MW_TARGET` as mentioned in the command below :
```python
MW_API_KEY=********** MW_TARGET=https://*****.middleware.io:443 DJANGO_SETTINGS_MODULE='demo.settings' middleware-run gunicorn -c conf/gunicorn.conf.py --workers=4  --bind 0.0.0.0:8000 --timeout 120 demo.wsgi
```


`Note:  --workers and --timeout are optional`