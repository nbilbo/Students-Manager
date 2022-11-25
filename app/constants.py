import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
ICONS_DIR = os.path.join(ASSETS_DIR, 'icons')
DATABASE_PATH = os.path.join(BASE_DIR, 'db.sqlite3')
