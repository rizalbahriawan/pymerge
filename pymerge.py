def merge(lst):
    if len(lst) > 1:
        #mencari nilai tengah list
        mid = len(lst)//2
        #membagi list jadi 2 bagian 
        l = lst[0:mid]
        r = lst[mid:len(lst)]

        
        merge(l) #sort tengah pertama
        
        merge(r) #sort tengah kedua
        

        i = j = k = 0

        #menggabungkan data ke list setelah di-sort
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k] = l[i]
                i+=1
            else:
                lst[k] = r[j]
                j+=1
            k+=1
           
        
        #menggabungkan data yang masih tersisa
        while i < len(l):
            lst[k] = l[i]
            i+=1
            k+=1 

        while j < len(r):
            lst[k] = r[j]
            j+=1
            k+=1 

if __name__ == "__main__":
    f = open("input.txt", "r") 
    inp = f.readlines()[0].strip()
    lst=[]
    for x in inp.split(","):
        lst.append(int(x))
    print("unsorted: " + str(lst))
    merge(lst)
    print("sorted: " + str(lst))    
