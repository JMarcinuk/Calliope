import uuid

from calliope.model.entry import Entry
from calliope.model.tag import Tag

from calliope.model.errors import DuplicateTagNameError

class Collection:
    def __init__(self, title, description, default_tags, id=None, char_limit=None, entries=None, tags=None):
        self.title = title
        self.description = description
        self._default_tags = default_tags

        self._id = id if id is not None else uuid.uuid4().hex

        self.char_limit = char_limit

        # entries and tags should load existing lists if they exist, or create a new one if they don't
        if entries is not None:
            self._entries = {entry.id: entry for entry in entries}
        else:
            self._entries = {}
        
        if tags is not None:
            self._custom_tags = {tag.id: tag for tag in tags}
        else:
            self._custom_tags = {}

    def _name_taken(self, tag_name, ignore_id=None):
        input = tag_name.strip().casefold()
        return any(
            tag.name.strip().casefold() == input
            for tag in self.available_tags().values()
            if tag.id != ignore_id
        )

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title data type invalid.")
        if len(new_title) > 50:
            raise ValueError("Collection title is too long.")
        self._title = new_title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_desc):
        if not isinstance(new_desc, str):
            raise TypeError("Description data type invalid.")
        if len(new_desc) > 500:
            raise ValueError("Collection description is too long.")
        self._description = new_desc

    @property
    def char_limit(self):
        return self._char_limit

    @char_limit.setter
    def char_limit(self, limit):
        self._char_limit = limit

    # entries and tags return copies of themselves so that they are not mutable in other classes
    # their contents remain mutable through the shallow copy, though
    @property
    def entries(self):
        return self._entries.copy()

    @property
    def custom_tags(self):
        return self._custom_tags.copy()

    # concatenates dicts of default and custom tags
    def available_tags(self):
        return {**self._default_tags, **self.custom_tags}

    def add_tag(self, tag_name, tag_color):
        if self._name_taken(tag_name):
            raise DuplicateTagNameError(f"A tag named '{tag_name}' already exists.")
        new_tag = Tag(tag_name, tag_color)
        self._custom_tags[new_tag.id] = new_tag
        return new_tag

    def add_entry(self, entry):
        pass

    def query(self, q):
        pass

    def blockingEntries(self, tag):
        pass

    def canDeleteTag(self, tag):
        pass

    def remove_entry(self, entry):
        pass

    def delete_tag(self, tag):
        pass

    def rename_tag(self, tag_id, new_name):
        pass