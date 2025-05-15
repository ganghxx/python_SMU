def make_shopping_bag():
    shopping_bag = {}
    while True:
        print('[구입]')
        item = input('상품명? ')
        if item != '':
            quantity = int(input('수량은? '))
            shopping_bag[item] = quantity
            print(f'장바구니에 {item} {quantity}개가 담겼습니다.')
            print()
        else:
            print()
            return shopping_bag

def show_shopping_bag(shopping_bag):
    print('>>> 장바구니 보기:', shopping_bag)
    print()

def check_product(shopping_bag):
    print('[검색]')
    kword = input('장바구니에서 확인하고자 하는 상품은? ')
    if kword in shopping_bag:
        print(f'{kword}은(는) {shopping_bag[kword]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {kword}은(는) 없습니다.')


if __name__ == '__main__':
    shopping_bag = make_shopping_bag()
    show_shopping_bag(shopping_bag)
    check_product(shopping_bag)
