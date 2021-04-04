from os import read


def getHtmlPage(lst: list) -> str:
    """
    Generates the html page.
    Input: list of HTML elements in str format
    Return: HTML Page
    """
    s = "<!DOCTYPE html><html>"
    for i in lst:
        s += str(i)
    s += "</html>"
    return s


def getList(lst: list, ordered: bool = True) -> str:
    """
    Returns the HTML List.
    Input:
        List : Python List
        ordered : True-> Ordered List , False-> Unordered List
    Return:
        str : Returns the HTML Script for the list
    """
    html = ""
    if ordered:
        html += "<ol>"
        for i in lst:
            html += "<li>" + str(i) + "</li>"
        html += "</ol>"
        return html
    else:
        html += "<ul>"
        for i in lst:
            html += "<li>" + str(i) + "</li>"
        html += "</ul>"
        return html


def getForm() -> str:
    with open("html/tst.html", "r") as file:
        s = file.read()
    # print(s)
    return s