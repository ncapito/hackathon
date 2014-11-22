import json
import webapp2
import time
import datetime
import model
import json
from json import JSONEncoder


def AsDict(guest):
  #jsonEncoder = jsonEncoder(guest.dateTime)
  return {'id': guest.key.id(), 'time': guest.dateTime, 'first': guest.first, 'last': guest.last}

class jsonEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime.datetime):
      return obj.isoformat()
    return(json.jsonEncoder.default(self, obj))

class RestHandler(webapp2.RequestHandler):

  def dispatch(self):
    #time.sleep(1)
    super(RestHandler, self).dispatch()


  def SendJson(self, r):
    self.response.headers['content-type'] = 'text/plain'
    self.response.write(json.dumps(r,cls=JSONDateEncoder))

class QueryHandler(RestHandler):

  def get(self):
    guests = model.AllGuests()
    r = [ AsDict(guest) for guest in guests ]
    self.SendJson(r)


class CheckinDeviceCheckinHandler(RestHandler):

  def get(self):
    guests = model.AllGuests()
    r = [ AsDict(guest) for guest in guests ]
    self.SendJson(r)


class GetAllDeviceHandler(RestHandler):

  def get(self):
    guests = model.AllGuests()
    r = [ AsDict(guest) for guest in guests ]
    self.SendJson(r)

class GetDeviceHandler(RestHandler):

  def get(self, deviceID):
    self.SendJson({'DeviceID': deviceID, 'dateTime': datetime.datetime.now()})


class UpdateHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    guest = model.UpdateGuest(r['id'], r['first'], r['last'])
    r = AsDict(guest)
    self.SendJson(r)


class InsertHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    guest = model.InsertGuest(r['first'], r['last'])
    r = AsDict(guest)
    self.SendJson(r)


class DeleteHandler(RestHandler):

  def post(self):
    r = json.loads(self.request.body)
    model.DeleteGuest(r['id'])


APP = webapp2.WSGIApplication([
    ('/rest/query', QueryHandler),
    ('/rest/insert', InsertHandler),
    ('/rest/delete', DeleteHandler),
    ('/rest/update', UpdateHandler),
    ('/api/device/(.+)\/checkin', CheckinDeviceCheckinHandler),
    ('/api/device/(.+)', GetDeviceHandler),
    ('/api/device', GetAllDeviceHandler),
], debug=True)
