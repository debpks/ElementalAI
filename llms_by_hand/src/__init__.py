import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print('parent_dir:', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))