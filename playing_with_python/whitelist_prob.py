total_tickets = 1017499
your_tickets = 119
total_prizes = 1500

win_prob = 0

for i in range(total_prizes):
    win_prob += your_tickets / (total_tickets - i)

print(win_prob)