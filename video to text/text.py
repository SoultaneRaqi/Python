l_chunks=[dir['chunk{}'.format(i+1)] for i in range(len(dir))]
text='\n'.join(l_chunks)

with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(text) 
   print("Finally ready!")