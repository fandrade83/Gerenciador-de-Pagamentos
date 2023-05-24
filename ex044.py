print('{:=^30}'.format(' FANDRADE STORE '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcelas = int(input(' Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {:.2f}x de R${:.2f} COM JUROS'.format(totalparcelas, parcela))
else:
    total = preço
    print('OPÇÃO \033[0;31mINVALIDA DE PAGTO. TENTE NOVAMENTE!\033[m')
print(f' Sua compra de R$: {preço} vai custar R${total} no final')
