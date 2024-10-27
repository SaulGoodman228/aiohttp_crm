from typing import Optional

from aiohttp.web import (Application as AiohttpAplication,
                         run_app as aiohttp_run_app,
                         View as AiohttpView,
                         Request as AiohttpRequest)
from aiohttp.web_request import Request
from aiohttp_apispec import setup_aiohttp_apispec

from apps.store import setup_accessor
from apps.store.crm.accessor import CrmAccessor
from apps.web.middlewares import setup_middlewares
from apps.web.routes import setup_routes



class Application(AiohttpAplication):
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None

class Request(AiohttpRequest):
    @property
    def app(self) -> "Application":
        return super().app()

class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()

def run_app():
    setup_routes(app)
    setup_aiohttp_apispec(app, tytle='CRM Application', url='/docks/json',swagger_path='/docks')
    setup_middlewares(app)
    setup_accessor(app)
    aiohttp_run_app(app, host='127.0.0.1', port=8080)