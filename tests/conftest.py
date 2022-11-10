import runpy

import pytest


@pytest.fixture()
def test_client():
    app = runpy.app
    return app.test_client()
