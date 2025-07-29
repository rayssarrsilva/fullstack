import pdb

for i in range(3):
    print("Iteração:", i)
    if i == 1:
        pdb.set_trace()


"""
i → mostra 1

n → executa a linha e vai pra próxima

c → continua até o final

"""