"""
Task 1: Data Structures. Sorting. Working with a Singly Linked List
"""

class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class LinkedList:
    """A simple singly linked list implementation."""
    def __init__(self):
        self.head = None

    def append(self, val):
        """Appends a new value to the end of the list."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Returns a string representation of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.val))
            current = current.next
        return " -> ".join(elements) if elements else "The list is empty"

    def to_list(self):
        """Converts the linked list to a regular Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

def reverse_list(head):
    """
    Reverses a singly linked list in place.
    
    Args:
        head: The head node of the linked list.
        
    Returns:
        The new head of the reversed list.
    """
    prev = None
    current = head

    while current:
        # Save the next node
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move prev forward
        prev = current
        # Move current forward
        current = next_temp

    return prev

def sort_linked_list(head):
    """
    Sorts a singly linked list using insertion sort.
    
    Args:
        head: The head node of the list.
        
    Returns:
        The head node of the sorted list.
    """
    if not head or not head.next:
        return head

    sorted_head = None
    current = head

    while current:
        next_temp = current.next
        sorted_head = insert_into_sorted_list(sorted_head, current)
        current = next_temp

    return sorted_head

def insert_into_sorted_list(head, new_node):
    """
    Inserts a node into a sorted linked list at the correct position.
    
    Args:
        head: Head of the sorted list.
        new_node: Node to be inserted.
        
    Returns:
        The head of the updated sorted list.
    """
    new_node.next = None

    if not head or head.val >= new_node.val:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.val < new_node.val:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

def merge_sorted(list1, list2):
    """
    Merges two sorted singly linked lists into one sorted list.
    
    Args:
        list1: Head of the first sorted list.
        list2: Head of the second sorted list.
        
    Returns:
        Head of the merged sorted list.
    """
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return dummy.next

def create_linked_list_from_array(arr):
    """Creates a linked list from a Python list."""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def linked_list_to_array(head):
    """Converts a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Demonstration of usage
def main():
    print()

    # Demonstration — Reversing a singly linked list
    print("1. Reversing a singly linked list:")

    reversed_list = LinkedList()
    for val in [10, 20, 30, 40, 50]:
        reversed_list.append(val)

    print(f"Original list: {reversed_list.display()}")

    # Apply reversal function
    reversed_list.head = reverse_list(reversed_list.head)
    print(f"Reversed list: {reversed_list.display()}\n")

    # Demonstration — Insertion sort on a singly linked list
    print("2. Sorting a singly linked list using insertion sort:")

    unsorted_list = LinkedList()
    for val in [45, 12, 78, 3, 29, 18, 56]:
        unsorted_list.append(val)

    print(f"Unsorted list: {unsorted_list.display()}")

    # Apply insertion sort
    unsorted_list.head = sort_linked_list(unsorted_list.head)
    print(f"Sorted list: {unsorted_list.display()}\n")

    # Demonstration — Merging two sorted linked lists
    print("3. Merging two sorted singly linked lists:")

    list1_head = create_linked_list_from_array([5, 15, 25])
    list2_head = create_linked_list_from_array([10, 20, 30])

    print(f"List 1: {linked_list_to_array(list1_head)}")
    print(f"List 2: {linked_list_to_array(list2_head)}")

    merged_head = merge_sorted(list1_head, list2_head)
    print(f"Merged list: {linked_list_to_array(merged_head)}\n")

    # Merging larger lists
    print("4. Merging two larger sorted linked lists:")

    big_list1 = create_linked_list_from_array([2, 8, 14, 22, 31])
    big_list2 = create_linked_list_from_array([1, 9, 15, 27, 33, 40])

    print(f"Big List 1: {linked_list_to_array(big_list1)}")
    print(f"Big List 2: {linked_list_to_array(big_list2)}")

    merged_big = merge_sorted(big_list1, big_list2)
    print(f"Merged Big List: {linked_list_to_array(merged_big)}")
    print()

# Usage
if __name__ == "__main__":
    main()
