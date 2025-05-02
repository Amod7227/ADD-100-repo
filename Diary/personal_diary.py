#Main function for diary program
def diary_program():
    #prompt user to enter date of diary entry
    diary_date = input("Please enter the date of Diary entry (M/D/Y): ")
    #prompt user to enter the time of diary entry
    diary_time = input("Please enter the time of Diary entry (00:00): ")
    #prompt user to enter diary entry
    Diary_Entry= input("Please enter your Diary entry: ")
    #File path variable created because 'ADD-100-repo' caused issues with the program
    file_path = 'ADD-100-repo/Diary/diary.txt'
    #Open or create a file named diary.txt in append mode using open()
    diary = open(file_path, 'a') #'a' mode = append
    #Write Date to opened file
    diary.write(diary_date +'\n')
    #Write time to opened file
    diary.write(diary_time +'\n\n')
    #Write Diary entry to opened file
    diary.write(Diary_Entry +'\n\n\n')

    #close file with close()
    diary.close()
    
    #print statement to notify that diary entry was completed and how to view diary
    print("\nDiary entry submitted.\nTo view diary entry open diary.txt file")



#Call Diary function to run
diary_program()