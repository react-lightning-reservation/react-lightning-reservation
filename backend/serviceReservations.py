#!/usr/bin/env python3
import json
import web
import xml.etree.ElementTree as ET

f = open('slot_data.json')
data = json.load(f)
f.close()

urls = (
    '/slots', 'list_slots',
    '/slots/(.*)', 'get_slot'
)

app = web.application(urls, globals())

class list_slots:        
    def GET(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        return json.dumps(data)

class get_slot:
    def GET(self, id):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        # return json.dumps(data['slots'][1])
        for s in data['slots']:
            if s['id'] == id:
                return json.dumps(s)
        web.notfound(self)
        return "not found"

if __name__ == "__main__":
    app.run()