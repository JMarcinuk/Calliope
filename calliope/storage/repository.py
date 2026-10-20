from pathlib import Path
import json
from datetime import datetime

from abc import ABC, abstractmethod

from calliope.model.library import Library
from calliope.model.collection import Collection
from calliope.model.entry import Entry

class Repository(ABC):
    @abstractmethod
    def load_library(self) -> Library:
        """loads the library from the filesystem, creates the Library object and returns it"""
        pass

    @abstractmethod
    def save_library(self, library: Library):
        """Writes changes to a Library object to the filesystem"""
        pass

    @abstractmethod
    def save_collection(self, collection: Collection):
        """Writes changes to a collection object to the filesystem"""
        pass

    @abstractmethod
    def delete_collection(self, collection_id: str):
        """removes a collection from the filesystem"""
        pass

    @abstractmethod
    def save_entry(self, collection: Collection, entry: Entry):
        """writes an entry to a specific collection and saves changes to the filesystem"""
        pass

    @abstractmethod
    def delete_entry(self, collection: Collection, entry_id: str):
        """removes an entry from a collection and saves changes to filesystem"""
        pass

class MarkdownFolderRepository(Repository):
    def __init__(self, root_path: Path):
        self._root_path = root_path

    def _read_entry(self, file: Path) -> Entry:
        raw_file = file.read_text(encoding="utf-8")
        file_list = raw_file.split("---\n", maxsplit=2)
        metadata = json.loads(file_list[1])
        body = file_list[2]

        return Entry(title=metadata["title"], id=metadata["id"], created=datetime.fromisoformat(metadata["created"]), 
                     modified=datetime.fromisoformat(metadata["modified"]), body=body, tag_ids=metadata["tag_ids"])

    def _write_entry(self, folder: str, entry: Entry):
        entries_path = self._root_path / "collections" / folder / "entries"
        entries_path.mkdir(parents=True, exist_ok=True)

        metadata = {
            "id": entry.id,
            "title": entry.title,
            "tag_ids": sorted(entry.tag_ids),
            "created": entry.created.isoformat(),
            "modified": entry.modified.isoformat()
        }

        divider = "---"
        filetext = (divider, json.dumps(metadata, indent=2, ensure_ascii=False), divider, entry.body)

        new_entry = entries_path / f"{entry.id}.md"
        tmp_file = new_entry.with_suffix(".tmp")

        tmp_file.write_text("\n".join(filetext), encoding="utf-8")
        tmp_file.replace(new_entry)

    def load_library(self) -> Library:
        raise NotImplementedError

    def save_library(self, library: Library):
        raise NotImplementedError

    def save_collection(self, collection: Collection):
        raise NotImplementedError

    def delete_collection(self, collection_id: str):
        raise NotImplementedError

    def save_entry(self, collection: Collection, entry: Entry):
        raise NotImplementedError

    def delete_entry(self, collection: Collection, entry_id: str):
        raise NotImplementedError