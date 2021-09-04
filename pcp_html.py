import htmlGen4
import html_utilities

tag = htmlGen4.create_html_object


def initialize_html_list():
    html_list = htmlGen4.new_html_document()
    tag(html_list, 'meta', 'head', [{'charset': 'utf-8'}])
    tag(html_list, 'link', 'head', [{'rel': 'stylesheet'},
        {'type': 'text/css'}, {'href': 'normalize.css'}])
    tag(html_list, 'link', 'head', [{'rel': 'stylesheet'},
        {'type': 'text/css'}, {'href': 'css\\styles.css'}])
    tag(html_list, 'title', 'head', [], ("Denists"))
    return html_list


def main():
    html_list = initialize_html_list()


for i in moList:
    if i[2] in practices:
        continue
    else:
        practices.append(i[2])

practices.sort()


for practice in practices:
    output += practice + "\n"
    for i in moList:
        if practice == i[2]:
            output += i[1] + " " + i[0] + "\n"
    output += "\n"

# for i in moList:
#    pass
#    print (i[1] + " " + i[0]) #First Name Last Name

# pyperclip.copy(output)

def outputHTMLDocument(htmlDocument, fileName):
    htmlDoc = open('%s%s.html' % (htmlExportPath, fileName), 'w')
    numBytes = htmlDoc.write(htmlDocument) # Just to stifle the return
    print('Created HTML Document at %s%s.html' % (htmlExportPath, fileName))
    htmlDoc.close()

htmlExportPath = 'K:\\Users\\Reggie\\Desktop\\html self assessment\\export\\'

html_list = initialize_html_list()  # Init with Html, Head, and Body Tags
#  tag structure is tag(html_list, tag_name, nearest_parent_tag,
# [{attrib_name:value}], "content")

google_search_query = "http://google.com/search?q="

for practice in practices:
    tag(html_list, 'a', 'body',
        [{'href': google_search_query + '{}'.format(practice)},
         {'target': '_blank'}])
    tag(html_list, 'h1', 'a', [{'class': 'practice'}],
        '{}'.format(practice))
    for i in moList:
        if practice == i[2]:
            full_name = i[1] + " " + i[0] + " DDS"
            tag(html_list, 'a', 'body',
                [{'href': google_search_query + '{}'.format(full_name)},
                 {'target': '_blank'}])
            tag(html_list, 'p', 'a', [{'class': 'dentist'}],
                '{}'.format(full_name))
    tag(html_list, 'br', 'body')

htmlDocument = htmlGen4.parseHtmlDocumentList(html_list)
outputHTMLDocument(htmlDocument, "dentists")