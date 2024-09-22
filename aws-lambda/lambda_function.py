import json
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def lambda_handler(event, context):
    with tracer.start_as_current_span("lambda_handler"):
        # Your business logic here
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Middleware!')
        }