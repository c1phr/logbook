import uuid
import time


class Event:
    def __init__(self):
        self.event_id = uuid.uuid4()
        self.timestamp = int(time.time())
