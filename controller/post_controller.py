from flask import Blueprint
from services.post_service import PostService

post_blueprint = Blueprint('post_blueprint', __name__)
@post_blueprint.route('/sync_posts', methods=['GET'])
def sync_data():
   return PostService.sync_posts()