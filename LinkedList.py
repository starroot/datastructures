class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = ""
        # first value and arrow
        string = string + str(self.value) + "--> "

        # values up to null
        curr = self.next
        while not curr is None:
            string = string + str(curr.value) + "--> "
            curr = curr.next
        string = string + "None"
        return string
        



l = LinkedList(2)
print(l)
