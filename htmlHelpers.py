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