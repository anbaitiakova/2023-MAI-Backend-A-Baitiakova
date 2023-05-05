import LRUCache

cache = LRUCache.LRUCache(100)
print(cache.set('Jesse', 'Pinkman'))
print(cache.set('Walter', 'White'))
print(cache.set('Jesse', 'James'))
print(cache.get('Jesse')) # вернёт 'James'
print(cache.rem('Walter'))
print(cache.get('Walter')) # вернёт ''