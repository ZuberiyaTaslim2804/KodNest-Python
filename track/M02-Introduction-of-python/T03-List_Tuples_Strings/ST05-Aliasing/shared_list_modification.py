original_scores=[]

for _ in range(3):
    original_scores.append(int(input()))

# Aliasing the list
alias_scores=original_scores

replacement_score=int(input())
additional_score=int(input())

# Modify the shared list through alias_scores
alias_scores[0]=replacement_score
alias_scores.append(additional_score)

print("Original: ",original_scores)
print("Alias:",alias_scores)
print("Shared Object:",original_scores is alias_scores)