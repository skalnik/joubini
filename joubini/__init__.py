import os
import flask
import logging

import octoprint.plugin

static_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
print(static_folder)
blueprint = flask.Blueprint("plugin.joubini", __name__, static_folder=static_folder)

@blueprint.route('/', methods=["GET"])
def home():
    return flask.redirect(flask.url_for('.static', filename='index.html'))


class JoubiniPlugin(octoprint.plugin.BlueprintPlugin):
    def get_blueprint(self):
        global blueprint
        return blueprint

    def is_blueprint_protected(self):
        return False

__plugin_name__ = "Joubini"
__plugin_version__ = "0.0.1"
__plugin_description__ = "OctoPrint UI for Tiny Screens"
__plugin_implementations__ = [JoubiniPlugin()]
