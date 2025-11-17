no_of_block=1
max_length_block=1
c=1
block_length=1
while c<=8:
    num=int(input("Enter number:"))
    if c==1:
        prev=num
    else:
        if num>prev:
            block_length+=1
            prev=num
        else:
            no_of_block+=1
            prev=num
            if block_length>max_length_block:
                max_length_block=block_length
                block_length=1
    c+=1
print("number of block: ",no_of_block,"max length of block: ",max_length_block)
    
