## Installation

    pip install -r requirements.txt

## Run application

Note: add MW_TRACKER=True and middleware-run for post-fork instrumentation process-model.

    MW_TRACKER=True middleware-run gunicorn -c gunicorn.conf.py  --bind :8000 --workers 3 --threads 8 --timeout 120 app:app

More on this : https://opentelemetry-python.readthedocs.io/en/stable/examples/fork-process-model/README.html

## Run application Container

docker build -t gunicorn-app .

docker run -p 8090:8090 gunicorn-app
