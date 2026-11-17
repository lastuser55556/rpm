class BookingBook:
    def __init__(self):
        self._by_slot = {}

    def reserve(self, slot, request_id):
        requests = self._by_slot.setdefault(slot, set())
        if request_id in requests:
            return False
        if len(requests) >= 4:
            return False
        requests.add(request_id)
        return True

    def cancel(self, slot, request_id):
        requests = self._by_slot.get(slot)
        if not requests or request_id not in requests:
            return False
        requests.remove(request_id)
        if not requests:
            del self._by_slot[slot]
        return True
