import csv

with open("params.csv", 'r') as f:
    a = 0 
    for i in csv.reader(f):
        if a == 1:
            p = i
        a += 1

# funtion f(x,y) = a1 xx + a2 yy + a3 xy + a4 x + a5 y + a6

function_text = f"{p[0]} x\u00B2 + {p[1]} y\u00B2 + {p[2]} xy + {p[3]} x + {p[4]} y + {p[5]}"

new_txt = ""
i = 0

while i < len(function_text):
    if function_text[i] == "+" and function_text[i+2] == "-":
        print("yoo")
        new_txt += "- "
        i += 3
    else:
        new_txt += function_text[i]
        i += 1


with open("Params_to_function.txt", 'w', encoding="utf-8") as f:
    f.write(new_txt)

