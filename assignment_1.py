products = [
    {'name': 'Wireless Headphones', 'price': 89.99, 'category': 'Electronics', 'stock': 45},
    {'name': 'Running Shoes', 'price': 79.99, 'category': 'Sports', 'stock': 23},
    {'name': 'Bluetooth Speaker', 'price': 59.99, 'category': 'Electronics', 'stock': 67},
    {'name': 'Yoga Mat', 'price': 24.99, 'category': 'Sports', 'stock': 8}
]

#======================== Task 1

by_price = sorted(products, key=lambda product: product['price'], reverse=True)

# TODO: Sort products by category, then by name alphabetically (Primary Sort, Secondary Sort)
by_category_name = sorted(products, key=lambda item: (item['category'], item['name']) )

# Test your sorting
print("Most expensive:", by_price[0]['name'])
print("First alphabetically:", by_category_name[0]['name'])

#======================TASK 2

# TODO: Create a lambda to determine price category
# - Price >= 100: 'Premium'
# - Price <= 50: 'Budget'  
# - Otherwise: 'Standard'
price_category = lambda price: 'Premium' if price >= 100 else 'Budget' if price <= 50 else 'Standard'

# TODO: Create a lambda to check stock status
# - Stock <= 10: 'Low Stock'
# - Otherwise: 'In Stock'
stock_status = lambda stock: 'Low Stock' if stock <= 10 else 'In Stock'

# Test your lambdas
print("Product Status Report:")
for product in products:
    category = price_category(product['price'])
    status = stock_status(product['stock'])
    print(f"{product['name']}: {category}, {status}")
