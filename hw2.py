def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(money):
    coin = [500, 100, 50, 10]
    for i in coin:
        coin_count = money // i
        money %= i
        print(f"{i}원 동전의 개수: {coin_count}")

exchange(get_integer("동전으로 교환하고자 하는 금액은? "))