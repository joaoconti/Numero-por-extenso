from numeros import um_digito, dois_digitos, tres_digitos


def numeros_extensos(numero_indice, tabela, indice):
    resultado = ''
    for k, v in tabela.items():
        k = str(k)

        if numero_indice == k[indice]:
            resultado = v
            return resultado

while True:
    try:
        resultado = []
        numero = input('Digite um número: ')
        qtd_caracteres = len(numero)

        if not numero.isnumeric():
            print('Digite apenas números inteiros.')
            continue

        if qtd_caracteres < 2:
            callbeck_um_digito = numeros_extensos(numero[0], um_digito, 0)
            print(callbeck_um_digito)

        if qtd_caracteres > 2:
            callbeck_tres_digitos = numeros_extensos(numero[0], tres_digitos, 0)
            resultado.append(callbeck_tres_digitos)

            if numero[1] == '0' and numero[2] == '0':
                print(''.join(resultado))
                continue

            resultado.append('e')
            callbeck_dois_digitos = numeros_extensos(numero[1], dois_digitos, 0)
            resultado.append(callbeck_dois_digitos)

            callbeck_um_digito = numeros_extensos(numero[2], um_digito, 0)
            resultado.append(callbeck_um_digito)

            print(' '.join(resultado))

    except ValueError:
        print('Digite apenas números inteiros.')