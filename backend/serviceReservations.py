#!/usr/bin/env python3
import web
import xml.etree.ElementTree as ET

tree = ET.parse('event_data.xml')
root = tree.getroot()

urls = (
    '/events', 'list_events',
    '/events/(.*)', 'get_event'
)

app = web.application(urls, globals())

class list_events:        
    def GET(self):
        output = 'events:[';
        for child in root:
            print('child', child.tag, child.attrib)
            output += str(child.attrib) + ','
        output += ']';
        return output

class get_event:
    def GET(self, id):
        for child in root:
            if child.attrib['id'] == id:
                return str(child.attrib)

if __name__ == "__main__":
    app.run()