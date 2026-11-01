from helpers import login_user


def test_login_success(registered_user):
    response = login_user(registered_user["username"], registered_user["password"])

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data.get("access"), str) and data["access"]
    assert isinstance(data.get("refresh"), str) and data["refresh"]


def test_login_wrong_password(registered_user):
    response = login_user(registered_user["username"], "WrongPassword")

    assert response.status_code == 401, response.text


def test_login_wrong_username(registered_user):
    response = login_user("wrong_user_xyz_zk", registered_user["password"])

    assert response.status_code == 401, response.text


def test_login_empty_password(registered_user):
    response = login_user(registered_user["username"], "")

    assert response.status_code == 400, response.text
    assert "password" in response.json()


def test_login_empty_username(registered_user):
    response = login_user("", registered_user["password"])

    assert response.status_code == 400, response.text
    assert "username" in response.json()


def test_login_both_fields_empty():
    response = login_user("", "")

    assert response.status_code == 400, response.text
    errors = response.json()
    assert "username" in errors
    assert "password" in errors
