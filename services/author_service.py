from models.author import Author
from models import db
from elasticsearch import Elasticsearch

es = Elasticsearch('192.168.14.217:9200')

class AuthorService:

    @staticmethod
    def get_synced_authors():
        index_name = 'facebook2'
        es_query = {
            "query": {
                "match_all": {}
            }
        }
        response = es.search(index=index_name, body=es_query, size=1000)

        synced_authors = []

        for hit in response['hits']['hits']:
            document = hit['_source']
            author_name = document.get('author')
            author_link = document.get('author_link')

            # Check if the author already exists in the database
            existing_author = Author.query.filter_by(name=author_name).first()

            if existing_author is None:
                new_author = Author(name=author_name, link=author_link)  # Only take the first 100 characters
                db.session.add(new_author)
                db.session.commit()
                synced_authors.append({"name": author_name, "link": author_link[:100]})
            else:
                synced_authors.append({"name": author_name, "link": existing_author.link})

        return synced_authors

