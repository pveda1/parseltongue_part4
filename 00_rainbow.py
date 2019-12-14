def write_colorful_text():    #(string, style, foreground, background): 
    for style in range(8):
        for foreground_color in range(30,38): 
            s1 = ''
            for background_color in range(40,48):
                format = ';'.join([str(style), str(foreground_color), str(background_color)]) 
                s1 += '\x1b[%sm %s \x1b[0m' % (format, x)
            print(s1) 
        print('\n')

x = ['R','A', 'I', 'N', 'B', 'O', 'W']

#write_colorful_text("R", \33[1m, \33[31m, \33[40m)
write_colorful_text()

def write_color_text(string, style, foreground, background):
    for style in range(8):
        for foreground in range(30, 38):
            s1 = ""
            for background in range(40, 48):
                format = ';'.join([str(style), str(foreground), str(background)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, R)
            print(s1)
        print('\n')
