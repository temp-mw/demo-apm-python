import logging
from django.http import HttpResponse
from opentelemetry import trace

tracer = trace.get_tracer("hello_world_tracer")

def index(request):
    with tracer.start_as_current_span(name="hello") as span:
        span.set_attribute("message", "This is sample span hello world!")
    return HttpResponse("Hello, world!")

def ok(request):
    return HttpResponse("Hello, ok", status=404)

def run(request):
    logging.warning("run: warning log sample")
    return HttpResponse("Hello, run!")
