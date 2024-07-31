import wikipedia

print('the NAV search engine')

print("WARNING!:this search engine is not fully complete,so you can't type space but the search still works without space.also it only shows the result if there is a page according to your search.")

wikipedia.set_lang('en')

query = str(input('search here : '))

print(wikipedia.summary(query))

input('exit ?: ')


