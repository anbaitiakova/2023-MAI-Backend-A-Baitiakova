import LRUCache

cache = LRUCache.LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.get('Jesse') # вернёт 'James'
cache.rem('Walter')
cache.get('Walter') # вернёт ''