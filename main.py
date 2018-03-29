#!/usr/bin/env python
import os
import jinja2
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.topic import TopicHandler
from handlers.TopicList import TopicListHandler
from handlers.onetopic import OneTopicHandler



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/topic/add',TopicHandler,name="topic-add"),
    webapp2.Route('/topiclist',TopicListHandler),
    webapp2.Route('/topic/<topic_id:\d+>',OneTopicHandler,name="topic")

], debug=True)
