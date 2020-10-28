import os

def check_if_component_direct_exist():
    if not os.path.exists('components'):
        os.makedirs('components')

def createComponent(componentName : str):
    cLower = componentName.lower()
    cCap = cLower.capitalize()
    
    # Compnent.js
    with open("components/"+cCap+".js","w+") as compJS:
        compJS.write("import React from 'react';\n")
        compJS.write("import './"+cCap+".css';\n\n")
        compJS.write("function "+cLower+"() {\n\treturn(\n\t\t<div className=\""+cLower+"\">\n")
        compJS.write("\t\t\t<h1>I'm a \""+cCap+"\" Component</h1>\n")
        compJS.write("\t\t</div>\n\t)\n}\n\n")
        compJS.write("export default "+cLower+";")
    
    # Component.css
    with open("components/"+cCap+".css","w+") as compCSS:
        compCSS.write("."+cLower+" {\n\n}")  


def main():
    check_if_component_direct_exist()
    createComponent("test")

if __name__ == "__main__":
    main()
