print("Sudhanhsu Singh")
A=[9,4,1,3,2]
temp = 0;

print("Elements of array: ");
for i in range(0, 5):
    print(A[i], end=" ");
for i in range(0,5):
    for j in range(i+1, 5): 
        if (A[i] > A[j]): 
            temp = A[i];
            A[i]= A[j];
            A[j] = temp;
print();

print("Elements of array sorted in ascending order: ");
for i in range(0, 5):
    print(A[i],end=" ");