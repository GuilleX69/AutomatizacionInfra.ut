#!/bin/bash

archivo="Archivo.csv"
echo "ID, CAMIONETA"
grep -i "adolfo" "$archivo" | awk -F ',' '{print $1 "," $19}' | column -s, -t
                                                                                        
