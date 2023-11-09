
def ordenarLista(a):
    total =len(a)
    cont = 0
    for i in range(0, len(a)):
        for j in range(0, total - 1):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] , a[j]
                cont +=1
        total -=1
    return a		
         
    
    
def main():
	a = [8, 3, 1, 19, 14]
	print(ordenarLista(a))


if __name__ == "__main__":
    main()