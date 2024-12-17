def get_passcode(n):
    passdict = {}
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
                     10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
                     14: 1611325212343114105968, 15: 1214114232133124115106978,
                     16: 1317115262143531341251161079, 17: 11621531441351261171089,
                     18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
                     20: 13141911923282183731746416515614713812911})
    passcode = passdict.get(n)
    return passcode

n = int(input('введите шиифр: '))
print('Шифр: ', n)

pairnum1 = list(range(1, n))
pairnum2 = list(range(1, n))
pairs = []
result = ''

for i in pairnum1:
    for j in pairnum2:
        pn1 , pn2 = i , j
        if pn1 >= pn2:
            continue
        else:
            kratno = n % (pn1 + pn2)
            if kratno == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел:', *pairs)
print('Пароль:', result)
if int(result) == get_passcode(n):
    print('Путь свободен!')





