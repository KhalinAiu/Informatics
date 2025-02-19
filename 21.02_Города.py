cities = input().lower().split()
connection = dict()
for i in range(len(cities)):
    a = list(cities[i][-1])
    a.append(cities[i])
    connection[cities[i][0]] = tuple(a)

let_count = dict()
for i in range(len(cities)):
    if cities[i][0] not in let_count.keys():
        let_count[cities[i][0]] = 1
    else:
        let_count[cities[i][0]] += 1
    if cities[i][-1] not in let_count.keys():
        let_count[cities[i][-1]] = -1
    else:
        let_count[cities[i][-1]] -= 1

start = None
for key in let_count.keys():
    if let_count[key] == 1:
        if start == None:
            start = key
        else:
            start = 0
            break
if start != 0 and start != None:
    n = 0 
    while n < 1000:
        n += 1
        if connection[start][0] in connection.keys() and connection[start][1] in cities:
            cities.remove(connection[start][1])
            start = connection[start][0]
        else:
            cities.remove(connection[start][1])
            break

    if len(cities) == 0:
        print('Yes')
    else:
        print('No')

else:
    print('No')