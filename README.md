# Getting Started With Middleware Python APM 
Follow our [documentation](https://docs.middleware.io/docs/apm-configuration/python/python-apm-setup) to setup APM for your Python application and detailed explanation for telemetry data for APMs.

[![PyPI - Version](https://img.shields.io/pypi/v/middleware-apm)](https://pypi.org/project/middleware-apm/)


|  Traces  |  Metrics  |  Profiling  |  Logs (App/Custom)  |
|:--------:|:---------:|:-----------:|:-------------------:|
|   Yes    |    Yes    |     Yes     |       Yes/Yes       |

## Prerequisites
Ensure that you have the Middleware Host [Agent](https://docs.middleware.io/agent-installation/overview#installing-the-middleware-agent) installed for Instrumentation of your Python Application.

---------------------

## Getting Started Guide 
### Setup Virtual Environment (Optional)
Run the following commands in your terminal:

```bash
$ python -m venv myenv
$ source myenv/bin/activate
```
### Install Middleware's Python APM package
Run the following commands in your terminal:
```bash
$ pip install middleware-apm
```
### Install instrumentation library for the framework:
Run the following commands in your terminal  
to install instrumentation library:
```bash
$ middleware-bootstrap -a install
```

The `middleware-bootstrap -a install` command reads through the list of packages installed in your active `site-packages` folder, and installs the corresponding instrumentation libraries for these packages, if applicable. For example, if you already installed the `flask` package, running `middleware-bootstrap -a install` will install `opentelemetry-instrumentation-flask` for you. The Middleware Python agent will use monkey patching to modify functions in these libraries at runtime.  

Ensure library is installed properly with command:  
```bash
$ pip list | grep -i flask

  Flask                                        3.0.3
  opentelemetry-instrumentation-flask          0.48b0
```

## Instrument Python Application

## 1. Zero Code Instrumentation Using Environment Variables

Zero code instrumentation allows you to monitor your Python application without modifying the code. This can be achieved by setting environment variables that configure the application with Middleware Application Performance Monitoring (APM) tool.

**Example:**

you can set the following environment variables in your shell:

```bash
export MW_API_KEY='whkvkobudfitutobptgonaezuxpjjypnejbb'
export MW_TARGET='https://myapp.middleware.io:443'
export MW_SERVICE_NAME='MyFlaskServer'
middleware-run python app.py
```
Add or replace envs as required for the application.

## 2. Using `mw_tracker` Function from Middleware
If you prefer more control and want to integrate APM directly into your application, you can use a middleware function like `mw_tracker`. This method requires adding a specific function call in your application's code .

**Example:**
```python
from flask import Flask

# Add the mw_tracker middleware to your app
from middleware import mw_tracker, MWOptions, record_exception, DETECT_AWS_EC2
 mw_tracker(
     MWOptions(
         access_token="whkvkobudfitutobptgonaezuxpjjypnejbb",
         target="https://myapp.middleware.io:443",
         console_exporter=True,
         debug_log_file=True,
         service_name="MyPythonServer",
         otel_propagators = "b3,tracecontext",
         custom_resource_attributes="call_id=12345678, request_id=987654321",
         detectors=[DETECT_AWS_EC2]
     )
 )

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```
### Run Your Application 

To run your application, use the following command:
```bash
MW_TRACKER=True middleware-run python app.py
```

###  APM Configuration Attributes and Environment Variables

| Attribute                        | Type               | Environment Variable                                   | Example Usage                                                   |
|----------------------------------|--------------------|-------------------------------------------------------|----------------------------------------------------------------|
| `access_token`                   | `str`              | `MW_API_KEY`                                          | `access_token = "whkvkobudfitutobptgonaezuxpjjypnejbb"`       |
| `service_name`                   | `str`              | `MW_SERVICE_NAME` (alternative: `OTEL_SERVICE_NAME`) | `service_name = "MyPythonServer"`                              |
| `collect_traces`                 | `bool`             | `MW_APM_COLLECT_TRACES` (default: True)              | `collect_traces = True`                                       |
| `collect_metrics`                | `bool`             | `MW_APM_COLLECT_METRICS` (default: True)             | `collect_metrics = False`                                      |
| `collect_logs`                   | `bool`             | `MW_APM_COLLECT_LOGS` (default: True)                | `collect_logs = True`                                         |
| `log_level`                      | `str`              | `MW_LOG_LEVEL` (alternative: `OTEL_LOG_LEVEL`)       | `log_level = "DEBUG"`                                         |
| `mw_agent_service`               | `str`              | `MW_AGENT_SERVICE` (default: "localhost")            | `(Docker) mw_agent_service = 172.17.0.1`<br>`(Kubernetes) mw_agent_service = mw-service.mw-agent-ns.svc.cluster.local` |
| `target`                         | `str`              | `MW_TARGET` (alternative: `OTEL_EXPORTER_OTLP_ENDPOINT`, default: "http://localhost:9319") | `target = "https://myapp.middleware.io:443"`                 |
| `custom_resource_attributes`      | `str`              | `MW_CUSTOM_RESOURCE_ATTRIBUTES`                       | `custom_resource_attributes = "call_id=12345678, request_id=987654321"` |
| `otel_propagators`               | `str`              | `MW_PROPAGATORS` (alternative: `OTEL_PROPAGATORS`, default: "b3")  | `otel_propagators = "b3,tracecontext"`                        |
| `console_exporter`               | `bool`             | `MW_CONSOLE_EXPORTER` (default: False)               | `console_exporter = True`                                     |
| `debug_log_file`                 | `bool`             | `MW_DEBUG_LOG_FILE` (default: False)                 | `debug_log_file = True`                                       |
| `project_name`                   | `str`              | `MW_PROJECT_NAME`                                    | `project_name = "TestingProject"`                              |
| `sample_rate`                    | `int`              | `MW_SAMPLE_RATE`                                     |  `sample_rate = 0.5` <br>`AlwaysOn (1), AlwaysOff (0), or a TraceIdRatio as 1/N.` |
| `detectors`                      | `(str, List[Detector])`  |  `MW_DETECTORS`                                     |  `detectors = [DETECT_AWS_LAMBDA, DETECT_GCP]` <br> `MW_DETECTORS= "aws_lambda,gcp"`  |

---------------------------------

## Custom Exception 
To send exception to traces: 
```python
from middleware import record_exception
    try:
        print("Divide by zero:",1/0)
    except Exception as e:
        record_exception(e)
```
Note: This is required only for cases where custom exception handling is required.

## Debug Trace, Metrics, Logs using Console Exporter
To console log telemetry data use `console_exporter` with `mw_tracker()` or `export MW_CONSOLE_EXPORTER=True`.  
To send this telemetry data in files use `debug_log_file` with `mw_tracker()` or `export MW_DEBUG_LOG_FILE=True`

## Add Resource Detectors
To add resource detectors use `detectors` with `mw_tracker()` or `export MW_DETECTORS="aws_ec2,envvars"`
```python
from middleware import mw_tracker, MWOptions, DETECT_AWS_EC2
 mw_tracker(
     MWOptions(
         service_name="MyPythonServer",
         detectors=[DETECT_AWS_EC2]
     )
 )
```

## Use Token and Target (For Agent-less/Serverless Setup)
To add token use `access_token` with `mw_tracker()` or `export MW_API_KEY="whkvkobudfitutobptgonaezuxpjjypnejbb"`
To add target use `target` with `mw_tracker()` or `export MW_TARGET="https://myapp.middleware.io:443"`
```python
from middleware import mw_tracker, MWOptions
 mw_tracker(
     MWOptions(
         service_name="MyPythonServer",
         access_token="whkvkobudfitutobptQgonaezuxpjjypnejbb",
         target="https://myapp.middleware.io:443",
     )
 )
```

## Use Agent Service for Containerized Application 
To add agent service use `mw_agent_service` with `mw_tracker()` or `export MW_AGENT_SERVICE="172.17.0.1"`.  
* For Docker:  
  + `mw_agent_service="172.17.0.1"` or `export MW_AGENT_SERVICE="172.17.0.1"`.  
* For Kubernetes:  
  + `mw_agent_service="mw-service.mw-agent-ns.svc.cluster.local"` or   
    `export MW_AGENT_SERVICE="mw-service.mw-agent-ns.svc.cluster.local"`.  

Note: Middleware Host [Agent](https://docs.middleware.io/agent-installation/overview#installing-the-middleware-agent) is required.

## Change log level
To change loge level use `mw_log_level` with `mw_tracker()` or `export MW_LOG_LEVEL=DEBUG`.  
Also alternative OTel env can also be set as `OTEL_LOG_LEVEL=DEBUG`.

## Context Propagators
To add [propagators](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#:~:text=Known%20values%20for%20OTEL_PROPAGATORS%20are%3A) for context propagation use `otel_propagators`  
Example usage:  
 * otel_propagators = "b3,tracecontext"

## Continous Profiling
To enable continous profiling for your python application.  
Install required profiling dependencies with below command:
```
pip install middleware-apm[profiling]
```
Enable profiling with `collect_profiling` or `export MW_APM_COLLECT_PROFILING=True`

## Troubleshooting 
If you face any protoc specific errors, Try setting ...
```
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```
---------------------------------
Follow our [documentation](https://docs.middleware.io/docs/apm-configuration/python/python-apm-setup) for more troubleshooting steps for Python APM.
