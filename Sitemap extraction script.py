f = open("tagine_sitemap_output.txt", "a")
with open('tagine_sitemap.txt', 'r') as file:
    data = []
    for line in file:
              data.append(line)

for line in data:
    if not line.startswith('<lastmod>') :
        f.write(line)
 
f.close()