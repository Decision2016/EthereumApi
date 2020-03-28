from utils.baseclass import BaseAPIView
from .models import BlockInfo


class GetBlockInfo(BaseAPIView):
    def get(self, request):
        num = int(request.GET.get('num'))
        total = BlockInfo.objects.count()
        if num > 30 or num > total:
            return self.error('request too much')
        LatestData = BlockInfo.objects.last()
        maxId = LatestData.BlockId
        resData = []
        for i in range(num - 1, -1, -1):
            resData.append(BlockInfo.objects.filter(BlockId=maxId - i)[0].BlockHash)
        return self.success(resData)
