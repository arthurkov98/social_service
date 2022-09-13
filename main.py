# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import uvicorn
from graph import Graph
from starlette.routing import Route
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse

async def set_graph(request: Request):
    data = request.json()
    app.graph.parse_data2graph(data["graph"])
    return JSONResponse(app.graph.get_info())

async def graph_info(request: Request):
    return JSONResponse(app.graph.get_info())


async def add_conn(request: Request):
    data = request.json()
    n_from = data['from']
    n_to = data['to']
    return JSONResponse({"message": app.graph.add_connection((n_from, n_to))})


routes = [
    Route('/create', set_graph),
    Route('/info', graph_info),
    Route('/add', add_conn),
]

app = Starlette(debug=True, routes=routes)
app.graph = Graph()
uvicorn.run(app, host="0.0.0.0")