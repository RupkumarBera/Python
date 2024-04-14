questions=[
    ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
      ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
      ["which is the sky color ?","Green","white","Blue",
     "Black","None",4],
    ["which is the sky color ?","Green","white","Blue",
     "Black","None",4] ,
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4] ,
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4] ,
     ["which is the sky color ?","Green","white","Blue",
     "Black","None",4]
]
levels= [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1280000,2560000,
        5120000,1000000]
money=0
for i in range (0,len(questions)):
    question=questions[i]
    print(questions[i])
    print(f"question for Rs. {levels[i]}")
    print(f"a. {question[1]}       b.{question[2]}")
    print(f"c. {question[3]}       d.{question[4]}")
    reply=int(input("Enter the answer(1-4) or 0 to quit:\n"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("wrong answer:")
        break
print(f"Take  of home  money is {money}")