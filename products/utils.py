class GetPostCustomMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)