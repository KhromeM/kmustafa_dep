
newArr = [rates[i]*strategy[i] for i in range(len(rates))]
profit = sum(newArr)
left = 0
s, s2 = sum(newArr[:k]) sum(newArr[:k//2])
maxVal = s2 - s
for right in range(k,len(rates)):
    s -= newArr[right-k] + newArr[right]
    s2 -= newArr[right-k//2] + newArr[right]
    maxVal = max(maxVal,s2-s)
return maxVal #???
