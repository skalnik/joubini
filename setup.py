import setuptools

def package_data_dirs(source, subdirs):
    import os
    dirs = []

    for subdir in subdirs:
        for dirname, _, files in os.walk(os.path.join(source, subdir)):
            dirname = os.path.relpath(dirname, source)
            for f in files:
                dirs.append(os.path.join(dirname, f))

    return dirs

def params():
    name = "Joubini"
    version = "0.0.1"

    description = "OctoPrint UI for Tiny Screens"
    author = "Mike Skalnik"
    author_email = "hi@mikeskalnik.com"
    license = "MIT"

    packages = ["joubini"]
    package_data = {"joubini": package_data_dirs('joubini', ['templates', 'static'])}
    include_package_data = True

    entry_points = {
        "octoprint.plugin": [
                "joubini = joubini"
            ]
    }

    return locals()

setuptools.setup(**params())
