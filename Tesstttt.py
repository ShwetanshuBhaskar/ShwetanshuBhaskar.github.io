shape=input("Type A Basic Shape Name :")
if shape=="square":
    sqh=int(input("Enter The Breadth :"))
    sqb=int(input("Enter The Height :"))
    print(2*(sqh+sqb),"Is The Perimetere")
elif shape=="rectangle":
    sqh=int(input("Enter The Breadth :"))
    sqb=int(input("Enter The Height :"))
    print(2*(sqh+sqb),"Is The Perimetere")
elif shape=="rhombus":
    sqh=int(input("Enter The Breadth :"))
    sqb=int(input("Enter The Height :"))
    print(2*(sqh+sqb),"Is The Perimetere")
elif shape=='circle':
    r=int(input("Type The Radius :"))
    print(2*22/7*r,"Is The Circumfrence")
elif shape=='triangle':
    t1=int(input("Enter The Altitude :"))
    t2=int(input("Enter The Base :"))
    t3=int(input("Enter The Hypotenuse :"))
    print(t1+t2+t3,"Is The Perimetere")
elif shape=='oval':
    print("Cant Solve Here!")
elif shape=='hexagon':
    h1=int(input("Enter The First Side :"))
    h2=int(input("Enter The Second Side :"))
    h3=int(input("Enter The Third Side :"))
    h4=int(input("Enter The Fourth Side :"))
    h5=int(input("Enter The Fifth Side :"))
    h6=int(input("Enter The Sixth Side :"))
    print(h1+h2+h3+h4+h5+h6,"Is The Perimetere")
elif shape=='pentagon':
    p1=int(input("Enter The First Side :"))
    p2=int(input("Enter The Second Side :"))
    p3=int(input("Enter The Third Side :"))
    p4=int(input("Enter The Fourth Side :"))
    p5=int(input("Enter The Fifth Side :"))
    print(p1+p2+p3+p4+p5,"Is The Perimetere")
elif shape=='octagon':
    o1=int(input("Enter The First Side :"))
    o2=int(input("Enter The Second Side :"))
    o3=int(input("Enter The Third Side :"))
    o4=int(input("Enter The Fourth Side :"))
    o5=int(input("Enter The Fifth Side :"))
    o6=int(input("Enter The Sixth Side :"))
    o7=int(input("Enter The Seventh Side :"))
    o8=int(input("Enter The Eighth Side :"))
    print(o1+o2+o3+o4+o5+o6+o7+o8,"Is The Perimetere")
elif shape=='heptagon':
    l1=int(input("Enter The First Side :"))
    l2=int(input("Enter The Second Side :"))
    l3=int(input("Enter The Third Side :"))
    l4=int(input("Enter The Fourth Side :"))
    l5=int(input("Enter The Fifth Side :"))
    l6=int(input("Enter The Sixth Side :"))
    l7=int(input("Enter The Seventh Side :"))
    print(l1+l2+l3+l4+l5+l6+l7,"Is The Perimetere")
else :
    print("You Better Check Your Spelling Or Enter A More Basic Shape")
