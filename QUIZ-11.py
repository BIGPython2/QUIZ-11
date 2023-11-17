class Beverage:
    menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def __init__(self, name, quantity):
        self.name = name
        self.price = self.menu.get(name)
        self.quantity = quantity

    def calculate(self):
        total_price = self.price * self.quantity
        print(f"주문 내역: {self.name} {self.quantity}잔, 총 가격: {total_price}원")

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

selected_beverage = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")
if selected_beverage == "커피":
    quantity = int(input(f"주문할 {selected_beverage}의 수량을 입력하세요: "))
    Coffee.quantity = quantity
    Coffee.calculate()
elif selected_beverage == "녹차":
    quantity = int(input(f"주문할 {selected_beverage}의 수량을 입력하세요: "))
    GreenTea.quantity = quantity
    GreenTea.calculate()
elif selected_beverage == "아이스티":
    quantity = int(input(f"주문할 {selected_beverage}의 수량을 입력하세요: "))
    IceTea.quantity = quantity
    IceTea.calculate()
else:
    print("잘못된 음료를 선택하셨습니다.")
