# Úkol na 5. 10. 2026
import re

text = """to square(side)
  repeat 4 [
    forward side
    right 90
  ]
end

color "green"
square(100)
color "blue"
square(100) ;Tady bude třeba dlouhý komentář
"""
colors = re.findall(r'\"([a-z]+)\"', text)
print(colors)
comments = re.findall(r';(.*)$', text)
print(comments)

text = """for (i = 0; i < 10; i++) {
  if (i % 2 == 0) {
    print(i)
  }
}"""

operators = re.findall(r'(<=|>=|==|!=|\+\+|\-\-|[+\-*/<>=()\[\],\%])', text)
print(operators)
