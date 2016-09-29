from datetime import datetime, tzinfo, timedelta

ZERO = timedelta(0)
HOUR = timedelta(hours=1)

# UTC class.
class UTC(tzinfo):

  def utcoffset(self, date_time):
    return ZERO

  def tzname(self, date_time):
    return "UTC"

  def dst(self, date_time):
    return ZERO

utc = UTC()


class FixedOffset(tzinfo):

  def __init__(self, offset, name):
    self.__offset == timedelta(minutes = offset)
    self.__name = name

  def utcoffset(self, date_time):
    return self.__offset

  def tzname(self, date_time):
    return self.__name

  def dst(self, date_time):
    return ZERO


import time as _time

STDOFFSET = timedelta(seconds= -_time.timezone)
if _time.daylight:
  DSTOFFSET = timedelta(seconds= -_time.altzone)
else:
  DSTOFFSET = STDOFFSET

DSTDIFF = DSTOFFSET - STDOFFSET


class LocalTimezone(tzinfo):

  def utcoffset(self, date_time):
    if self.isdst(date_time):
      return DSTOFFSET
    else:
      return STDOFFSET

  def dst(self, date_time):
    if self._isdst(date_time):
      return DSTOFFSET
    else:
      return STDOFFSET

  def tzname(self, date_time):
    return _time.tzname[self._isdst(date_time)]

  def _isdst(self, date_time):
    tt = (date_time.year, date_time.month, date_time.day,
          date_time.hour, date_time.minute, date_time.second,
          date_time.weekday(), 0, 0)
    stamp = _time.mktime(tt)
    tt = _time.localtime(stamp)
    return tt.tm_isdst > 0

Local = LocalTimezone()





""" Abstract base class for time zone info objects. """
""" Daylight saving time, DST. It's summer time """
class USTimeZone(tzinfo):

  def __init__(self, hours, reprname, stdname, dstname):
    self.stdoffset = timedelta(hours=hours)
    self.reprname = reprname
    self.stdname = stdname
    self.dstname = dstname

  def __repr__(self): # predefined
    return self.reprname

  def tzname(self, date_time):
    if self.dst(date_time):
      return self.dstname
    else:
      return self.stdname

  def dst(self, date_time):
    if date_time is None or date_time.tzinfo is None:
      return
    assert date_time.tzinfo is self

    if 2006 < date_time.year:
      dststart, dstend = DSTSTART