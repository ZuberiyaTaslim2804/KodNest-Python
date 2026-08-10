def display_invoice_total(price,quantity):
    total=price*quantity
    return total
    pass
price=int(input())
quantity=int(input())

res=display_invoice_total(price,quantity)
print(f"Total: {res}")