import json
import webapp2
import time
import datetime
import device as d
import json
import model
import logging
from json import JSONEncoder

from google.appengine.api import urlfetch

def AsDict(device):
  return {'id': device.key.id(), 'activity': device.activity, 'lastCheckIn': device.lastCheck, 'room': device.room, 'deviceID': device.deviceID}

class JSONDateEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime.date):
      return obj.isoformat()
    return JSONEncoder.default(self, obj)

class RestHandler(webapp2.RequestHandler):

  def dispatch(self):
    #time.sleep(1)
    super(RestHandler, self).dispatch()


  def SendJson(self, r):
    self.response.headers['content-type'] = 'text/plain'
    self.response.write(json.dumps(r,cls=JSONDateEncoder))



class IDeviceHandler(RestHandler):
    def post(self,deviceID = None):
        r = json.loads(self.request.body)
        logging.info("Just got something" + self.request.body)
        device_id = None
        payload = None
        if('bit_id' in r):
            bit_id = r['bit_id']
        if('payload' in r):
            payload = r['payload']['percent']
        if('percent' in r):
            payload = r['percent']
        model.Save(bit_id, payload)
        logging.info(" saving " + bit_id + " " + str(payload))


    def get(self, deviceID = None, action = None):
        d = model.AllDeviceUpdates()
        r = [ device.to_dict() for device in d ]
        self.SendJson(r)



APP = webapp2.WSGIApplication([
    ('/api/devices/(.*)', IDeviceHandler),
], debug=True)
