



text  = '-------------------------------------------------------\n'
text  += '                MARK SHEET APP \n'
text  += '-------------------------------------------------------\n\n'
text  += 'Enter your marks to generate marksheet'
print(text)

subjects = {
    'english': [100,0], # subject = [paper marks, obtain marks]
    'urdu': [100,0],
    'math': [100,0],
    'chemistry':[50,0],
    'physics': [50,0],
}

while True:
    marks, total_marks, paper_num = '', 0 , 0
    marksheet = '\nStudent Obtained Marks:\n'
    
    for subject in subjects:
        text = 'Enter your {} Marks (Paper Marks: {}) : '.format(subject.title(),subjects[subject][0])
        marks = input(text)

        if not marks.isalnum():
            text = 'Incorrect input value \n Please try again\n'
            continue

        marks =  int(marks)
        total_marks += marks
        paper_num += subjects[subject][0] 
        subjects[subject][1] = marks
        
        marksheet +='{} marks is : {} out of {}\n'.format(subject,marks,subjects[subject][0])
        
    marksheet +='\nTotal marks obtained: {} out of {}\n'.format(total_marks,paper_num)
    percentage = (total_marks/paper_num)*100
    marksheet +='\nStudent percentage :{}\n'.format(percentage)
    
    print(marksheet.upper())

    percentage = int(percentage)

    if  percentage  >=88:
        text = "'A' Grade"
    elif percentage >=75:
        text = "'B' Grade"
    elif percentage>=60:
        text = "'C' Grade"
    else:
        text ="Fail "

    print(text)
    text = '\n\n------------------------------------------------------\n'
    text = 'Press enter to continue, or type \'Exit\' then press enter to stop: '
    result = input(text)
    if result.strip()=='Exit':
        break


