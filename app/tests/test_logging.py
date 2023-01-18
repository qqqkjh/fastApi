import os
from unittest import TestCase
from app.utils.path import get_app_path,get_cur_path,get_env_path

class Test(TestCase):
    def test_log_http(self):
        print('--cur')
        print(get_cur_path())
        print('--app')
        print(get_app_path())
        print('--env')
        print(get_env_path())
        print('--logging')
        print(os.path.join(get_app_path(), 'logging.conf'))
