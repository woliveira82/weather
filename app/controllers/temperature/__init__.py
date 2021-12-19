from flask import Blueprint

temperature = Blueprint('temperature', __name__)

from .apis import *
