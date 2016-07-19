import os
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, asynchronous
from tornado.websocket import WebSocketHandler
from tornado import gen
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from pprint import pprint
import json
import logging
from logging.handlers import TimedRotatingFileHandler

class PingHandler(RequestHandler):
    def get(self):
        self.write("Pong Man !!!")

def main():
    # log_file = "/ixp_data_partition/logs/serverlogs/querygen/"

    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(threadName)s - %(message)s')

    # access_log_handler = TimedRotatingFileHandler(log_file + "tornado-access.log",
    #                                  when="d",
    #                                  interval=1,
    #                                  backupCount=3)
    # access_log_handler.setFormatter(formatter)

    # app_log_handler = TimedRotatingFileHandler(log_file + "tornado-app.log",
    #                                  when="d",
    #                                  interval=1,
    #                                  backupCount=3)
    # app_log_handler.setFormatter(formatter)

    # gen_log_handler = TimedRotatingFileHandler(log_file + "tornado-gen.log",
    #                                  when="d",
    #                                  interval=1,
    #                                  backupCount=3)
    # gen_log_handler.setFormatter(formatter)


    # logging.getLogger('tornado.access').addHandler(access_log_handler)
    # logging.getLogger('tornado.application').addHandler(app_log_handler)
    # logging.getLogger('tornado.general').addHandler(gen_log_handler)
    
    settings = {
        # "template_path":os.path.join(os.path.dirname(__file__), "templates"),
        # "static_path":os.path.join(os.path.dirname(__file__), "templates/static"),
        "static_path":os.path.join(os.path.dirname(__file__), "examples/"),
        "debug": True
    }
    application = Application([
        (r"/", PingHandler)
    ], **settings)
    http_server = HTTPServer(application)
    port = int(os.environ.get("PORT", 3000))
    http_server.listen(port)
    IOLoop.instance().start()

if __name__ == "__main__":
    main()