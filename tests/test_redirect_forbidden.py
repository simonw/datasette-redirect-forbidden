from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_redirect():
    path = "/"
    datasette = Datasette(
        [],
        memory=True,
        metadata={
            "allow": {
                "id": "root",
            },
            "plugins": {"datasette-redirect-forbidden": {"redirect_to": "/-/login"}},
        },
    )
    response = await datasette.client.get(path)
    assert response.status_code == 302
    assert response.headers["location"] == "/-/login"
    # But root works OK
    root_response = await datasette.client.get(
        path, cookies={"ds_actor": datasette.sign({"a": {"id": "root"}}, "actor")}
    )
    assert root_response.status_code == 200
