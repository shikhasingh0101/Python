def QuestionsMarks(strParam):
    last_num = None
    question_count = 0
    
    for char in strParam:
        if char.isdigit():
            num = int(char)
            if last_num is not None and last_num + num == 10:
                if question_count != 3:
                    return 'false'
                question_count = 0
                return 'true'
            last_num = num
        elif char == '?':
            question_count += 1
            
    return 'false'

print(QuestionsMarks("arrb6???4XXbl5???eee5"))