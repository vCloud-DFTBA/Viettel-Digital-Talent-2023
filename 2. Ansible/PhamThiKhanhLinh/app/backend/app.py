from pymongo import MongoClient
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import json 


def get_database(name):
   CONNECTION_STRING = "mongodb://kilinh:Linh2812@mongo:27017/"
   client = MongoClient(CONNECTION_STRING)
   return client[name]

class APIHandler(BaseHTTPRequestHandler): 
    def do_GET(self): 
        print('Get Data')
        if self.path == '/api':
            self.send_response(200) 
            self.send_header('Content-Type', 'application/json') 
            self.end_headers() 

            # Connect to database
            dbname = get_database("VDT2023")
            collection_name = dbname["attendees"]

            # Query data
            item_details = collection_name.find()

            data = []
            for item in item_details:
               data.append({k: v for k, v in item.items() if k != '_id'})

            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))  
        else: 
            self.send_response(404)
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
  
if __name__ == "__main__":
    print('begin..')
    httpd = HTTPServer(('0.0.0.0', 8000), APIHandler) 
    print('Backend running...')
    httpd.serve_forever()
