from src.views import *


app = web.Application()
app.router.add_static('/static', path='src/static')

app.add_routes([
    web.get("/", root),
    web.get("/client/{uri:.+}", client),
    ]
)
web.run_app(app)