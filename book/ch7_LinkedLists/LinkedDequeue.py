from DoublyLinkedBase import _DoublyLinkedBase
from Error import Empty

class LinkedDeque(_DoublyLinkedBase):
    """ Double-ended queue implementation based on a doubly linked list. """

    def first(self):
        if self.is_empty(): raise Empty("Deque is empty")

        return self._header._next._element

    def last(self):
        if self.is_empty(): raise Empty("Deque is empty")

        return self._trialer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trialer._prev, self._trialer)

    def delete_first(self):
        if self.is_empty(): raise Empty("Deque is empty")

        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty(): raise Empty("Deque is empty")
        return self._delete_node(self._trialer._prev)