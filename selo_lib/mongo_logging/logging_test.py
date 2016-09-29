import logging
from mongo_logger import SELOLogger

class EmailSMSLog(SELOLogger):
    collection = "m2t_logsms"
    fields = ("recipient", "body", "timestamp", "error", "fromnumber")

    def __init__(self):
        SELOLogger.__init__(self, collection=self.collection)


emailSMSLog = EmailSMSLog()
emailSMSLog.create(**{
    "name": "SELO",
    "phone": "001-5678-9999"
})
emailSMSLog.create(name="SERIM", address="Seoul, Korea")
# emailSMSLog.create("what", hello={
#     "name": "SELO",
# })

