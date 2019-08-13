from flask import Blueprint, render_template

# Blueprint instance to errors route
errors = Blueprint("errors", __name__)


'''
ERROR HANDLERS
'''


# 404 error handler
@errors.app_errorhandler(404)
def not_found_error(error):
    return render_template("error_404.html"), 404


# 505 error handler
@errors.app_errorhandler(500)
def something_wrong_error(error):
    return render_template("error_500.html"), 500
