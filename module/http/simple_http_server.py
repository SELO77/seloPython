# 일시적인 로그 남기기 스크립트

import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer


import pymongo

## AWS 사용시 허용 포트인지 확인 필요
PORT_NUMBER = 8083
API_KEY = "SELO"


class tempHTTPServer_RequestHandler(BaseHTTPRequestHandler):


  # def __init__(self):
  #   super(tempHTTPServer_RequestHandler, self).__init__()
    # self.config_info = self.read_config()


  def do_GET(self):
    print("GET PATH:%s"%self.path)
    self.send_response(200)

    query_string = self.parsing_path()
    message = str(self.write_data(query_string))

    # message to client
    # self.wfile.write('success', 'utf8')
    try:
      self.wfile.write(bytes(message, 'utf8'))
      self.wfile.write(bytes('pong', 'utf8'))
    except:
      print(traceback.format_exc())



  def parsing_path(self):
    result = {}
    if isinstance(self.path, str):
      for i, v in enumerate(self.path.split('&')):
        if i == 0:
          v = v.replace('/?', '')
        temp_list = v.split('=')
        result[temp_list[0]] = temp_list[1]
    return result


  def write_data(self, query_string):
    try:
      self.config_info = self.read_config()
      print(self.config_info)
      client = pymongo.MongoClient(self.config_info.get('host'), 27017)
      db = client.TraportLog
      return db.traportLeaveMember.save(query_string)
    except:
      print(traceback.format_exc())
      return traceback.format_exc()


  def read_config(self):
    config_info = {}
    try:
      with open('config', 'r') as f:
        while True:

          line = f.readline()
          if not line: break
          temp_list = line.split('=')
          config_info[temp_list[0]] = temp_list[1].replace('\n', '')

      return config_info
    except:
      print(traceback.format_exc())


def run():
  print('starting http server...')
  server_address = ('localhost', PORT_NUMBER)
  httpd = HTTPServer(server_address, tempHTTPServer_RequestHandler)
  print('running http server...')
  httpd.serve_forever()

run()