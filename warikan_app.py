amount = int(input("合計いくら: "))
number_of_people = int(input("合計何人: "))

payment = amount // number_of_people
remainder = amount % number_of_people

print(f"1人 : {payment}円, 端数 :{remainder}円")
