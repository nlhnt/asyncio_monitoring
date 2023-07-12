Based on the article found in [here](https://blog.meadsteve.dev/programming/2020/02/23/monitoring-async-python/).

More info [here](https://docs.python.org/3.8/library/asyncio-dev.html#asyncio-dev).

# How to use

from fastapi import FastAPI
from monitor import Monitor

monitor = Monitor(0.25)
app = FastAPI(title="British Food Generator")

@app.on_event("startup")
def start_monitoring():
    monitor.start()