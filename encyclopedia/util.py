import re
import urllib
import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def fname(title):
    f = default_storage.open(f"entries/{title}.md", 'r')
    print("f is: ", f)
    # print(os.path.basename(f.name))
    fname = f.read()
    print("fname is: ", fname)
    return fname

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """


    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename).lower()
                for filename in filenames if filename.endswith(".md")))

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        print("same name!!")
        return None
    else:
        print("new name")
        default_storage.save(filename, ContentFile(content))
        return 0

def save_edit(title, content):
    """
    Saves any changes a user makes to the content Markdown of a given entry.
    """
    f = open(f"entries/{title}.md", "w")
    f.write(content)
    print("File edit saved.")



def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

# transform entries to lowercase in order to compare search results

entries = list_entries()
def lowentry(entries):
    return [entry.lower() for entry in entries]