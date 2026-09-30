#1).'''
data=[10,20,[30,40,50],60]
print(type(data))
print(data[2][1])

#2).
data = [[10, 20], [30, 40], [50, 60]]
print(data[2][0])

#3).
data = (10, 20, (30, 40, 50), 60)
# l1=(list(data))
# print(l1)
print(data[2][0])

#4).
data = {"a": 10, "b": 20, "c": 30}
print(data["b"])

#5).
data = {"numbers": [10, 20, 30, 40]}
print(data["numbers"][2])

#6).
data = [(10, 20), (30, 40), (50, 60)]
print(data[1][1])

#7).
data = ([10, 20], [30, 40], [50, 60])
print(data[2][1])

#8).
data = {"student": {"marks": 85, "age": 20}}
print(data["student"]["marks"])

#9)
data = [{"a": 10}, {"b": 20}, {"c": 30}]
print(data[1]["b"])

#10).
data = [10, 20, [30, 40, 50]]
print(data[2][2])

#11).
data = [[10, 20], [30, [40, 50, 60]], [70, 80]]
print(data[1][1][1])

#12)
data = {"numbers": [10, 20, 30, 40, 50], "other": [60, 70]}
print(data["numbers"][3])

#13).
data = {"values": (10, 20, 30, 40, 50)}
print(data["values"][2])

#14).
data = [{"numbers": [10, 20, 30]}, {"numbers": [40, 50, 60]}]
print(data[1]["numbers"][1])

#15).
data = ([10, 20], {"numbers": [30, 40, 50]}, [60, 70])
print(data[1]["numbers"][1])

#16).
data = {"student": {"marks": [70, 80, 90, 100]}}
print(data["student"]["marks"][2])

#17).
data = [(10, 20, [30, 40], ), (50, 60, [70, 80])]
print(data[1][2][1])

#18).
data = {"A": [10, 20, (30, 40)], "B": [50, 60, (70, 80)]}
print(data["B"][2][0])

#19).
data = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(data[2][1])

#20).
data = {"numbers": ([10, 20], [30, 40], [50, 60])}
print(data["numbers"][2][1])

#21).
data = [10, [20, 30, [40, 50, [60,70]]], 80]
print(data[1][2][2][1])

#22).
data = {"company": { "employees": {"developer": {"salary": [50000, 60000, 70000]}}}}
print(data["company"]["employees"]["developer"]["salary"][1])

#23).
data = {"employee": ("Rahul", [100, 200, 300]) } 
print(data["employee"][1][1])

#24).
data = {"students": [{"marks": [70, 80, 90]}, {"marks": [60, 75, 85]}, {"marks": [50, 65, 95]}]}
print(data["students"][2]["marks"][2])

#25).
data=([10, 20], {"numbers": ([30, 40], [50, 60, [70, 80]])})
print(data[1]["numbers"][1][2][1])

#26).
data = {"data":[{"values": (10, 20, [30, 40, 50])}, {"values": (60, 70, [80, 90, 100])}]}
print(data["data"][1]["values"][2][1])

#27).
data = [[10, 20, 30], [40, [50, 60, 70]], [80, 90, [100, 110, 120]]]
print(data[2][2][1])

#28).
data = {"A": [(10, 20)], "B": [30, (40, 50, [60, 70, 80])]}
print(data["B"][1][2][1])

#29).
data= {"employees": [{"name": "Amit", "details": { "scores": (80, 85, 90)}}]}
print(data["employees"][0]["details"]["scores"][1])

#30).
data = [{"department": "IT","employees": [{"name": "A","data": (10, [20, 30, {"marks": [40, 50, 60]}])},{"name": "B","details": {"scores": (75, 88, 95)
        },"data": (70, [80, 90, {"marks": [100, 110, 120]}])}]}]

print(data[0]["employees"][1]["data"][1][2]["marks"][1])



import numpy as np 

arr=np.array([10,20,30,40,50])
print(arr.ndim)
print(arr)