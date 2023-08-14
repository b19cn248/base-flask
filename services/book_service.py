from models.book import Book;
from flask import (jsonify, request)
from models import db

class BookService:

    @staticmethod
    def get_all_books():
        books = Book.query.all()
        return jsonify([book.as_dict() for book in books])

    @staticmethod
    def get_book(book_id):
        try:
            book = Book.query.get(book_id)
            if book:
                return jsonify(book.as_dict())
            else:
                return jsonify({"message": "Book not found with given id"}), 404
        except Exception as e:
            return jsonify({"message": "An error occurred"}), 500

    @staticmethod
    def create_book():
        data = request.json
        book = Book(title=data['title'], author=data['author'])
        db.session.add(book)
        db.session.commit()

        # Chuyển đổi đối tượng book thành từ điển trước khi trả về
        book_dict = book.as_dict()
        return jsonify(book_dict), 201

    @staticmethod
    def update_book(book_id):
        book = Book.query.get(book_id)
        if book:
            data = request.json
            book.title = data['title']
            book.author = data['author']
            db.session.commit()

            # Chuyển đổi đối tượng book thành từ điển trước khi trả về
            book_dict = book.as_dict()

            return jsonify(book_dict)
        return ('', 404)

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return ('', 204)
        return ('', 404)
