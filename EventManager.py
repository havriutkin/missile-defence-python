class EventManager:
    """Class for event managing. Contains list of observers and notifies them"""
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_all(self, message, data):
        for observer in self.observers:
            observer.get_message(message, data)
