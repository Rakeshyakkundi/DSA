from typing import List
class Boat_life:
    def cal(people,limit):
        people.sort(reverse=True)
        # print(people)
        start = 0
        end = len(people)-1
        no_of_boat = 0
        while start<=end:
            if start == end:
                no_of_boat +=1
                break
            if people[start]+people[end]<=limit:
                start +=1
                end -=1
                no_of_boat +=1
            elif people[start]<=limit:
                start +=1
                no_of_boat +=1
            else:
                end -=1
                no_of_boat +=1
        return no_of_boat
    
cal = Boat_life
boat_max_weight_handel = 80
people_weight = [50,40,60,50,40,30,10]
print("No of boats required are :",cal.cal(people_weight,boat_max_weight_handel))

                