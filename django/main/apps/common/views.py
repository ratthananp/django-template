class ActionRelatedSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Flow:  (`-->` = `fallback`)
    CREATE: `create_serializer_class` --> `write_serializer_class`
    UPDATE: `update_serializer_class` --> `write_serializer_class`
    LIST: `list_serializer_class`
    RETRIEVE: `retrieve_serializer_class` --> `list_serializer_class`

    ref: https://www.revsys.com/tidbits/using-different-read-and-write-serializers-django-rest-framework/
    """

    list_serializer_class = None
    retrieve_serializer_class = None

    write_serializer_class = None
    create_serializer_class = None
    update_serializer_class = None

    def get_serializer_class(self):
        if self.action in ['create']:
            return self.get_create_serializer_class()
        if self.action in ['update', 'partial_update']:
            return self.get_update_serializer_class()
        if self.action in ['retrieve']:
            return self.get_retrieve_serializer_class()
        return self.get_list_serializer_class()

    def get_list_serializer_class(self):
        assert self.list_serializer_class is not None, (
                "'%s' should either include a `list_serializer_class` attribute,"
                "or override the `get_list_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.list_serializer_class

    def get_retrieve_serializer_class(self):
        return self.retrieve_serializer_class or self.get_list_serializer_class()

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
                "'%s' should either include a `write_serializer_class` attribute,"
                "or override the `get_write_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.write_serializer_class

    def get_create_serializer_class(self):
        return self.create_serializer_class or self.get_write_serializer_class()

    def get_update_serializer_class(self):
        return self.update_serializer_class or self.get_write_serializer_class()
