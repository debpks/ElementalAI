import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ['PYTHONPATH']=parent_dir

print(os.environ['PYTHONPATH'])