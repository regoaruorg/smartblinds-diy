#!/usr/bin/env python
import web
import subprocess

urls = (
    '/getbattery/(.*)', 'get_battery',
    '/getposition/(.*)', 'get_position',
    '/moveup/(.*)', 'move_up',
    '/movedown/(.*)', 'move_down',
    '/setposition/(.*)/(.*)', 'set_position'
)

app = web.application(urls, globals())

class get_battery:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/usr/src/smartblinds-diy/control.py', '-t', mac, '-c', 'get_battery'])
        return output

class get_position:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/usr/src/smartblinds-diy/control.py', '-t', mac, '-c', 'get_position'])
        return output

class move_down:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/usr/src/smartblinds-diy/control.py', '-t', mac, '-c', 'move_down'])
        return "OK"

class move_up:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','/usr/src/smartblinds-diy/control.py', '-t', mac, '-c', 'move_up'])
        return "OK"

class set_position:
    def GET(self, mac, position):
        output = subprocess.check_output(['/usr/bin/python','/usr/src/smartblinds-diy/control.py', '-t', mac, '-c', 'move_target', '-a', position])
        return "OK"


if __name__ == "__main__":
    app.run()