print()
print("----------- stack operations--------------")
print()
print("______ task1_____________")
stack=['step1','step2','step3']
print()
print("the element in stack before popping two element:",stack)
print()
stack.pop()
stack.pop()
print("after popping two steps the remaining step is:",stack)
print()
print("______ task2_____________")
print()
stack=['topic A','topic B','topic C']
print("the element in stack before popping one topic:",stack)
stack.pop()
print()
print("the remaining topic after popping one topic is :",stack)
print()
print("_______queue operations_______________")
print()
print("--------- task1 -----------")
print()
queue=list(range(1,10))
print("initial queue :",queue)
served_clients=5
remaining_queue =queue[served_clients:]
print("the remaining queue:",remaining_queue)

front_client = remaining_queue[0]
print("the client at the front:",front_client )
print()
print("----------task2-------------")
print()
buses=list(range(1,9))
print("queue",buses)
first_served = buses[0]
second_served = buses[1]

print("first bus served:",first_served)
print("second bus served:",second_served)
