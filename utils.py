import json


def load_data_posts():
    """ Загружает данные из файла и возвращает обычный list"""
    with open("C:\\Users\\Den4ik\\PycharmProjects\\coursework2_source\\data\posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_data_comments():
    """ Загружает данные из файла и возвращает обычный list"""
    with open("C:\\Users\\Den4ik\\PycharmProjects\\coursework2_source\\data\\comments.json", "r",
              encoding="utf-8") as file:
        data = json.load(file)
    return data


# Функции, связанные с постами #


def get_posts_all():
    """ Возвращает все посты"""
    all_posts = load_data_posts()
    return all_posts


def get_posts_by_user(username=str):
    """ Возвращает посты по имени юзера"""
    user_posts = []
    for data in load_data_posts():
        if data['poster_name'] == username.lower():
            user_posts.append(data)
    return user_posts




def get_post_by_pk(pk=int):
    """ Возвращает посты по id"""
    for data in load_data_posts():
        if data['pk'] == pk:
            return data


def search_for_posts(query=str):
    """ Возвращает посты по содержимому content"""
    posts_by_query = []
    for data in load_data_posts():
        if query.lower() in data['content'].lower():
            posts_by_query.append(data)
    return posts_by_query


# Функции, связанные с комментами #

def get_comments_by_post_id(post_id=int):
    """ Возвращает комменты по id поста"""
    comments_by_id = []
    for data in load_data_comments():
        if data['post_id'] == post_id:
            comments_by_id.append(data)
    return comments_by_id
