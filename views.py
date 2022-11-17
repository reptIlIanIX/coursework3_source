import logging
from flask import Blueprint, render_template, request, jsonify

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
posts_by_name_blueprint = Blueprint("posts_by_name_blueprint", __name__, template_folder='templates')
posts_by_id_blueprint = Blueprint("posts_by_id_blueprint", __name__, template_folder='templates')
user_posts_blueprint = Blueprint("user_posts_blueprint", __name__, template_folder='templates')
api_posts_blueprint = Blueprint("api_posts_blueprint", __name__, template_folder='templates')
api_posts_by_id_blueprint = Blueprint("api_posts_by_id_blueprint", __name__, template_folder='templates')

logging.basicConfig(level=logging.INFO, filename='logs/api.log')

@main_blueprint.route('/')
def page_index():
    posts = get_posts_all()
    logging.info("Главная страница запрошена")
    return render_template('index.html', posts=posts)


@posts_by_name_blueprint.route('/search')
def page_sort():
    s = request.args['s']
    posts = search_for_posts(s)
    len_posts = len(posts)
    logging.info("Страница поиска запрошена")
    return render_template('search.html', posts=posts, s=s, len_posts=len_posts)


@posts_by_id_blueprint.route("/post/<int:pk>")
def post_id(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    comments_len = len(comments)
    text_len = len(post['content'])
    logging.info("Страница с подробным постом и комментариями запрошена")
    return render_template('post.html', post=post, comments=comments, comments_len=comments_len, text_len=text_len)


@user_posts_blueprint.route("/users/<username>")
def user_posts(username):
    logging.info("Страница с постами юзера запрошена")
    username = get_posts_by_user(username)
    return render_template('user-feed.html', username=username)


@api_posts_blueprint.route("/api/posts/")
def api_posts():
    posts = get_posts_all()
    logging.info("Страница с json постами запрошена")
    return jsonify(posts)


@api_posts_by_id_blueprint.route("/api/posts/<int:pk>")
def api_posts_by_id(pk):
    post = get_post_by_pk(pk)
    logging.info("Страница с json постом по pk запрошена")
    return jsonify(post)
