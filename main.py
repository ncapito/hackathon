import json
import webapp2
import time
import datetime
import device as d
import json
import model
from json import JSONEncoder


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


class GetAllDeviceHandler(RestHandler):

  def get(self):
    things = d.AllDevices()
    r = [ AsDict(device) for device in things ]
    self.SendJson(r)

class GetDeviceHandler(RestHandler):

  def get(self, deviceID, activity):
    self.SendJson({'DeviceID': deviceID})

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
    ('/api/device/(.+)/checkin', CheckinDeviceCheckinHandler),
    ('/api/device/(.+)/', GetDeviceHandler),
    ('/api/device/', GetAllDeviceHandler),
], debug=True)
