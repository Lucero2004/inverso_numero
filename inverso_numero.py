# programa para determinar el inverso de un numero N de 3 cifras

print("--------------------------------")
print("-------QUIZ--------")
print("--------------------------------")

# input
n= int(input("digite el valor de x: "))

# procesing

m=n//100
s=n%100
o=s//10
p=s%10
q= m+o*10+p*100

# output
print("-------------------------------")
print("------RESULTADO:------ ")
print("---------------------------------")
print("numero invertido:" +str(q))
