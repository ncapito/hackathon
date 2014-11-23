from google.appengine.ext import ndb
import datetime

class DeviceUpdate(ndb.Model):
  title = ndb.StringProperty()
  body = ndb.StringProperty()
  percent = ndb.IntegerProperty()
  updateDate = ndb.DateTimeProperty()

def AllDeviceUpdates():
    return DeviceUpdate.query()

def Save(deviceID, payload):
    d =  DeviceUpdate.query().filter(ndb.StringProperty("title") == deviceID).get()
    if(d is None):
        d = DeviceUpdate(title=deviceID)
    d.percent=payload
    d.updateDate=datetime.datetime.now()
    d.put()
    return d

def Update(title, body):
    d = DeviceUpdate(title=title, body=body, updateDate=datetime.datetime.now())
    d.put()
    return d
