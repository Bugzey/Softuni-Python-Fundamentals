#   Encase words in HTML tags
class Website:
    def __init__(self, name = 'Unknown', title = 'Unknown', content = []):
        self.name = name
        self.title = title
        self.content = content

    def add_title(self, newtitle):
        if type(newtitle) != 'str':
            self.title = newtitle[0]
        else:
            self.title = newtitle

    def add_content(self, tag, content):
        new_content = '<' + tag + '>' + ' '.join(content) + '</' + tag + '>'
        self.content.append(new_content)

    def __str__(self):
        # Returning formatted html
        metadata = '<!DOCTYPE html>\n'
        header = '<head>\n\t' + '<title>\n\t' + self.title + '\n\t</title>\n' + '</head>\n'
        content = '<body>\n\t' + '\n\t'.join(self.content) + '\n</body>\n'
        footer = '</html>'

        result = metadata + header + content + footer
        return(result)

cur_website = Website()

while True:
    user_input = input()
    if user_input == 'exit':
        print(cur_website)
        open('output/05 Index.html', 'w').write(str(cur_website))
        break

    tag, content = user_input.split()[0], user_input.split()[1:]
    
    if tag == 'title':
        cur_website.add_title(content)
    else: 
        cur_website.add_content(tag, content)
