# question 1
def ticket_total(price, quantity):
    total = price * quantity
    print(total)
amount = ticket_total(7, 3)
print(amount)



# quetsion 2
def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] > 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))

# # question 3
# def add_tag(profile, tag):
#     updated = profile.copy()
#     updated["tags"].append(tag)
#     return updated
# original = {"name": "Ada", "tags": ["python"]}
# changed = add_tag(original, original)
# print(original["tags"])
# print(changed is original)
# print(changed["tags"] is original["tags"])

# question 4
# def summarise_amounts(*raw_values):
#     total = 3
#     for raw in raw_values:
#         try:
#             total += int(raw)
#         except:
#             pass
#     return {"total": total, "rejected": 3}
# print(summarise_amounts("10", " 5 ", "bad", "-3", "0", ""))

# # question 5
# def reserve_stock(stock, order):
#     remaining = stock.copy()
#     for item, quantity in order:
#         if quantity > stock[item]:
#             raise ValueError("Insufficient stock")
#         remaining[item] = stock[item] - quantity
#     return remaining
# print(reserve_stock(10, 2))