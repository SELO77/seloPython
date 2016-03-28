roomCount = 1
totalPaxCount = 2

def distributePaxForRoom(roomCount, totalPaxCount):
  # 방배정 리스트 초기화
  resultList = []

  cnt = 0
  while(cnt < roomCount):
    print("==")
    resultList.append(0)
    cnt += 1

  distributionCnt = 0
  roomNumCnt = 0

  while(distributionCnt < totalPaxCount):

    # 방 갯수만큼 1만큼 인원 분배
    if roomNumCnt >= roomCount:
      roomNumCnt = 0

    paxCount = resultList[roomNumCnt]
    paxCount += 1
    resultList[roomNumCnt] = paxCount

    roomNumCnt += 1
    distributionCnt += 1

  return resultList

data = distributePaxForRoom(roomCount, totalPaxCount)
print(data)