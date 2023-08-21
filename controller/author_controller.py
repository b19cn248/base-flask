from flask import Blueprint
from services.author_service import AuthorService

auth_blueprint = Blueprint('auth_blueprint', __name__)
@auth_blueprint.route('/sync_authors', methods=['GET'])
def sync_data():
   return AuthorService.get_synced_authors()
