from PyPDF2 import PdfFileWriter, PdfFileReader

# Read the invoice file
inputpdf = PdfFileReader(open("invoice.pdf", "rb"))

"""
Itration to split the pdf files and name them
"""
for num in range(inputpdf.numPages):
    # get the current page
    pageObj = inputpdf.getPage(num)

    # Extract the page content
    text = pageObj.extractText()
    # Split the content
    text2 = text.split()

    """
    Making the name for the file using the bill to name
    """

    # initalize the start and end list for holding the mark used in finding the name
    start = []
    end = []
    try:
        # loop through the list and get the name
        for i in text2:
            if text2[text2.index(i)][:5] == "PRICE" and len(i) > 5:
                start.append(text2.index(i))
            if text2[text2.index(i)][:3] == "TO:" and text2[text2.index(i)][:10] != "TO:INVOICE":
                end.append(text2.index(i))

        fname = text2[start[0]: start[0] + 2]
        fname[0] = fname[0][5:]
    except:
        # get the page content and name it with the page number
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(num))

        with open("%s.pdf" % num, "wb") as outputStream:
            output.write(outputStream)

    name = ""
    for i in fname:
        name += i
        name += " "

    # get the page content
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(num))

    # name construction
    filename = str(num)
    filename += " "
    filename += name

    # file write operation
    try:
        with open("%s.pdf" % filename, "wb") as outputStream:
            output.write(outputStream)
    except:
        with open("%s.pdf" % num, "wb") as outputStream:
            output.write(outputStream)
