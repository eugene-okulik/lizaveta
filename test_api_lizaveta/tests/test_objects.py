import pytest


TEST_DATA = [
    {"data": {"color": "black", "size": "small"}, "name": "super new object"},
    {"data": {"color": "white", "size": "huge"}, "name": "super new object 2"},
    {"data": {"color": "yellow", "size": "tiny"}, "name": "super new object 3"}
]


@pytest.mark.parametrize('payload', TEST_DATA)
def test_post_a_new_object(create_object_endpoint, payload):
    create_object_endpoint.create_new_object(payload)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(payload['name'])


def test_delete_object(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()
    delete_object_endpoint.check_object_is_deleted(object_id)


def test_put_object(update_object_endpoint, object_id):
    payload = {"data": {"color": "yellow", "size": "small"}, "name": "super new object updated/put"}
    update_object_endpoint.update_object(object_id, payload)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(payload['name'])


def test_patch_object(patch_object_endpoint, object_id):
    payload = {"name": "super new object updated/PATCH"}
    patch_object_endpoint.patch_object(object_id, payload)
    patch_object_endpoint.check_that_status_is_200()
    patch_object_endpoint.check_response_name_is_correct(payload['name'])
    patch_object_endpoint.check_response_data_is_correct({"color": "black", "size": "small"})


def test_get_object(get_object_endpoint, object_id):
    get_object_endpoint.get_object(object_id)
    get_object_endpoint.check_that_status_is_200()
    get_object_endpoint.check_response_id_is_correct(object_id)
    get_object_endpoint.check_response_name_is_correct('super new object')
    get_object_endpoint.check_response_data_is_correct({"color": "black", "size": "small"})
