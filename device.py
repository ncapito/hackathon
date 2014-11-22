from google.appengine.ext import ndb
import datetime

class Device(ndb.Model):
  room = ndb.StringProperty()
  deviceID = ndb.StringProperty()
  lastCheck = ndb.DateTimeProperty()
  activity = ndb.BooleanProperty()


def AllDevices():
  return Device.query()


def UpdateDevice(deviceID, activity, lastCheck):
  device = Device(deviceID=deviceID, activity=activity, lastCheck=datetime.datetime.now())
  device.put()
  return device


def InsertDevice(room, deviceID):
  device = Device(room=room, deviceID=deviceID, lastCheck=datetime.datetime.now(), activity=False)
  device.put()
  return device


def DeleteDevice(id):
  key = ndb.Key(Device, id)
  key.delete()
