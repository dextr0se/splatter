import xml.etree.ElementTree as et
tree = et.parse('xml/references.xml')
root = tree.getroot()

# READ IN THE HTML HEAD
try:
    headFile = open('files/html-head', 'r')
    html_document = headFile.read()
    headFile.close()
except Exception as e:
    print e


# Loop through each Subject
for subject in root:
    subject_name = subject.text.encode('utf-8').strip(' \n\t')
    print '(+) Starting XML Parse on subject: ' + subject_name
    # INSERT COLLAPSIBLE SUBJECT BUTTON WITH SUBJECT NAME
    html_document += '\t<button type="button" class="btn btn-success btn-block" data-toggle="collapse" ' + \
        'style="padding: 10px 10px;" data-target="#' + subject_name + '">' + subject_name + '</button><br>\n' + \
        '\t<div id="' + subject_name + '" class="collapse">\n'
    # GET THE NUMBER OF SECTIONS WITHIN SUBJECT
    total_sections = len(subject.findall('section'))
    print '\t(+) FOUND ' + str(total_sections) + ' SECTIONS WITHIN THE ' + subject_name + ' SUBJECT'

    # START ITERATE/PARSING SECTIONS
    section_counter = 1
    for section in subject:
        section_name = section.text.encode('utf-8').strip(' \n\t')
        # INSERT COLLAPSIBLE SECTION BUTTON WITH SECTION NAME
        html_document += '\t\t<button type="button" class="btn btn-danger btn-block" data-toggle="collapse" ' + \
            'data-target="#' + section_name + '">' + section_name + '</button><br>\n' + '\t\t<div id="' + \
            section_name + '" class="collapse">\n'

        # START ITERATE/PARSING CONTENT WITHIN SECTION
        for content in section:
            if content.tag == "content-title":
                content_title = content.text.encode('utf-8').strip('\n\t')
                # ADD FONT COLOR TO CONTENT TITLE
                html_document += '\t\t\t<font color="red"><b>' + content_title + '</b></font>\n'
            if content.tag == "content":
                content_lines = content.text.split('\n')
                html_document += '\t\t\t<div class="w3-code w3-black">\n'

                # ITERATE THROUGH EACH LINE IN CONTENT
                for content_line in content_lines:
                    content_line = content_line.encode('utf-8').strip(' \t')
                    # CLEAR ANY BLANK LINES
                    if len(content_line.strip()) == 0:
                        content_line = ''
                        print '(*) - FOUND BLANK CONTENT LINE - CHECK XML AT ' + content_title
                    # IF FIRST CHAR IN LINE IS A # - CHANGE FONT COLOR FOR LINE
                    if content_line[:1] == "#":
                        html_document += '\t\t\t\t<font color ="blue">' + content_line + '</font><br>\n'
                    # CHANGE FONT COLOR OF LINE
                    else:
                        html_document += '\t\t\t\t<font color="green">' + content_line + '</font><br>\n'
                # CLOSE OUT CONTENT DIV
                html_document += '\t\t\t</div><br>\n'
        # CLOSE OUT SECTION DIV
        html_document += '\t\t</div>\n'
        # ONCE LAST SECTION HAS BEEN REACHED - CLOSE OUT SUBJECT DIV
        if section_counter == total_sections:
            html_document += '\t</div><br>\n'
        else:
            section_counter += 1

# END OF LOOP - CLOSE OUT FINAL DIV / BODY / HTML TAGS
html_document += '''
</div>
</body>
</html>
'''

try:
    htmlFile = open("splatter.html", "w")
    htmlFile.write(html_document)
    htmlFile.close()
    print '(+) HTML FILE GENERATED'
except Exception as e:
    print '(-) FILE ERROR: ' + e

