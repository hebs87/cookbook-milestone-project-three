from flask import Blueprint, render_template

# Blueprint instance to errors route
errors = Blueprint("errors", __name__)


'''
ERROR HANDLERS
'''


# 404 error handler
@errors.errorhandler(404)
def not_found_error(error):
    return render_template("errors/error_404.html"), 404


# 505 error handler
@errors.errorhandler(500)
def something_wrong_error(error):
    return render_template("errors/error_500.html"), 500


# Catch all error handler
@errors.route("/<path:path>")
def global_error(path):
    return render_template("errors/error_404.html"), 404
