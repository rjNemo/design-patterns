"""
The client code may or may not know about the Concrete Iterator or Collection
classes, depending on the level of indirection you want to keep in your program.
"""
from behavioral.iterator.alpha_order_iterator import WordCollection

collection = WordCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")

print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()), end="")
