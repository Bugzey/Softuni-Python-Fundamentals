#   Site, domain and queries (if any)
class Website:
    def __init__(self, host, domain, queries = []):
        self.host, self.domain = [item.strip() for item in [host, domain]]
        if len(queries) != 0:
            self.queries = [query.strip() for query in queries.split(',')]
        else:
            self.queries = []

    def __str__(self):
        result = 'https://www.' + self.host + '.' + self.domain
        if len(self.queries) > 0:
            query_list = '&'.join(['[' + query + ']' for query in self.queries])
            result += '/query?=' + query_list
        return(result)

website_list = []

while True:
    user_input = input().split('|')
    if user_input[0] == 'end':
        print(*website_list, sep = '\n')
        break
    
    cur_site = Website(*user_input)
    website_list.append(cur_site)
