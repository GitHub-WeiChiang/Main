import time
import uvicorn as uvicorn

from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


app = FastAPI()

# # Enforces that all incoming requests must either be https or wss.
# # Any incoming requests to http or ws will be redirected to the secure scheme instead.
# app.add_middleware(HTTPSRedirectMiddleware)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/", tags=["Main"])
async def root():
    return RedirectResponse("http://127.0.0.1:8000/docs#/")


if __name__ == '__main__':
    uvicorn.run("Main:app", host="127.0.0.1", port=8000, reload=True)
