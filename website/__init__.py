from flask import Flask


def create_app():
    # set up the template folder for project
    # otherwise it will find the default template folder named "Templates"
    app = Flask(__name__, template_folder="views")

    # creating the secret key for application
    app.config['SECRET_KEY'] = 'hello website'

    from .views import views

    # registed the views
    app.register_blueprint(views, url_prefix='/')

    return app