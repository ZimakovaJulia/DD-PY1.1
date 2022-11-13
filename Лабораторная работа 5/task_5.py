from random import choices

def get_random_password(n = 8) -> str:
    letters_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num_ = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password = []
    password.append(choices(letters_up, k=1))
    password.append(choices(letters_low, k=1))
    password.append(choices(num_, k=1))
    simb = letters_up + letters_low + num_
    password.append(choices(simb, k=(n - 3)))
    return password
#  Почему так: 1) обычно в пароле требуют от 1 знака из каждого пункта 2) sample из-за отсутствия повторов дает меньшую вариативность

print(get_random_password())
