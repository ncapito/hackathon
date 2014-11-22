from google.appengine.ext import ndb
import datetime

class Guest(ndb.Model):
  first = ndb.StringProperty()
  last = ndb.StringProperty()
  dateTime = ndb.DateTimeProperty()


def AllGuests():
  return Guest.query()


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
