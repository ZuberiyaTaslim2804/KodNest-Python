n=int(input())
scores=[]

for i in range(n):
    scores.append(int(input()))

search_score=int(input())

print("Hihest SCores:",max(scores))
print("Lowest Scores:",min(scores))
print("Total Score:",sum(scores))

if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")
