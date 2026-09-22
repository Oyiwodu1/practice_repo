# def tickect_total(price, quantity):
#     total = price * quantity
#     print(total)
# amount = tickect_total("7", 3)
# print(amount)

# def passing_scores(scores):
#     passed = []
#     for index in range(len(scores) - 1):
#         if scores[index] > 50:
#             passed.append(scores[index])
#     return passed
# print(passing_scores([49, 50, 80, 65]))

# def add_tag(profile, tag):
#     updated = profile.copy()
#     updated["tags"].append(tag)
#     return updated
# original = {"name": "Ada", "tags": ["python"]}
# add_tag(original, "testing")
# print(original["tags"])
# print( original)
# print(["tags"] is original["tags"])

# def summarise_amounts(raw_values):
#     total = 0
#     for raw in raw_values:
#         try:
#             total += int(raw)
#         except:
#             pass
#     return {"total": total, "rejected": 0}


# def reserve_stock(stock, order):
#     remaining = stock.copy()
#     for item, quantity in order:
#         if quantity > stock[item]:
#             raise ValueError("Insufficient stock")
#         remaining[item] = stock[item] - quantity
#     return remaining

# def passing_scores(scores):
#     passed = []
#     for index in range(len(scores) - 1):
#         if scores[index] > 50:
#             passed.append(scores[index])
#     return passed
# print(passing_scores([49, 50, 80, 65]))

# def add_tag(profile, tag):
#     updated = profile.copy()
#     updated["tags"].append(tag)
#     return updated
# original = {"name": "Ada", "tags": ["python"]}
# add_tag(original, "testing")
# print(original["tags"])
# print( original)
# print(["tags"] is original["tags"])