import os
from app import create_app
from flask_script import Manager,Shell,Server
from app import app_config

config_object=app_config.get(os.environ.get('FLASK_CONIFG','default'))

app=create_app(config_object)

manager=Manager(app)

def make_shell():
    return dict(app=app)

manager.add_command('shell',Shell(make_context=make_shell))
manager.add_command('runserver',Server(
    use_reloader=True,
    host='localhost',
    port=5000
))

if __name__=='__main__':
    manager.run()
