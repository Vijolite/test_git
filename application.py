import flask


# Create the application.
application = flask.Flask(__name__)


@application.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    application.debug=True
    application.run()


    
