phone_num = ''.join(input().split())
try:
    assert phone_num[0] == '+'
    assert phone_num[1] == '7'
except AssertionError:
    if not phone_num.startswith('8'):
        print('неверный формат')
        exit(0)
try:
    assert phone_num.count('--') == 0
    assert not phone_num.startswith('-')
    assert phone_num[-1] != '-'
    assert phone_num.count('(') == phone_num.count(')') == 1 or phone_num.count('(') == phone_num.count(')') == 0
except AssertionError:
    print('неверный формат')
    exit(0)
phone_num = phone_num.replace('(', '')
phone_num = phone_num.replace(')', '')
phone_num = phone_num.replace('-', '')
if phone_num.startswith('8'):
    phone_num = '+7' + phone_num[1:]
operator = phone_num[2:5]
mts = ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919',
       '980', '981', '982', '983', '984', '985', '986', '987', '988', '989']
megafon = ['920', '921', '922', '923', '924', '925', '926', '927', '928',
           '929', '930', '931', '932', '933', '934', '935', '936', '937',
           '938', '939']
beeline = ['902', '903', '904', '905', '906', '960', '961', '962', '963',
           '964', '965', '966', '967', '968', '969']
allop = mts + megafon + beeline
try:
    assert len(phone_num) == 12
except AssertionError: 
    print('неверное количество цифр')
    exit(0)
try:
    assert operator in allop
except AssertionError:
    print('не определяется оператор сотовой связи')
    exit(0)
print('Результат:',phone_num) 
