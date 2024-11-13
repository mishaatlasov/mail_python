n = int(input())

participants = []
for _ in range(n):
    id_num, score = map(int, input().split())
    participants.append((id_num, score))

sorted_participants = sorted(participants, key=lambda x: (-x[1], x[0]))


for id_num, score in sorted_participants:
    print(id_num, score)