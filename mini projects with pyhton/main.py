class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Order:
    def __init__(self, order_id, customer, dish, time):
        self.order_id = order_id
        self.customer = customer
        self.dish = dish
        self.time = time
        self.status = "Pending"

class CanteenManager:
    def __init__(self):
        self.orders = []
        self.menu = [
            Dish("Caesar Salad", 6.50, "Starter"),
            Dish("Daily Soup", 4.50, "Starter"),
            Dish("Steak & Fries", 12.00, "Main"),
            Dish("Pasta Carbonara", 10.00, "Main"),
            Dish("Apple Pie", 4.00, "Dessert"),
            Dish("Yogurt", 2.00, "Dessert")
        ]
        self.OPENING_TIME = "11:30"
        self.CLOSING_TIME = "14:00"

    def display_menu(self):
        print("\n=== AVAILABLE DISHES ===")
        for i, dish in enumerate(self.menu, 1):
            print(f"{i}. {dish.name} - €{dish.price} ({dish.category})")

    def add_order(self, customer, dish_number, delivery_time):
        if not (1 <= dish_number <= len(self.menu)):
            return "Invalid dish number"
        if not (self.OPENING_TIME <= delivery_time <= self.CLOSING_TIME):
            return f"Invalid time. Please order between {self.OPENING_TIME} and {self.CLOSING_TIME}"

        order = Order(len(self.orders) + 1, customer, self.menu[dish_number - 1], delivery_time)
        self.orders.append(order)
        return f"Order #{order.order_id} confirmed"

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = new_status
                return "Status updated"
        return "Order not found"

    def get_customer_orders(self, customer):
        customer_orders = [order for order in self.orders if order.customer.lower() == customer.lower()]
        if not customer_orders:
            return "No orders found"
        return customer_orders

    def daily_summary(self):
        if not self.orders:
            return "No orders today"
        
        total_orders = len(self.orders)
        delivered = sum(1 for order in self.orders if order.status == "Delivered")
        total_amount = sum(order.dish.price for order in self.orders)
        
        return {
            "total_orders": total_orders,
            "delivered": delivered,
            "pending": total_orders - delivered,
            "total_amount": total_amount
        }

def main():
    manager = CanteenManager()
    
    while True:
        print("\n=== CANTEEN MANAGEMENT SYSTEM ===")
        print("1. Add new order")
        print("2. Update order status")
        print("3. View customer orders")
        print("4. View daily summary")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            manager.display_menu()
            customer = input("Customer name: ")
            dish_number = int(input("Dish number: "))
            time = input("Delivery time (HH:MM): ")
            print(manager.add_order(customer, dish_number, time))
            
        elif choice == "2":
            order_id = int(input("Order ID: "))
            print("1. Pending\n2. Preparing\n3. Delivered")
            status_choice = input("New status (1-3): ")
            status = ["Pending", "Preparing", "Delivered"][int(status_choice) - 1]
            print(manager.update_order_status(order_id, status))
            
        elif choice == "3":
            customer = input("Customer name: ")
            orders = manager.get_customer_orders(customer)
            if isinstance(orders, list):
                for order in orders:
                    print(f"\nOrder #{order.order_id}")
                    print(f"Dish: {order.dish.name}")
                    print(f"Price: €{order.dish.price}")
                    print(f"Time: {order.time}")
                    print(f"Status: {order.status}")
            else:
                print(orders)
            
        elif choice == "4":
            summary = manager.daily_summary()
            print("\n=== DAILY SUMMARY ===")
            print(f"Total orders: {summary['total_orders']}")
            print(f"Delivered: {summary['delivered']}")
            print(f"Pending: {summary['pending']}")
            print(f"Total amount: €{summary['total_amount']:.2f}")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()



