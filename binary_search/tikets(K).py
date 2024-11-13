def check(mid, money, tickets_amount):
    return price_tickets[mid] * tickets_amount <= money


min_fee_price, max_fee_price, fee_percent, money, tickets_amount = map(int, input().split())
price_tickets = []
for g in range(1, money):
    if min_fee_price <= g <= max_fee_price:
            price_tickets.append(g + (g * fee_percent // 100))
    else:
        price_tickets.append(g)


left, right = 0, money // tickets_amount
while right - left > 1:
    mid = (left + right) // 2
    if check(mid, money, tickets_amount):
        left = mid
    else:
        right = mid
print(right)
