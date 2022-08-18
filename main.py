import string
import random

#gerar id aleatorio
def gerar_id():
    qts_ids = 1
    comprimento_do_id = 6
    for x in range(qts_ids):
        print(''.join(random.choice(string.ascii_letters + string.digits)
              for _ in range(comprimento_do_id)))


gerar_id()


#gerar id apartir do que o user quer
def user_id_gen_by_user():
    qts_id = int(input("Quantidade de ids que vc gostaria de gerar: "))
    comprimento_id = int(input("comprimento dos ids: "))
    for x in range(qts_id):
        print(''.join(random.choice(string.ascii_letters + string.digits)
              for _ in range(comprimento_id)))

user_id_gen_by_user()
