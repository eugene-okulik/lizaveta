import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.patch_object import PatchObject
from endpoints.update_object import UpdateObject


@pytest.fixture()
def create_object_endpoint(delete_object_endpoint):
    endpoint = CreateObject()
    yield endpoint
    delete_object_endpoint.delete_object(endpoint.object_id)


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint):
    payload = {"data": {"color": "black", "size": "small"}, "name": "super new object"}
    create_object_endpoint.create_new_object(payload)
    yield create_object_endpoint.object_id


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()
