items=["pencil", "pen", "eraser", "marker", "ruler", "compass"]
stocks_counts=[12, 0, 8, 5, 3]

inventory={item: count for item, count in zip(items, stocks_counts)}
print("full inventory is:", inventory)


in_stock_items={item: count for item, count in zip(items, stocks_counts) if count>0}
print("Items in stock:", in_stock_items)
