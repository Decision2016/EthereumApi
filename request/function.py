import time
import requests
from blockGet.models import BlockInfo

def refreshData(request):
    apiKey = request.GET.get('apiKey')
    timeStamp = int(time.time())
    request = requests.get('https://api-cn.etherscan.com/api',
                           {
                               'module': 'block',
                               'action': 'getblocknobytime',
                               'timestamp': timeStamp,
                               'closest': 'before',
                               'apikey': apiKey
                           })
    totalBlock = int(request.json()['result'])
    if BlockInfo.objects.count() == 0:
        request = requests.get('https://api-cn.etherscan.com/api',
                               {
                                   'module': 'proxy',
                                   'action': 'eth_getBlockByNumber',
                                   'tag': hex(totalBlock),
                                   'boolean': 'true',
                                   'apiKey': apiKey
                               })
        jsonData = request.json()
        nowBlock = BlockInfo.objects.create(BlockId=totalBlock, BlockHash=jsonData['result']['hash'],
                                            TimeStamp=int(jsonData['result']['timestamp'], 16))
        nowBlock.save()
        return

    totalNumber = BlockInfo.objects.count()
    latestId = BlockInfo.objects.get(id=totalNumber).BlockId
    for i in range(latestId + 1, totalBlock + 1):
        request = requests.get('https://api-cn.etherscan.com/api',
                               {
                                   'module': 'proxy',
                                   'action': 'eth_getBlockByNumber',
                                   'tag': str(hex(i)),
                                   'boolean': 'true',
                                   'apiKey': apiKey
                               })
        jsonData = request.json()
        if not BlockInfo.objects.filter(BlockId=i).exist:
            nowBlock = BlockInfo.objects.create(BlockId=i, BlockHash=jsonData['result']['hash'],
                                            TimeStamp=int(jsonData['result']['timestamp'], 16))
            nowBlock.save()