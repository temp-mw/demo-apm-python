FROM python:3.10-slim

WORKDIR /app

COPY ./ /app
RUN pip install -r requirements.txt
RUN middleware-bootstrap -a install 

ENV MW_SERVICE_NAME="python-basic-app"
ENV MW_AGENT_SERVICE="172.17.0.1"

CMD ["middleware-run","python3", "main.py"]