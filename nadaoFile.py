import os, shutil


def getPic():
   # setting the counter
   count = 0
   # getting the source and dest file
   src = input("Enter the source folder (the one u want to search in): ")
   trg = input("Enter the dest folder (the one u want the file to transfer to: ")
   # getting desired file type
   fileType = input("Enter the file type: (example: png, jpg, text, mp4)")
   # if someone add by mistake '.'
   if fileType[0] == '.':
      fileType = fileType[1:]
   print(fileType)
   # using os.walk to run throw the files
   for (root,dirs,files) in os.walk(src):
      for fileN in files:
         # finding the file that we are looking for
         if fileN.endswith('.'+fileType):
            count += 1
            # changing the file path for the shutil.copy so the library will know the full path
            beforePath = os.path.join(root,fileN)
            newPath = beforePath.replace(os.path.sep, '/')
            # copying the file to dest file
            shutil.copy2(newPath, trg)
   print("the amount of picture that was copied:",count)
   # checking if the user want something else
   answer = input("would u like to scan or quit? ").lower()
   # clearing all the screen
   os.system('cls')
   return answer
   


def getScan():
    # setting the counter
   count = 0
   # getting the source and dest file
   src = input("Enter the source folder (the one u want to search in): ")
   # getting desired file type
   fileType = input("Enter the file type: (example: png, jpg, text, mp4)")
   # if someone add by mistake '.'
   if fileType[0] == '.':
      fileType = fileType[1:]
   print(fileType)
   
   # using os.walk to run throw the files
   for (root,dirs,files) in os.walk(src):
      for fileN in files:
         if fileN.endswith("."+fileType):
            count += 1 
   print("the amount " + fileType + f" files that i found are: {count}")
   # checking if the user want something else
   answer = input("would u like to transfer or quit? ").lower()
   # clearing all the screen
   os.system('cls')
   return answer



def main():
   print("Hello welcome to nadaoFile")
   print("The python program that will make your life easyer")
   print("First u need to decide if u want to scan the file type or transfer the file type:")
   answer = input().lower()
   while True:
      if answer == 'scan':
         answer = getScan()
      elif answer == 'transfer':
         answer = getPic()
      elif answer == 'quit':
         break
      else:
         print('I didnt under stand your answer. Try Again!')
         answer = input("Enter your desired action: ").lower()
   print("thank you for using my program")
   print("wagovv")




if __name__ == "__main__":
   main()

