# function with output
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"{format_f_name} {format_l_name}"


format_string = format_name("tAma", "haVik")
print(format_string)
