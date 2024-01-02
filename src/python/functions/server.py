from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import pickle
from search_engine import SearchEngine

hostname = "localhost"
serverPort = 8080

with open('page_db_instance.pkl', 'rb') as file:
    loaded_page_db = pickle.load(file)

search_engine = SearchEngine(loaded_page_db)

class DataHandlerServer(BaseHTTPRequestHandler):
  def do_GET(self):
        if self.path == '/':
          self.send_header('Content-type','text/html')
          self.end_headers()
          self.wfile.write(bytes("Welcome!", "utf8"))
        else:
          self.send_response(404)
  def do_POST(self):
    if self.path == '/search':
      self.send_response(200)
      content_length = int(self.headers['Content-Length'])
      raw_data = self.rfile.read(content_length)
      search_request = json.loads(raw_data.decode('utf-8'))
      print(search_request['search'])
      search_response = search_engine.search(search_request['search'])
      search_response_json = json.dumps(search_response)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write(bytes(search_response_json, "utf8"))
    else:
      self.send_response(404)

with HTTPServer((hostname, serverPort), DataHandlerServer) as server:
  print(f'Starting server on port {serverPort}')
  server.serve_forever()