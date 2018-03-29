from handlers.base import BaseHandler
from google.appengine.api import users
from models.topic import Topic

class OneTopicHandler(BaseHandler):
    def get(self, topic_id):
        topic = Topic.get_by_id(int(topic_id))
        params = {"topic" : topic }
        return self.render_template("topic.html",params=params)
