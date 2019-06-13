# LRU Cache Solution

The solution for the LRU cache is implemented in two python modules.
`lru_cache.py ` contains the cache class `LRUCache`. And `linked_list.py`
implements a doubly linked list which serves as the store for the cache
entries.

## Design

The first goal of the cache is to enable fast storage and lookup of data
items. Each of these operations, `get()` and `set()` should run in constant
time. To achieve this requires a hash based look up for cache keys. The
implementation uses a python dictionary for this.

The second design goal is to enable the cache to have a fixed capacity and to
flush cache entries in least recently used (LRU) order. To achieve this
requires a way to track cache accesses and know which item (or items) was
accesses the longest ago. To achieve this I decided to store each cache entry
in a doubly linked list. This allows an accessed entry to be moved to the
front of the list in constant time on every access. And thus ensures that the
tail of the list contains the element that was accessed least recently.

## Runtime analysis

Assuming a cache size of n.

The get() operation performs a lookup in the index dictionary which is O(1).
It then removes the element from the cache store list O(1) and inserts is at
the head of the cache store O(1). So the overall complexity of get() is O(1).

The set() operation performs an in test to see if the key is in the index. If
it is then the entry is updated and moved to the front of the cache store.
Both of these operations are O(1). If it is not in the list then the capacity
is checked. This requires testing the len() of the index (O(n)) and then if
the capacity is exceeded, removing elements from the tail of the list until
the list is under capacity. Removing items from the tail of the list will be
O(1) so unless the capacity is reduced we would expect this to be a constant
time operation as well.

For each cache entry we are maintaining a `DNode` which requires forward and
back pointers as well as storing the key for entry in the index. This is
additional overhead per entry. In addition the dictionary will require space
proportional to the capacity of the cache. It is possible to reduce the
storage requirements of the cache by lowering the capacity value, but this
would only reduce the number of active elements in storage and wouldn't
impact th space required for the index.
