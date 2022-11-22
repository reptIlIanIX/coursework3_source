from run import app
from utils import get_posts_all, get_post_by_pk

keys_posts = {'content',
              'likes_count',
              'pic',
              'pk',
              'poster_avatar',
              'poster_name',
              'views_count'}


def test_app():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_app_2():
    response = app.test_client().get('/meow')
    assert response.status_code == 404


def test_app_post():
    response = app.test_client().get('/post/3')
    mistake_response = app.test_client().get('/post/9')
    assert response.status_code == 200
    assert mistake_response.status_code == 500


def test_search():
    params = {"s": str}
    response = app.test_client().get('/search', query_string=params)
    print(response.json)
    assert response.status_code == 200


def test_search_2():
    params = {"s": int}
    response = app.test_client().get('/search', query_string=params)
    print(response.json)
    assert response.status_code == 200


def test_json_all():
    data = get_posts_all()
    response = app.test_client().get('/api/posts/', json=data)
    assert response.json == data
    for item in data:
        assert set(item.keys()) == keys_posts


def test_json_one():
    data = get_post_by_pk(2)
    response = app.test_client().get('/api/posts/2', json=data)
    assert response.json == data
    assert set(data.keys()) == keys_posts
