import flask
from flask import request

from opentelemetry import trace
import logging
logging.getLogger().setLevel(logging.INFO)

app = flask.Flask(__name__)

tracer = trace.get_tracer(__name__)


def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_fast(n - 2)


def fib_fast(n):
    nth_fib = [0] * (n + 2)
    nth_fib[1] = 1
    for i in range(2, n + 1):
        nth_fib[i] = nth_fib[i - 1] + nth_fib[i - 2]
    return nth_fib[n]


@app.route("/fibonacci")
def fibonacci():
    n = int(request.args.get("n", 1))
    with tracer.start_as_current_span("root"): # added custom span root
        with tracer.start_as_current_span("fib_slow") as slow_span: # added custom span slow_span
            ans = fib_slow(n)
            logging.info(f"calculated fib_slow for n={n} and got {ans}")
            slow_span.set_attribute("n", n)
            slow_span.set_attribute("nth_fibonacci", ans)
        with tracer.start_as_current_span("fib_fast") as fast_span: # added custom span fast_span
            ans = fib_fast(n)
            logging.info(f"calculated fib_fast for n={n} and got {ans}")
            fast_span.set_attribute("n", n)
            fast_span.set_attribute("nth_fibonacci", ans)

    return f"F({n}) is: ({ans})"


if __name__ == "__main__":
    app.run()