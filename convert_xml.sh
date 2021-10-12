
#!/bin/bash

# Usage: ./convert_to_xml.sh <directory where .msh is located>
# eg: /home/ubuntu/murtazo/cloudnaca/msh

for f in *.msh; do
    dolfin-convert "$f" "${f%.*}.xml"
done
echo "*** Moving files ***"
for f in *.msh; do
     rm "$f"
done
echo "*** Deleted msh files ***"