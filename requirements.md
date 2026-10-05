A basic list of goals and requirements for the project.

Non-Technical Requirements
- Opens to show a GUI of "Collections" which are folders that can be clicked on, this main screen is called the "Library"
- Each collection can contain "Entries" which are individual bits of text contained in that Collection.
- Each entry has a title, body, and at least one "Tag." It also has metadata like when it was created and last edited.
- When in a collection its Entries are shown in a neat list reminiscent of Discord's forum channels with the title of the Entry, the body (or a preview, if it's more than 5 or 6 lines long), and a list of that Entry's tags (which may also be shortened if there are more than 3)
- A tag merely possesses a name and a color. When displayed, the name is in a capsule-shaped bubble with it's color dot to the left, and the bubble has an outline in the tag's color.
- While in an entry, tags can be assigned an unassigned to that entry with a simple checkbox interface
- There is a default list of tags, but custom ones can be added to Collections. Custom tags cannot be used outside the collection they were added to.
- While in a collection, one can create an entry, upon which they will be brought to an entry composition screen, and prompted to title and tag the entry before it is saved to the collection.
- At the collection level, the user can filter tags to only show results with certain tags. They may use an exclusive filter that shows only entries with the tags selected. They may also use an inclusive filter that shows entries with *any one of* the tags selected.
- Entries in a collection can be sorted by recency, length, or alphabetically by title.
- At the library level, a collection can be created. That collection is given a title, description, and (optionally) a per entry character limit. Entries above a collection's character limit cannot be submitted.
- While in a collection, keywords can be searched to locate entries by their body and title content.
- Collections can be exported to a folder of markdown files
- At the collection level, there is a tag manager screen where tags can easily be added, edited, and deleted (with an "are you sure?" screen). When creating tags, you're offered an 8-bit color selector for color-coding the tag.
- Entry editor has a rich-text editor bar with buttons for standard rich text/markdown formatting (bold, italic, underline, bullet list, etc)

Technical Requirements:
- Can run as a standalone program in as close to a fresh windows installation as possible (minimal dependencies). Ubuntu compatibility is a stretch goal.
- Supports markdown
- Is entirely self-contained, ease of use feels like opening the sticky notes app on windows except it runs in just one window.