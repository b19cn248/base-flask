from models import db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }

    def __repr__(self):
        return f"<Book {self.title}>"
