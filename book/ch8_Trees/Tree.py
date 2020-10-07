"""
    This code is on page 307 of the book: Data Structures and Algorithms in Python
"""

class Tree:
    """ Abstract base class representing a tree structure """

    # Nested Position class
    class Position:
        """ An abstraction representing the location of a single element. """

        def element(self):
            """ Return the element stored at this position """
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """ Return True if other position presents the same location """
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Return True if other does not represent the same location """
            return not (self == other)

    
    # Abstract methods that concrete subclass must support
    def root(self):
        """ Return Position representing the tree s root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self):
        """ Return Position representing p s parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """ Return the number of children that Position p has. """
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """ Generate an iteration of Positions representing p's children """
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """ Return the total number of elements in the tree. """
        raise NotImplementedError("must be implemented by subclass")

    # Concrete methods implemented in this class
    def is_root(self, p):
        """ Return True if Position p represents the root of the tree."""
        return self.root( ) == p
    
    def is_leaf(self, p):
        """ Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """ Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """ Return the number of levels seperating Position p from the root. """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """ Return the height of the subtree rooted at Position p. """
        if self.is_leaf(p):
            return 0

        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        """ 
            Return the height of the subtree rooted at Position p

            If p is None, return the height of the entire tree.
        """
        if p is None: p = self.root()
        
        return self._height(p)