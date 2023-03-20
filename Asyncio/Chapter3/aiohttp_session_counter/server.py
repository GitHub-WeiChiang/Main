import base64

from aiohttp import web
from aiohttp_session import setup, get_session, SimpleCookieStorage
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet

routes = web.RouteTableDef()


@routes.get('/')
async def index(request: web.Request):
    session = await get_session(request)
    session['count'] = (session['count'] if 'count' in session else 0) + 1
    return web.Response(text=f"Count is {session['count']}")


app = web.Application()
app.add_routes(routes)

# secret_key must be 32 url-safe base64-encoded bytes
fernet_key = fernet.Fernet.generate_key()
secret_key = base64.urlsafe_b64decode(fernet_key)
setup(app, EncryptedCookieStorage(secret_key))

# # non-secret
# setup(app, SimpleCookieStorage())

web.run_app(app)
