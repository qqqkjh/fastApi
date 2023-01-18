import os

def get_cur_path():
    return os.path.abspath(os.curdir)

def get_app_path():
    app_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(app_dir)

def get_env_path(env: str = '.env'):
    app_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(app_dir)
    base_dir = os.path.dirname(root_dir)
    return os.path.join(base_dir, env)
