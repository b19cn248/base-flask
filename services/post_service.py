from models import db
from models.post import Post
from elasticsearch import Elasticsearch

es = Elasticsearch('192.168.14.217:9200')

class PostService:
    @staticmethod
    def sync_posts():
        index_name = 'facebook2'
        page_size = 100  # Số lượng documents trên mỗi trang
        total_documents = None

        es_query = {
            "query": {
                "match_all": {}
            }
        }

        synced_posts = []

        while total_documents is None or len(synced_posts) < total_documents:
            response = es.search(index=index_name, body=es_query, size=page_size, from_=len(synced_posts))

            if total_documents is None:
                total_documents = response['hits']['total']['value']

            for hit in response['hits']['hits']:
                document = hit['_source']
                post_title = document.get('title')
                post_content = document.get('content')

                new_post = Post(title=post_title, content=post_content)
                db.session.add(new_post)
                db.session.commit()

                synced_posts.append({"title": post_title, "content": post_content})

        return synced_posts

