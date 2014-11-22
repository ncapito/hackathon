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

class QueryHandler(RestHandler):

  def get(self):
    #guests = model.AllGuests()
    #r = [ AsDict(guest) for guest in guests ]
    #self.SendJson(r)
    #temp = model.Test()
    #if temp != None:
    #    temp = temp.to_dict()

    things = d.AllDevices()
    r = [ AsDict(device) for device in things ]
    self.SendJson(r)


    #self.SendJson(temp)


class CheckinDeviceCheckinHandler(RestHandler):

  def get(self, deviceID):
    r = d.UpdateDevice(deviceID, self.request.motion, datetime.datetime.now())
    self.SendJson(r)


class CheckinDeviceUpdateHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    model.Update(r['title'], r['body'])
    self.SendJson(r)


class DeviceUpdateHandler(RestHandler):

  def get(self):
    d = model.AllDeviceUpdates()
    r = [ device.to_dict() for device in d ]
    self.SendJson(r)


class GetAllDeviceHandler(RestHandler):

  def get(self):
    things = d.AllDevices()
    r = [ AsDict(device) for device in things ]
    self.SendJson(r)

class GetDeviceHandler(RestHandler):

  def get(self, deviceID, activity):
    self.SendJson({'DeviceID': deviceID})

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
        model.Save(bit_id, payload)
        logging.info(" saving " + bit_id + " " + str(payload))


    def get(self, deviceID = None, action = None):
        url = "https://api-http.littlebitscloud.cc/devices"
        token = "e2110423b7a483d778daf6525141e2bbb694b8eb71cd04da1c27414f7e328711"
        headers = { "Authorization" : "Bearer " + token,"Accept" : "application/vnd.littlebits.v2+json"}
        if(deviceID is not None):
            url += "/" + deviceID
        if(action is not None):
            url += "/" + action

        print url
        result = urlfetch.fetch(url, headers=headers)
        self.response.headers['content-type'] = 'text/plain'
        self.response.write(result.content)



class UpdateHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    device = d.UpdateDevice(r.deviceID, self.request.motion, datetime.datetime.now())
    r = AsDict(device)
    self.SendJson(r)


class InsertHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    device = d.InsertGuest(r.room, r.deviceID)
    r = AsDict(device)
    self.SendJson(r)


class DeleteHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    d.DeleteDevice(r['id'])


APP = webapp2.WSGIApplication([
    ('/rest/query', QueryHandler),
    ('/rest/insert', InsertHandler),
    ('/rest/delete', DeleteHandler),
    ('/rest/update', UpdateHandler),
    ('/api/idevices/', IDeviceHandler),
    ('/api/idevices/(.*)', IDeviceHandler),
    ('/api/devices/(.*)', IDeviceHandler),
    ('/api/idevices/(.*)/(.*)', IDeviceHandler),
    ('/api/deviceupdate', CheckinDeviceUpdateHandler),
    ('/api/devices/', DeviceUpdateHandler),
    ('/api/device/(.+)/checkIn', CheckinDeviceCheckinHandler),
    ('/api/device/(.+)', GetDeviceHandler),
    ('/api/device/', GetAllDeviceHandler),
], debug=True)
