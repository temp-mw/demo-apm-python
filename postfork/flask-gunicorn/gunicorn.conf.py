
bind = "127.0.0.1:8000" 

# Sample Worker processes
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Sample logging
errorlog = "-"
loglevel = "info"
accesslog = "-"
access_log_format = (
    '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
)

from middleware import mw_tracker, MWOptions 

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    # add middleware-instrumentation in post fork (note: export MW_TRACKER=True in post fork model)
    mw_tracker(
        MWOptions(
            access_token="tesasdfaevcqdctespapp",              # can also be added using env
            target="https://tespapp.middleware.io:443",        # can also be added using env
            service_name="TestPythonApp123",                   # can also be added using env
            custom_resource_attributes=f"worker={worker.pid}", # can also be added using env
            # console_exporter=True,                           # add to console log telemetry data
            # debug_log_file=True,                             # add to add console log telemetry data in files 
            # log_level="DEBUG",                               # add to get all instrumentation logs 
        )
    )
    