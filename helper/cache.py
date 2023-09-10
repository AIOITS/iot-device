import cachetools

class Cache():
  token_cache = cachetools.LRUCache(maxsize=10)

  @classmethod
  def get_cache(cls, name):
    token = cls.token_cache.get(name)
    return token

  @classmethod
  def save_cache(cls, name, value):
    cls.token_cache[name] = value
