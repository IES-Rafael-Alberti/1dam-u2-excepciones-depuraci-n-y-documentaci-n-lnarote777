
def ordenarLista():
    a = [8, 3, 1, 19, 14]
    total =len(a)
    for i in range(0, len(a)):
        for j in range(0, total - 1):
            if a[j] > a[j+1]:
                a[j] , a[j+1] = a[j+1] , a[j]
    			
         
    
    
def main():
	print(ordenarLista())


if __name__ == "__main__":
    main()