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
    d = DeviceUpdate(title=deviceID, percent=payload, updateDate=datetime.datetime.now())
    d.put()
    return d

def Update(title, body):
    d = DeviceUpdate(title=title, body=body, updateDate=datetime.datetime.now())
    d.put()
    return d

class Guest(ndb.Model):
  first = ndb.StringProperty()
  last = ndb.StringProperty()
  dateTime = ndb.DateTimeProperty()


def AllGuests():
  return Guest.query()

def Test():
    return Guest.query().filter(ndb.StringProperty("first") == 'Nick').get()

def UpdateGuest(id, first, last):
  guest = Guest(id=id, first=first, last=last)
  guest.put()
  return guest


def InsertGuest(first, last):
  guest = Guest(first=first, last=last, dateTime=datetime.datetime.now())
  guest.put()
  return guest


def DeleteGuest(id):
  key = ndb.Key(Guest, id)
  key.delete()
