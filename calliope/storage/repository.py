from pathlib import Path

from abc import ABC, abstractmethod

from calliope.model.library import Library
from calliope.model.collection import Collection
from calliope.model.entry import Entry

class Repository(ABC):
    @abstractmethod
    def load_library() -> Library:
        """loads the library from the filesystem, creates the Library object and returns it"""
        pass

    @abstractmethod
    def save_library(library: Library):
        """Writes changes to a Library object to the filesystem"""
        pass

    @abstractmethod
    def save_collection(collection: Collection):
        """Writes changes to a collection object to the filesystem"""
        pass

    @abstractmethod
    def delete_collection(collection_id):
        """removes a collection from the filesystem"""
        pass

    @abstractmethod
    def save_entry(collection, entry):
        """writes an entry to a specific collection and saves changes tot he filesystem"""
        pass

    @abstractmethod
    def delete_entry(collection, entry_id):
        """removes an entry from a collection and saves changes to filesystem"""
        pass

class MarkdownFolderRepository(Repository):
    def __init__(root_path: Path):
        _root_path = root_path

    def _read_entry(file) -> Entry:
        pass

    def _write_entry(folder, entry):
        pass