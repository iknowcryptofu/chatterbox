import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(user_agent='KnowledgeGraphTest (iknowcryptofu@gmail.com)', language='en')

pages[] = ['Wasabi', 'Shamrock','Grasshopper','Statue_of_Liberty']

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