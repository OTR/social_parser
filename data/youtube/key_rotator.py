"""
"""
from data.youtube.csv_key_value_storage import CSVKeyValueStorage

class KeyRotator:
    """"""

    def __init__(self, keys: list[str], storage: CSVKeyValueStorage):
        """"""
        if not keys:
            raise ValueError("API keys list cannot be empty.")
        self._keys = keys
        self._storage = storage
        self._current_key_index = 0

    def get_current_key(self) -> str:
        """Returns the current API key."""
        return self._keys[self._current_key_index]

    def rotate_key(self) -> str:
        """Rotates to the next available key."""
        starting_index = self._current_key_index
        while True:
            self._current_key_index = (self._current_key_index + 1) % len(self._keys)
            key = self.get_current_key()
            if self._storage.is_key_available(key):
                return key
            if self._current_key_index == starting_index:
                raise Exception("No available API keys to rotate to.")
    
    def record_quota_exceeded(self):
        """Record the quota exceeded time for the current key."""
        current_key = self.get_current_key()
        self._storage.update_quota_exceeded_time(current_key)
