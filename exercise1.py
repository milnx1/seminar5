try:
	file1=open('mailbox.txt')
except:
	print("File cannot be opened or doesn't exist")
	exit()

lines=file1.readlines()
count=0
for line in lines:
	count+=line.count("@")

file2=open("output.txt","w")
file2.write(str(count))
print(count)
file1.close()
file2.close()

