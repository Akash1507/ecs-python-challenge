class Course(object):
    """
    Representation of Course in form of class.
    """

    def __init__(
        self,
        id=None,
        title=None,
        description="",
        price=0.00,
        discount_price=0.00,
        image_path="",
        on_discount=False,
        date_created=None,
        date_updated=None,
    ):
        """
        Constructor
        """
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.discount_price = discount_price
        self.image_path = image_path
        self.on_discount = on_discount
        self.date_created = date_created
        self.date_updated = date_updated

    def to_dict(self):
        """
        Utility Method of Course class to convert object to dict.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "discount_price": self.discount_price,
            "image_path": self.image_path,
            "on_discount": self.on_discount,
            "date_created": self.date_created,
            "date_updated": self.date_updated,
        }
