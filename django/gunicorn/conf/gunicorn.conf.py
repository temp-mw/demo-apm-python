from middleware import mw_tracker, MWOptions
mw_tracker(
    MWOptions(
        access_token="whkvkobudfitutobptgonaezuxpjjypnejbb",
        target="https://myapp.middleware.io:443",
        service_name="MyPythonApp",
    )
)

import django
django.setup()

import tracemalloc
tracemalloc.start()