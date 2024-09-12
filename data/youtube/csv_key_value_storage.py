"""

"""
import csv
from datetime import datetime, timedelta
import os

class CSVKeyValueStorage:
    """"""
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._initialize_file()

    def _initialize_file(self):
        """Initialize the CSV file if it does not exist."""
        if not os.path.exists(self._file_path):
            with open(self._file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['key', 'last_quota_exceeded'])

    def _read_storage(self) -> dict:
        """Read the CSV file and return the data as a dictionary."""
        storage = {}
        with open(self._file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['last_quota_exceeded']:
                    storage[row['key']] = datetime.fromisoformat(row['last_quota_exceeded'])
                else:
                    storage[row['key']] = None
        return storage

    def _write_storage(self, storage: dict):
        """Write the dictionary data back to the CSV file."""
        with open(self._file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['key', 'last_quota_exceeded'])
            for key, last_time in storage.items():
                writer.writerow([key, last_time.isoformat() if last_time else ''])

    def update_quota_exceeded_time(self, key: str):
        """Update the quota exceeded time for a specific key."""
        storage = self._read_storage()
        storage[key] = datetime.now()
        self._write_storage(storage)

    def is_key_available(self, key: str) -> bool:
        """Check if 24 hours have passed since the last quota exceeded time."""
        storage = self._read_storage()
        last_time = storage.get(key)
        if last_time is None:
            return True
        return datetime.now() - last_time >= timedelta(days=1)

    def get_next_available_key(self, keys: list[str]) -> str:
        """Return the next available key from the list."""
        storage = self._read_storage()
        for key in keys:
            if self.is_key_available(key):
                return key
        raise Exception("No keys available that have not exceeded their quota in the last 24 hours.")
