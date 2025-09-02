#!/usr/bin/python3
import this
 
# Décodage du Zen de Python
zen_de_python = "".join([this.d.get(c, c) for c in this.s])
 
print(zen_de_python)
