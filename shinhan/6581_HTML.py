string = ''
while True:
    try:
        current_str = input()
        if len(string) + len(current_str) <= 80:
            string += current_str
        else:
            print(string)
            print(current_str)

        if '<br>' in current_str:
            count_br = current_str.count('<br>')
            for _ in range(count_br):
                
        
    except:
        break