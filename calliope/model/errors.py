class DuplicateTagNameError(ValueError):
    pass

class TagInUseError(ValueError):
    def __init__(self, blocking_entries):
        self.blocking_entries = blocking_entries
        super().__init__(f"This tag is the only tag on {len(blocking_entries)} entries")

class DefaultTagError(ValueError):
    pass