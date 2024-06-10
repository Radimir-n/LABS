try:
    phone_num = input().replace(" ", "").replace("\t", "")
    if "(" in phone_num and ")" in phone_num:
        st_index = phone_num.index("(")
        en_index = phone_num.index(")")
        phone_num = phone_num[:st_index] + phone_num[st_index + 1:en_index] + phone_num[en_index + 1:]
    if "(" in phone_num or ")" in phone_num:
        raise TypeError()
 
    if "--" not in phone_num and "-" in phone_num:
        phone_num = phone_num[0] + phone_num[1:-1].replace("-", "") + phone_num[-1]
    if "-" in phone_num:
        raise TypeError()
 
    if phone_num.startswith("+7"):
        phone_num = "+7" + phone_num[2:]
    elif phone_num.startswith("8"):
        phone_num = "+7" + phone_num[1:]
 
    if len(phone_num.replace("+", "")) != 11 or not phone_num[1:].isdigit():
        raise ValueError()
    print(phone_num)
except ValueError:
    print("error")
except TypeError:
    print("error")
