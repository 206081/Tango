class Code:
    class Generic:
        def __init__(self):
            self.not_exist = f"{self.__class__.__name__.lower()}_not_exists"
            self.no_permissions = "no_permissions"
            self.create = f"{__class__.__name__}created"
            self.retrieve = f"{__class__.__name__}retrieve"
            self.list = f"{__class__.__name__}list"
            self.all = f"{__class__.__name__}all"

    class Table(Generic):
        pass

    class List(Generic):
        pass

    class Card(Generic):
        pass

    class Comment(Generic):
        pass

    table = Table()
    list = List()
    card = Card()
    comment = Comment()


class Message:
    class Generic:
        def __init__(self):
            self.not_exist = f"{self.__class__.__name__} does not exists"
            self.no_permissions = "No permission"
            self.create = f"{__class__.__name__} created"
            self.retrieve = f"{__class__.__name__} retrieve"
            self.list = f"{__class__.__name__} list"
            self.all = f"{__class__.__name__} all"

    class Table(Generic):
        pass

    class List(Generic):
        pass

    class Card(Generic):
        pass

    class Comment(Generic):
        pass

    table = Table()
    list = List()
    card = Card()
    comment = Comment()


class Detail:
    class Generic:
        def __init__(self):
            self.not_exist = f"The {self.__class__.__name__.lower()} you trying to reach does not exist"
            self.no_permissions = f"You do not have permissions to reach this {self.__class__.__name__.lower()}"
            self.create = f"{__class__.__name__} has been created successfully"
            self.retrieve = f"{__class__.__name__} has been retrieved successfully"
            self.list = f"{__class__.__name__} has been listed successfully"
            self.all = f"{__class__.__name__} lists with all cards has been listed successfully"

    class Table(Generic):
        pass

    class List(Generic):
        pass

    class Card(Generic):
        pass

    class Comment(Generic):
        pass

    table = Table()
    list = List()
    card = Card()
    comment = Comment()
