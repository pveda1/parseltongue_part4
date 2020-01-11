def write_colorful_text(string, style, foreground, background):
    s1 = ""
    format = ';'.join([str(style), str(foreground), str(background)])
    s1+= '\x1b[%sm %s \x1b[0m' % (format, string)
    print(s1)

write_colorful_text("R", 8, 31, 40)
write_colorful_text("A", 8, 32, 40)
write_colorful_text("I", 8, 33, 40)
write_colorful_text("N", 8, 36, 40)
write_colorful_text("B", 8, 34, 40)
write_colorful_text("O", 8, 35, 40)
write_colorful_text("W", 8, 38, 40)
