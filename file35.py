question = [
    ['What is the capital of India', 'Mumabi', 'New Delhi', 'Kolkata', 'Banglore', 'b'],
    ['What is the capital of UP', 'Mumabi', 'New Delhi', 'Kolkata', 'Lucknow', 'd'],
    ['What is the capital of Maharastra', 'Mumabi', 'New Delhi', 'Kolkata', 'Banglore', 'a'],
    ['What is the capital of West Bengaal', 'Mumabi', 'New Delhi', 'Kolkata', 'Banglore', 'c'],
    ['What is the capital of Karnataka', 'Mumabi', 'New Delhi', 'Kolkata', 'Banglore', 'd']    
]
total_score =  0
count = 1
for q in question :
    print(f"{count}. {q[0]}")
    print("a. "+q[1])
    print("b. "+q[2])
    print("c. "+q[3])
    print("d. "+q[4])
    
    ra = q[5]
    ans = input("Please enter answer: ")
    if ra == ans :
        q.append(1)
    else:
        q.append(0)
    q.append(ans)
    count = count + 1

count = 1
for q in question :
     print(f"{count}. {q[0]}")
     print(f"Right Answer: {q[5]} and you entered {q[7]}")
     if q[6] == 1 :
         print("Right Answer")
     else:
         print("Wrong Answer")
         
     total_score = total_score + q[6]
     count = count + 1