salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for months in range(1, months+1):
    need_money = need_money + spend - salary
    months +=1
    spend = spend + spend*increase

print(round(need_money))
