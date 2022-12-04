import re

# Task 1

mtxt = mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

# print(re.findall(r"\s\w+[._-]*\w+\@\w+\.*\w+\.\w+", mtxt))


# htmltxt = """ bla bla bla
# <h1> My Rubric </h1>
 # bla bla bla. """

# print(re.findall(r"<h1>\s*(.*?)\s*</h1>", htmltxt))


# Main Task

f = open("tabla.html", encoding="utf-8")
txt = f.read()

simpsons = re.findall(r"""<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*<div class="svtJsStopPropagation">\s*<div class="svtTablaTitleInfo svtHide-Js">\s*<div class="svtTablaContent-Description">\s*<p class="svtXMargin-Bottom-10px">\s*Amerikansk animerad komediserie från\s*\d+(?:\-*\d+)*. Säsong\s*(\d+)\.\s*Del\s*(\d+)\s*\w+\s*(\d+)\.\s*(.+?) Simpsons bor i Springfield.""", txt)


for i in range(len(simpsons)):
    print("Tid:\t", simpsons[i][0])
    print("Säsong:\t", simpsons[i][1])
    print("Avsnitt: {}/{}".format(simpsons[i][2], simpsons[i][3]))
    print("Handling", simpsons[i][4])
    print("-----------------------")
