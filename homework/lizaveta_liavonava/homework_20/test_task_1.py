import requests
import pytest


@pytest.fixture()
def new_line():
    body = {"data": {"color": "black", "size": "small"}, "name": "super new object"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    line_id = response.json()['id']
    print(line_id)
    yield line_id
    print('deleting the line')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{line_id}')


@pytest.fixture(scope='session', autouse=True)
def system_message():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def system_message_each_test():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
@pytest.mark.parametrize('body', [
    {"data": {"color": "black", "size": "small"}, "name": "super new object"},
    {"data": {"color": "white", "size": "huge"}, "name": "super new object 2"},
    {"data": {"color": "yellow", "size": "tiny"}, "name": "super new object 3"}
])
def test_post_new_line(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == body['name'], 'Name is incorrect'
    requests.delete(f'http://objapi.course.qa-practice.com/object/{response.json()["id"]}')


def test_put_a_line(new_line):
    body = {
        "data":
            {"color": "yellow",
             "size": "small"},
        "name": "super new object updated/put"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_line}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "super new object updated/put", 'Name is incorrect'


def test_patch_a_line(new_line):
    body = {
        "name": "super new object updated/PATCH"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_line}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "super new object updated/PATCH", 'Name is incorrect'
    assert response.json()['data'] == {"color": "black", "size": "small"}, 'Data has changed'


@pytest.mark.medium
def test_get_one_line(new_line):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{new_line}',
    )
    assert response.status_code == 200, 'The line is not found'
    assert response.json()['id'] == new_line, 'The line with the id is not found'
    assert response.json()['name'] == 'super new object', 'The line with the name is not found'
    assert response.json()['data'] == {"color": "black", "size": "small"}, 'The line ith the data is not found'


def test_delete_one_line(new_line):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_line}')
    assert response.status_code == 200, 'Status code is incorrect'
    check = requests.get(f'http://objapi.course.qa-practice.com/object/{new_line}')
    assert check.status_code == 404, 'Object was not deleted'
