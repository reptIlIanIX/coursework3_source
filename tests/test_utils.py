import pytest

from utils import get_posts_all, load_data_posts, load_data_comments, get_comments_by_post_id

keys_posts = {'content',
              'likes_count',
              'pic',
              'pk',
              'poster_avatar',
              'poster_name',
              'views_count'}

keys_comments = {'commenter_name', 'post_id', 'comment', 'pk'}


def test_load_data_posts():
    load_posts = load_data_posts()
    assert type(load_posts) == list, "возвращается не список"


def test_load_data_comments():
    load_comments = load_data_comments()
    assert type(load_comments) == list, "возвращается не список"


def test_load_data_comments():
    load_posts = load_data_posts()
    assert type(load_posts) == list, "возвращается не список"


def test_get_posts_all():
    all_posts = get_posts_all()
    assert type(all_posts) == list, "возвращается не список"
    assert len(all_posts) > 0, "возвращается пустой список"
    for item in all_posts:
        assert set(item.keys()) == keys_posts, "неверный список ключей"


def test_comments_by_post_id():
    comments_by_id = get_comments_by_post_id(8)
    assert type(comments_by_id) == list, "возвращается не список"
    assert len(comments_by_id) > 0, "возвращается пустой список"
    for item in comments_by_id:
        assert set(item.keys()) == keys_comments, "неверный список ключей"


def test_comments_by_post_id():
    with pytest.raises(TypeError):
        get_comments_by_post_id(1, 3)
