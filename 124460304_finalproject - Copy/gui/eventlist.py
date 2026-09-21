#Feature 1
class Event:
    def __init__(self, event):
        self.data = event      # event text
        self.next = None       # pointer to next node


class EventList:
    def __init__(self, max_events=10):
        self.head = None       # start of the list
        self.length = 0
        self.max_events = max_events

    def add_event(self, event_text):
        """Insert a new event at the head of the list."""
        new_event = Event(event_text)
        new_event.next = self.head
        self.head = new_event
        self.length += 1

        # Trim list if too long
        if self.length > self.max_events:
            self._remove_last()

    def _remove_last(self):
        """Remove the final node in the list."""
        current = self.head
        prev = None

        while current.next is not None:
            prev = current
            current = current.next

        if prev is not None:
            prev.next = None

        self.length -= 1

    def print_events(self):
        """Print all events from newest to oldest."""
        print("\nRecent Events:")
        current = self.head
        while current is not None:
            print(" -", current.data)
            current = current.next
        print()
