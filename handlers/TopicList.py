from handlers.base import BaseHandler
from google.appengine.api import users
from models.topic import Topic

class TopicListHandler(BaseHandler):
    def get(self):
        list = Topic.query().fetch()
        params = {"list": list}
        return self.render_template("topiclist.html",params=params)
