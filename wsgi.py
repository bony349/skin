from app import app
from flask import Flask
config_file='settings.py'
app.config.from_pyfile(config_file)
