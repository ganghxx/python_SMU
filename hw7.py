shopping_bag = {}

print('[구입]')

while True:
    item = input('상품명? ')
    if item != '':
        quantity = int(input('수량은? '))
        shopping_bag[item] = quantity
        print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
        print()
    else:
        print()
        break

print('>>>장바구니 보기:', shopping_bag)
print()

print('[검색]')
kword = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{kword}은(는) {shopping_bag[kword]}개 담겨 있습니다.')
