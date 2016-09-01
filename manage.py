from flask import Flask
from flask.ext.script import Manager, Server
from price import price as web

app = web.create_app()
manager = Manager(app)

manager.add_command('server', Server(host='0.0.0.0', use_reloader=True))

if __name__ == '__main__':
    manager.run()
