# 2822

score = []

for _ in range(8):
    score.append(int(input()))
    
print(sum(sorted(score, reverse=True)[:5]))
score_kind = [score.index(i) + 1 for i in sorted(score, reverse=True)[:5]]
print(" ".join(map(str, sorted(score_kind))))