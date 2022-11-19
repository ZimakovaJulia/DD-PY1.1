from random import choices

def get_random_password(n = 8) -> str:
    password = []
    password.append(choices(string.ascii_uppercase, k=1))
    password.append(choices(string.ascii_lowercase, k=1))
    password.append(choices(string.digits, k=1))
    simb = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password.append(choices(simb, k=(n - 3)))
    return password
#  Почему так: 1) обычно в пароле требуют от 1 знака из каждого пункта 2) sample из-за отсутствия повторов дает меньшую вариативность

print(get_random_password())
