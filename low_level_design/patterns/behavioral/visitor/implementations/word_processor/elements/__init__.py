"""Elements implementation in visitor design pattern"""
from elements.base_element import Element
from elements.image_element import ImageElement
from elements.paragraph import Paragraph
from elements.table_element import TableElement


__all__=[
'Element','ImageElement','Paragraph','TableElement'
]

#return all these classes and consume from anywhere 