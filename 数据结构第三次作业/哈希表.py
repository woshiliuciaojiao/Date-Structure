class HashTable:
    def __init__(self, initial_capacity=8, load_factor_threshold=0.75):
        self.capacity = initial_capacity
        self.load_factor_threshold = load_factor_threshold
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    def _hash_function(self, key):
        return hash(key) % self.capacity
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        load_factor = self.size / self.capacity
        if load_factor > self.load_factor_threshold:
            self._resize()
    def get(self, key, default=None):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return default
    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return v
        return None
    def __str__(self):
        items = []
        for bucket in self.buckets:
            if bucket:
                items.extend([f"{k}: {v}" for k, v in bucket])
        return "{" + ", ".join(items) + "}"


ht = HashTable()
ht.put("name", "Alice")
ht.put("age", 25)
ht.put("city", "Beijing")
print("插入后哈希表：", ht)
print("查询name：", ht.get("name"))  # Alice
ht.put("age", 26)
print("修改age后：", ht)
ht.remove("city")
print("删除city后：", ht)  # {name: Alice, age: 26}
for i in range(10):
    ht.put(f"key{i}", f"value{i}")
print("扩容后哈希表：", ht)
print("当前容量：", ht.capacity)  # 扩容后容量变为16（初始8，超过负载因子后翻倍）