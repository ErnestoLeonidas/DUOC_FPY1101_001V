array = [-4,-2,0,1,3]
        # 0   1  2  3  4
array2 = [16, 4, 0, 1, 9]

# for n in range(1, 10):
#     print(n)


# for f in range(1, len(array2)+1):
#     print(f)


num=[1,123,123,290,22,41,52,6,2131,213,9,99999999]
ordenada=[]

for i in num:
  contador=0
  for j in ordenada:
    # print(j)
    if i > j:
      contador +=1
    # print(contador,i)
    # print(contador)
  # print("insertamos posicion=",contador,"valor",i)
  ordenada.insert(contador,i)
  
print(ordenada)