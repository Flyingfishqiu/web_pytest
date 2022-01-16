import os

import pytest

# pytest.main(['test_case_01.py'])
os.system('pytest')
os.system('allure generate ./result/ -o ./report/html --clean')