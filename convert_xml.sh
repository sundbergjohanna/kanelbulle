
#!/bin/bash

# Usage: ./convert_to_xml.sh <directory where .msh is located>
# eg: /home/ubuntu/murtazo/cloudnaca/msh

cd murtazo
cd cloudnaca
cd msh

for f in *.msh; do
    dolfin-convert "$f" "${f%.*}.xml"
done
echo "*** Converted to xml ***"
for x in *.msh; do
     rm "$x"
done
echo "*** Deleted all msh ***"
