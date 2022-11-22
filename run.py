from flask import Flask
from views import main_blueprint, posts_by_name_blueprint, posts_by_id_blueprint, user_posts_blueprint, \
    api_posts_blueprint, api_posts_by_id_blueprint


app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(posts_by_name_blueprint)
app.register_blueprint(posts_by_id_blueprint)
app.register_blueprint(user_posts_blueprint)
app.register_blueprint(api_posts_blueprint)
app.register_blueprint(api_posts_by_id_blueprint)

if __name__ == '__main__':
    app.run()
