from .function import refreshData
from utils.baseclass import BaseAPIView


class Request(BaseAPIView):
    def get(self, request):
        refreshData(request)
        return self.success('sucess')