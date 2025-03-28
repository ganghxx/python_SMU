def get_fixed_price(sale_price, sale_rate):
    return int(sale_price*(100/(100-sale_rate)))
    
rate = int(input('할인율은? '))
A_sale_price = int(input("A 상품의 할인된 가격은? "))
B_sale_price = int(input("B 상품의 할인된 가격은? "))

A_fixed_price = get_fixed_price(A_sale_price, rate)
B_fixed_price = get_fixed_price(B_sale_price, rate)

print(f"A 상품의 정가는 {A_fixed_price} 원")
print(f"B 상품의 정가는 {B_fixed_price} 원")