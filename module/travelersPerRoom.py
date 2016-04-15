numOfAdult = int(input("Input numOfAdult: "))
numOfChild = int(input("Input numOfChild: "))
numOfRooms = int(input("Input numOfRooms: "))
numOfPeople = numOfAdult + numOfChild

def distributeToRoom(numOfPeople, numOfRooms):

  if numOfPeople < numOfRooms:
    return print("\033[95m[Input Error]: numOfPeople < numOfRooms\033[0m")

  # 요청받은 갯수만큼 방 생성
  convertingResult = [0] * numOfRooms

  countInsertingOnePersonToOneRoom = 0
  listIndex = 0

  while(countInsertingOnePersonToOneRoom != numOfPeople):

    convertingResult[listIndex%numOfRooms] += 1
    listIndex += 1
    countInsertingOnePersonToOneRoom += 1

  return convertingResult



def distributeTravelersInTheRoom(numOfAdult, numOfChild, numOfRooms):

  travelersPerRoomList = []
  for i in range(0, numOfRooms):
    travelersPerRoomList.append({'adultCount': 0,'childCount': 0})

  countOfInsertPeople = 0
  numOfPeople = numOfAdult + numOfChild
  listIndex = 0

  while(countOfInsertPeople < numOfPeople):
    travelersPerRoomList[listIndex%numOfRooms]['adultCount'] += 1
    countOfInsertPeople += 1
    listIndex += 1

  for listIndex in range(0, numOfChild):
    travelersPerRoomList[listIndex%numOfRooms]['adultCount'] -= 1
    travelersPerRoomList[listIndex%numOfRooms]['childCount'] += 1

  return travelersPerRoomList




def test(numOfAdult, numOfChild, numOfRooms):

  numOfPeople = numOfAdult + numOfChild
  if numOfPeople < numOfRooms:
    return print("\033[95m[Input Error]: numOfPeople < numOfRooms\033[0m")

  # 요청받은 갯수만큼 방 생성
  convertingResult = [0] * numOfRooms

  countInsertingOnePersonToOneRoom = 0
  listIndex = 0

  while(countInsertingOnePersonToOneRoom != numOfPeople):

    convertingResult[listIndex%numOfRooms] += 1
    listIndex += 1
    countInsertingOnePersonToOneRoom += 1

  return convertingResult



# result = distributeToRoom(numOfPeople, numOfRooms)
# print("\033[93m convertToBedType(int(numOfPeople), int(numOfRooms)):\n%s\033[0m"%result)

result = distributeTravelersInTheRoom(numOfAdult, numOfChild, numOfRooms)
print("\033[94m convertToBedType(int(numOfPeople), int(numOfRooms)):\n%s\033[0m"%result)

# result = test(numOfAdult, numOfChild, numOfRooms)
# print("\033[93m convertToBedType(int(numOfPeople), int(numOfRooms)):\n%s\033[0m"%result)