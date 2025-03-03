from flask import Flask, request
import logging
import sys
from test import sample_function, another_function

logging.getLogger().setLevel(logging.INFO)
logging.info("Application initiated successfully.", extra={'Tester': 'Alex'})

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.error("error log sample", extra={'CalledFunc': 'hello_world'})
    logging.warning("warning log sample")
    logging.info("info log sample")
    return 'Hello World!'

@app.route('/exception-new')
def generate_exception():
    error_type = request.args.get('type', default=0, type=int)  # Get error type from query param
    try:
        sample_function(error_type)
    except Exception as e:
        logging.error(f"Caught an exception: {e}")
        another_function(e)
    return f"Error type {error_type} triggered successfully!"

if __name__ == '__main__':
    app.run('0.0.0.0', 8010)
