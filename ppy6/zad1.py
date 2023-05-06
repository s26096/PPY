class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, e, func=None):
        new_element = Element(e)
        current_element = self.head
        if current_element is None:
            self.head = new_element
            self.tail = new_element
            self.size += 1
            return
        if func is None:
            func = lambda x, y: x >= y
        old_element = None
        while current_element.nextE is not None and func(current_element.data, e) is False:
            old_element = current_element
            current_element = current_element.nextE
        if current_element is None:
            self.tail = new_element
        if old_element is None:
            self.head = new_element
        else:
            old_element.nextE = new_element
        new_element.nextE = current_element
        self.size += 1
        return

    def get(self, e):
        current_element = self.head
        while current_element:
            if current_element.data == e:
                return current_element
            current_element = current_element.nextE
        return None

    def delete(self, e):
        current_element = self.head
        if current_element is None:
            return
        if current_element.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return
        while current_element.nextE is not None:
            if current_element.nextE.data == e:
                current_element.nextE = current_element.nextE.nextE
                self.size -= 1
                if current_element.nextE is None:
                    self.tail = current_element
                return
            current_element = current_element.nextE

    def __str__(self):
        data = []
        curr = self.head
        while curr:
            data.append(str(curr.data))
            curr = curr.nextE
        return " , ".join(data)

    def __repr__(self):
        return self.__str__()
