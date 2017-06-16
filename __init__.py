from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

# migration
migrate = Migrate(app, db)

# Markdown
Markdown(app)

# images
upload_images = UploadSet('images', IMAGES)
configure_uploads(app, upload_images)

from blog import views
from author import views
