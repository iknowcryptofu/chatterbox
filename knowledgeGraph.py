import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='KnowledgeGraphTest (iknowcryptofu@gmail.com)', language='en')

pages = ['Wasabi', 'Shamrock','Grasshopper','Statue_of_Liberty']


def fetch_and_save_pages(page_titles: list, wiki: wikipediaapi.Wikipedia, output_dir: str = '.'):
    """Fetch each Wikipedia page in *page_titles* using *wiki* and save its text to a file.

    Each page will be written to '<title>.txt' under *output_dir*.  If the page does not
    exist a warning will be printed and no file will be created for it.
    """
    import os

    os.makedirs(output_dir, exist_ok=True)

    for title in page_titles:
        page = wiki.page(title)
        if not page.exists():
            print(f"Warning: page '{title}' does not exist, skipping")
            continue

        filename = os.path.join(output_dir, f"{title}.txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(page.text)
        print(f"Wrote {filename} ({len(page.text)} bytes)")


page_py = wiki_wiki.page('Wasabi')

page_py2 = wiki_wiki.page('Python_(programming_language)')
print("Page - Exists: %s" % page_py.exists())
# Page - Exists: True

page_missing = wiki_wiki.page('NonExistingPageWithStrangeName')
print("Page - Exists: %s" %     page_missing.exists())
# Page - Exists: False

print("Page - Title: %s" % page_py.title)
# Page - Title: Python (programming language)

print("Page - Summary: %s" % page_py.summary[0:60])
# Page - Summary: Python is a widely used high-level programming language for

wiki_wiki2 = wikipediaapi.Wikipedia(
    user_agent='MyProjectName (merlin@example.com)',
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

p_wiki = wiki_wiki2.page("Test 1")
print(p_wiki.text)
# Summary
# Section 1
# Text of section 1
# Section 1.1
# Text of section 1.1
# ...


# Example usage of the helper defined earlier
if __name__ == '__main__':
    # fetch and save the pages listed in `pages` using the default wiki object
    fetch_and_save_pages(pages, wiki_wiki2, output_dir='wiki_pages')

