MELON_COST = 1.00


def print_customer_payment_report(customer_filename, separator='|',
                                  melon_cost=MELON_COST):
    """Print line for each customer who over or underpaid"""

    customer_file = open(customer_filename)
    for line in customer_file:
        line = line.strip()
        words = line.split(separator)

        # customer_number = words[0]  [unused]
        customer_name = words[1]
        customer_melons = int(words[2])
        customer_paid = float(words[3])

        expected_payment = customer_melons * melon_cost
        if customer_paid != expected_payment:
            print customer_name, "paid {:.2f}, expected {:.2f}".format(
                customer_paid, expected_payment)

    customer_file.close()

print_customer_payment_report("customer-orders.txt")
