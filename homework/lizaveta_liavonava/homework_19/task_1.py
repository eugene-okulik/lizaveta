import requests


def post_new_line():
    body = {
        "data":
            {"color": "black",
             "size": "small"},
        "name": "super new object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "super new object", 'Name is incorrect'
    clear(response.json()['id'])


def new_line():
    body = {
        "data":
            {"color": "black",
             "size": "small"},
        "name": "super new object"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(line_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{line_id}')


def put_a_line():
    line_id = new_line()
    body = {
        "data":
            {"color": "yellow",
             "size": "small"},
        "name": "super new object updated/put"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{line_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "super new object updated/put", 'Name is incorrect'
    clear(line_id)


def patch_a_line():
    line_id = new_line()
    body = {
        "name": "super new object updated/PATCH"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{line_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "super new object updated/PATCH", 'Name is incorrect'
    assert response.json()['data'] == {"color": "black", "size": "small"}, 'Data has changed'
    clear(line_id)


def delete_a_line():
    line_id = new_line()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{line_id}')
    assert response.status_code == 200, 'Status code is incorrect'
    check = requests.get(f'http://objapi.course.qa-practice.com/object/{line_id}')
    assert check.status_code == 404, 'Object was not deleted'


post_new_line()
put_a_line()
patch_a_line()
delete_a_line()
