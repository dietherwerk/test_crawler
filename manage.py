# coding: utf-8
from app import app
from flask.ext.script import Manager

manager = Manager(app)

if __name__ == '__main__':
    app.debug = True
    manager.run()
