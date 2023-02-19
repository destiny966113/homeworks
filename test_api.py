import json

import pytest

from api import app


def test_index_route():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == json.dumps({"data": "ok"})


@pytest.mark.get_request
def test_get_image_route():
    response = app.test_client().get("/image")

    assert response.status_code == 200
