import xml.etree.ElementTree as ET
tree = ET.parse('xml/references.xml')
root = tree.getroot()

def countNumberSections(subject):
    sectionCounter = 0
    for section in subject:
        sectionCounter += 1
    return sectionCounter


htmlDocument = '''
<!DOCTYPE html>
<html lang=en>
<head>
    <title>splatter</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="css/bootstrap-3.3.7.min.css">
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/bootstrap-3.3.7.min.js"></script>
    <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.3.7.min.js"></script> -->
    <style>
        .w3-black,.w3-hover-black:hover{color:#fff!important;background-color:#000!important}
        .w3-code,.w3-codespan{font-family:Consolas,"courier new";font-size:16px}
        .w3-code{line-height:1.4;width:auto;background-color:#fff;padding:8px 12px;border-left:4px solid #4CAF50;word-wrap:break-word}
    </style>
</head>
<body class="w3-black">
'''

# Loop through each Subject
htmlDocument += '<div class="container-fluid"><br>\n'
for subject in root:
    subjectText = subject.text.strip(' \n\t')   # Iterate through each of the Subjects
    print subjectText
    htmlDocument += '\t<button type="button" class="btn btn-success btn-block" data-toggle="collapse" style="padding: 10px 10px;" data-target="#' + \
                    subjectText + '">' + subjectText + '</button><br>\n'
    htmlDocument += '\t<div id="' + subjectText + '" class="collapse">\n'
    # Count the number of Sections in the Subject - The last section needs </ul> tag at the end
    numSections = countNumberSections(subject)
    sectionNumber = 1
    for section in subject:
        sectionText = section.text.encode('utf-8').strip(' \n\t')
        htmlDocument += '\t\t<button type="button" class="btn btn-danger btn-block" data-toggle="collapse" data-target="#' + \
                    sectionText + '">' + sectionText + '</button><br>\n'
        htmlDocument += '\t\t<div id="' + sectionText + '" class="collapse">\n'
        for content in section:
            if content.tag == "content-title":
                contentTitle = content.text.encode('utf-8').strip('\n\t')
                htmlDocument += '\t\t\t<font color="red"><b>' + contentTitle + '</b></font>\n'
            if content.tag == "content":
                contentText = content.text.split('\n')
                htmlDocument += '\t\t\t<div class="w3-code w3-black">\n'
                for ctext in contentText:
                    ctext = ctext.encode('utf-8').strip(' \t')
                    if ctext == ' \n':
                        pass
                    if ctext[:1] == "#":
                        htmlDocument += '\t\t\t\t<font color ="blue">' + ctext + '</font><br>\n'
                    else:
                        htmlDocument += '\t\t\t\t<font color="green">' + ctext + '</font><br>\n'
                htmlDocument += '\t\t\t</div><br>\n'
        htmlDocument += '\t\t</div>\n'
        # Once the last section has been reached, add the final closing tags
        if sectionNumber == numSections:
            htmlDocument += '\t</div><br>\n'
        else:
            sectionNumber += 1
htmlDocument += '</div>'

htmlDocument += '''
</body>
</html>
'''

try:
    htmlFile = open("splatter.html", "w")
    htmlFile.write(htmlDocument)
    htmlFile.close()
except Exception as e:
    print e

