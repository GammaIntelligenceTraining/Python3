import wikipedia
print(wikipedia.summary("Wikipedia"))
# Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...
#
wikipedia.search("Barack")

ny = wikipedia.page(title="New York City")
print(ny.title)
# u'New York'
print(ny.url)
# u'http://en.wikipedia.org/wiki/New_York'
print(ny.content)
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
print(ny.links[0])
# u'1790 United States Census'

print(wikipedia.set_lang("fr"))
# print(wikipedia.summary("Facebook", sentences=1))