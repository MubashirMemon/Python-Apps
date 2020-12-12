{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# MarkSheet App uisng Python.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-------------------------------------------------------\n",
      "                MARK SHEET APP \n",
      "-------------------------------------------------------\n",
      "\n",
      "Enter your marks to generate marksheet\n",
      "Enter your English Marks (Paper Marks: 100) : 78\n",
      "Enter your Urdu Marks (Paper Marks: 100) : 76\n",
      "Enter your Math Marks (Paper Marks: 100) : 90\n",
      "Enter your Chemistry Marks (Paper Marks: 50) : 78\n",
      "Enter your Physics Marks (Paper Marks: 50) : 76\n",
      "\n",
      "STUDENT OBTAINED MARKS:\n",
      "ENGLISH MARKS IS : 78 OUT OF 100\n",
      "URDU MARKS IS : 76 OUT OF 100\n",
      "MATH MARKS IS : 90 OUT OF 100\n",
      "CHEMISTRY MARKS IS : 78 OUT OF 50\n",
      "PHYSICS MARKS IS : 76 OUT OF 50\n",
      "\n",
      "TOTAL MARKS OBTAINED: 398 OUT OF 400\n",
      "\n",
      "STUDENT PERCENTAGE :99.5\n",
      "\n",
      "'A' Grade\n",
      "Press enter to continue, or type 'Exit' then press enter to stop: exit\n",
      "Enter your English Marks (Paper Marks: 100) : 90\n",
      "Enter your Urdu Marks (Paper Marks: 100) : 90\n",
      "Enter your Math Marks (Paper Marks: 100) : 90\n",
      "Enter your Chemistry Marks (Paper Marks: 50) : 90\n",
      "Enter your Physics Marks (Paper Marks: 50) : 90\n",
      "\n",
      "STUDENT OBTAINED MARKS:\n",
      "ENGLISH MARKS IS : 90 OUT OF 100\n",
      "URDU MARKS IS : 90 OUT OF 100\n",
      "MATH MARKS IS : 90 OUT OF 100\n",
      "CHEMISTRY MARKS IS : 90 OUT OF 50\n",
      "PHYSICS MARKS IS : 90 OUT OF 50\n",
      "\n",
      "TOTAL MARKS OBTAINED: 450 OUT OF 400\n",
      "\n",
      "STUDENT PERCENTAGE :112.5\n",
      "\n",
      "'A' Grade\n",
      "Press enter to continue, or type 'Exit' then press enter to stop: Exit\n"
     ]
    }
   ],
   "source": [
    "\n",
    "text  = '-------------------------------------------------------\\n'\n",
    "text  += '                MARK SHEET APP \\n'\n",
    "text  += '-------------------------------------------------------\\n\\n'\n",
    "text  += 'Enter your marks to generate marksheet'\n",
    "print(text)\n",
    "\n",
    "subjects = {\n",
    "    'english': [100,0], # subject = [paper marks, obtain marks]\n",
    "    'urdu': [100,0],\n",
    "    'math': [100,0],\n",
    "    'chemistry':[50,0],\n",
    "    'physics': [50,0],\n",
    "}\n",
    "\n",
    "while True:\n",
    "    marks, total_marks, paper_num = '', 0 , 0\n",
    "    marksheet = '\\nStudent Obtained Marks:\\n'\n",
    "    \n",
    "    for subject in subjects:\n",
    "        text = 'Enter your {} Marks (Paper Marks: {}) : '.format(subject.title(),subjects[subject][0])\n",
    "        marks = input(text)\n",
    "\n",
    "        if not marks.isalnum():\n",
    "            text = 'Incorrect input value \\n Please try again\\n'\n",
    "            continue\n",
    "\n",
    "        marks =  int(marks)\n",
    "        total_marks += marks\n",
    "        paper_num += subjects[subject][0] \n",
    "        subjects[subject][1] = marks\n",
    "        \n",
    "        marksheet +='{} marks is : {} out of {}\\n'.format(subject,marks,subjects[subject][0])\n",
    "        \n",
    "    marksheet +='\\nTotal marks obtained: {} out of {}\\n'.format(total_marks,paper_num)\n",
    "    percentage = (total_marks/paper_num)*100\n",
    "    marksheet +='\\nStudent percentage :{}\\n'.format(percentage)\n",
    "    \n",
    "    print(marksheet.upper())\n",
    "\n",
    "    percentage = int(percentage)\n",
    "\n",
    "    if  percentage  >=88:\n",
    "        text = \"'A' Grade\"\n",
    "    elif percentage >=75:\n",
    "        text = \"'B' Grade\"\n",
    "    elif percentage>=60:\n",
    "        text = \"'C' Grade\"\n",
    "    else:\n",
    "        text =\"Fail \"\n",
    "\n",
    "    print(text)\n",
    "    text = '\\n\\n------------------------------------------------------\\n'\n",
    "    text = 'Press enter to continue, or type \\'Exit\\' then press enter to stop: '\n",
    "    result = input(text)\n",
    "    if result.strip()=='Exit':\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}