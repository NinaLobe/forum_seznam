from handlers.base import BaseHandler
from google.appengine.api import users
from models.topic import Topic

class TopicHandler(BaseHandler):
    def get(self):
        return self.render_template("topic_add.html")
    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("You have to login before post a topic!")

        title = self.request.get("title")
        content = self.request.get("text")

        new_topic = Topic(title=title, content=content, author_email=user.email())
        new_topic.put()

        return self.write("You have sucessfully created new topic!")
