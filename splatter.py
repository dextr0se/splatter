#!/usr/bin/env python3
# splatter.py - python3 script that takes xml notes and auto-builds HTML page for quick reference and copy-splat
import xml.etree.ElementTree as et
tree = et.parse('xml/references.xml')
root = tree.getroot()


def generateMenu(mbr_root):
    mbr_html_document = ''
    for mbr_menu_item in mbr_root:
        mbr_html_document += '\t<li>\n\t\t<a href="#' + mbr_menu_item.text.strip(' \n\t') + \
                             '" data-toggle="collapse" aria-expanded="false">' + \
                             mbr_menu_item.text.strip(' \n\t') + '</a>\n'
        mbr_html_document += '\t\t<ul class="collapse list-unstyled" id="' +  \
                             mbr_menu_item.text.strip(' \n\t') + '">\n'
        for mbr_submenu_item in mbr_menu_item:
            mbr_html_document += '\t\t\t<li> <a href="#' + mbr_submenu_item.text.strip(' \n\t') + \
                                 '">' + mbr_submenu_item.text.strip(' \n\t') + '</a></li>\n'
        mbr_html_document += '\t\t</ul>\n\t</li>\n'
    mbr_html_document += '''</ul>
</nav>
<div class="container-fluid"><br>\n\n'''
    return mbr_html_document


# READ IN THE HTML HEAD
try:
    headFile = open('files/html-head', 'r')
    html_document = headFile.read()
    headFile.close()
except Exception as e:
    print(e)


# Create Menu
html_document += generateMenu(root)


# Loop through each Subject
for subject in root:
    subject_name = subject.text.strip(' \n\t')
    print('(+) Starting XML Parse on subject: ' + subject_name)
    total_sections = len(subject.findall('section'))
    print('\t(+) FOUND ' + str(total_sections) + ' SECTIONS WITHIN THE ' + subject_name + ' SUBJECT')

    html_document += '<div class="panel-group" id="accordion">'
    # START ITERATE/PARSING SECTIONS
    section_counter = 1
    for section in subject:
        section_name = section.text.strip(' \n\t')

        # START ITERATE/PARSING CONTENT WITHIN SECTION
        html_document += '\t<div id="' + section_name + '" class="alert alert-info" role="alert"><center><h4>' + section_name + '</h4></center>\n'
        for content in section:
            if content.tag == "content-title":
                content_title = content.text.strip('\n\t')

                # ADD COLLAPSIBLE CONTENT WITH CONTENT TILE AS BUTTON TEXT
                html_document += '\t\t<button class="accordion-toggle btn btn-danger btn-block" data-toggle="collapse" data-parent="#accordion"' \
                                 + ' type="button"' + \
                                 ' data-target="#' + content_title + '">' + content_title + \
                                 '</button><br>\n' + '\t\t'
            if content.tag == "content":
                content_lines = content.text.split('\n')
                html_document += '\t\t<div class="panel-collapse collapse in w3-code w3-black" id="' + content_title + '">\n'

                # ITERATE THROUGH EACH LINE IN CONTENT
                for content_line in content_lines:
                    content_line = content_line.strip(' \t')
                    # CLEAR ANY BLANK LINES
                    if len(content_line.strip()) == 0:
                        content_line = ''
                        print('(*) - FOUND BLANK CONTENT LINE - CHECK XML AT ' + content_title)
                    # IF FIRST CHAR IN LINE IS A # - CHANGE FONT COLOR FOR LINE
                    if content_line[:1] == "#":
                        html_document += '\t\t\t<font color ="blue">' + content_line + '</font><br>\n'
                    # CHANGE FONT COLOR OF LINE
                    else:
                        html_document += '\t\t\t<font color="green">' + content_line + '</font><br>\n'
                # CLOSE OUT CONTENT DIV
                html_document += '\t\t</div><br>\n'
            #html_document += '</div>'
        # CLOSE OUT SECTION DIV
        html_document += '\t</div>\n'
        # ONCE LAST SECTION HAS BEEN REACHED - CLOSE OUT SUBJECT DIV
        #if section_counter == total_sections:
        #    html_document += '</div><br>\n'
        #else:
        #    section_counter += 1

    html_document += '</div>'

# END OF LOOP - CLOSE OUT FINAL DIV / BODY / HTML TAGS
html_document += '''
</div>
<button onclick="toggleMenu()" id="menuToggle" style="display: block">Toggle</button>
<button onclick="topFunction()" id="myBtn" title="Go to top">Top</button>
<button id="openAll" class="openall" style="display: block">open all</button>
<button id="closeAll" class="closeall" style="display: block">close all</button>

<script type="text/javascript">
    $(document).ready(function() {
           $('#sidebar').toggleClass('active');
    });

    function toggleMenu() {
        $('#sidebar').toggleClass('active');
        
    }

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("myBtn").style.display = "block";
        } else {
            document.getElementById("myBtn").style.display = "none";
        }
    }
    
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }
</script>

<script>
    $('.closeall').click(function(){
      $('.panel-collapse.in')
        .collapse('hide');
    });
    $('.openall').click(function(){
      $('.panel-collapse:not(".in")')
        .collapse('show');
    });
</script>

</body>
</html>
'''

try:
    htmlFile = open("splatter.html", "w")
    htmlFile.write(html_document)
    htmlFile.close()
    print('(+) HTML FILE GENERATED')
except Exception as e:
    print('(-) FILE ERROR: ' + e)

