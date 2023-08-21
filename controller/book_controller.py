from flask import Blueprint
from services.book_service import BookService
book_blueprint = Blueprint('book_blueprint', __name__)


@book_blueprint.route('/books', methods=['GET'])
def get_books():
    return BookService.get_all_books()


@book_blueprint.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return BookService.get_book(book_id)


@book_blueprint.route('/books', methods=['POST'])
def create_book():
    return BookService.create_book()

@book_blueprint.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    return BookService.update_book(book_id)


@book_blueprint.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return BookService.delete_book(book_id)
