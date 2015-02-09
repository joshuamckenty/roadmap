import os

DEBUG = True
SECRET_KEY = 'REPLACE_THIS_SECRET_KEY'

db_path = os.path.abspath(os.path.join(os.path.basename(__file__), "../"))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///%s/roadmap.db' % (db_path))
ORCHESTRATE_KEY = os.environ.get('ORCHESTRATE_KEY', "foo")
