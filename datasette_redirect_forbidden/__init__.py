from datasette import hookimpl
from datasette.utils.asgi import Response


@hookimpl
def forbidden(datasette):
    config = datasette.plugin_config("datasette-redirect-forbidden") or {}
    redirect_to = config.get("redirect_to")
    if redirect_to:
        return Response.redirect(redirect_to)
