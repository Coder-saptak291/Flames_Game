def main():
    n1 = input("Enter the name of the first player:")
    n2 = input("Enter the name of the second player:")

    n1 = n1.lower()
    n2 = n2.lower()

    n1.replace(" ", "")
    n2.replace(" ", "")

    list1 = list(n1)
    list2 = list(n2)
    if len(list1)>len(list2):
        d = list1
        v = list2
    else:
        v = list1
        d = list2
    checking(d,v)

def checking(d,v):
    # Creating a special list  of unmatched characters
    d_un=[]
    v_un=[]
    for i in d:
        if i not in v:
            d_un.append(i)
    for j in v:
        if j not in d:
            v_un.append(j)
    
    d= d_un
    v= v_un
    
    # main working
    z = len(d) + len(v)
    lz = ["f","l","a","m","e","s"]
    while len(lz)>1:
        f = z%len(lz)
        e = lz[(f-1)]
        lz.remove(e)
    finish(lz)


def finish(lz):
    r = lz[0]
    if r=="f":
        print("You two are friends.")
    elif r=="l":
        print("You two love each other.")
    elif r=="a":
        print("You two are attracted towards each other.")
    elif r=="m":
        print("You two are going to be married with each other")
    elif r=="e":
        print("You two are enemies.")
    elif r=="s":
        print("You two are siblings.")


# working 
main()

    
