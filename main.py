
# Conceito de variável

x = [1,2,3]
y = x
x.append(4)

print(y)
# o valor de x retorna com atualização da variável anterior.
print(x)

# As conversões de tipos de dados p/ int sem round são tratadas como inteiras.
e = float(int(3.9))
print(e)
f = float(3.9)
print(f)
# valores decimais <5 são arredondas para baixo e >5 pra cima.
h = round(3.9)
print(h)

# ao inveis de null usar None 

a = 'Isso é uma String com aspas Simples'
b = "Isso é uma String com aspas Duplas"
c = """Isso é Uma String com aspas Triplas"""
print(a + "\n" + b + "\n" + c)

#coding: utf-8
meu_nome = "Sintaxes Python"
meu_nick = 'Devmedia'
print ("Nome: %s, Nick: %s" % (meu_nome.upper(), meu_nick))
print ("Meu nome comeca com a letra ", meu_nome[0])
print ("Meu nome comeca com a letra ", meu_nome[0].lower())
print ("Meu primeiro nome é ", meu_nome[1:7])
