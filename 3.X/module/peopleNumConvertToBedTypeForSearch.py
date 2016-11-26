numOfPeople = input("Input numOfPeople: ")
numOfRooms = input("Input numOfRooms: ")

def convertToBedType(numOfPeople, numOfRooms):

  if numOfPeople < numOfRooms:
    return print("\033[95m[Input Error]: numOfPeople < numOfRooms\033[0m")

  # 요청받은 갯수만큼 방 생성
  convertingResult = [0] * numOfRooms
  print("len(convertingResult): %s"%str(len(convertingResult)))

  countInsertingOnePersonToOneRoom = 0
  listIndex = 0

  while(countInsertingOnePersonToOneRoom != numOfPeople):

    convertingResult[listIndex%numOfRooms] += 1
    listIndex += 1
    countInsertingOnePersonToOneRoom += 1

  return convertingResult

def justFnc():
  test_var = "just test"

def convertToHotelpassBedType(roomList):

  searchConditions = []
  searchCondition = {}

  sGLCNT = 0  #Single Bedtype
  dblOrTwin = 0 #Double or Twin Bedtype
  tRPCnt = 0  #Triple

  for each in roomList:
    if each == 1:
      sGLCNT += 1
    elif each == 2:
      dblOrTwin +=1
    elif each == 3:
      tRPCnt +=1
  justFnc()
  if dblOrTwin > 0:
    searchCondition['sGLCnt'] = sGLCNT
    searchCondition['tRPCnt'] = tRPCnt

    # 더블베드 검색 조건 생성
    searchCondition['dBLCnt'] = dblOrTwin
    searchCondition['tWNCnt'] = 0
    searchConditions.append(searchCondition)

    # 트윈베드 검색 조건 생성
    searchCondition = searchCondition.copy()
    searchCondition['dBLCnt'] = 0
    searchCondition['tWNCnt'] = dblOrTwin
    searchConditions.append(searchCondition)

  else:
    searchCondition['sGLCnt'] = sGLCNT
    searchCondition['tRPCnt'] = tRPCnt
    searchConditions.append(searchCondition)

  return searchConditions


result = convertToBedType(int(numOfPeople), int(numOfRooms))
print("\033[93m convertToBedType(int(numOfPeople), int(numOfRooms)):\n%s\033[0m"%result)

result = convertToHotelpassBedType(result)
print("\033[92m convertHotelpassBedType(result):\n%s\033[0m"%result)