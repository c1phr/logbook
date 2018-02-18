from events.event import Event


class AircraftSeenEvent(Event):
    def __init__(self, registration):
        super(AircraftSeenEvent, self).__init__()
        self.registration = registration
        self.type = 'AircraftSeenEvent'

    def serialize(self):
        return {
            'event_id': self.event_id,
            'timestamp': self.timestamp,
            'type': self.type,
            'registration': self.registration
        }
    
    def to_dynamo(self):
        return {
            'eventId': {'S': str(self.event_id)},
            'timestamp': {'N': str(self.timestamp)},
            'type': {'S': self.type},
            'registration': {'S': self.registration}
        }
    
    @staticmethod
    def fromJson(json):
        registration = json.get('registration')
        return AircraftSeenEvent(registration)