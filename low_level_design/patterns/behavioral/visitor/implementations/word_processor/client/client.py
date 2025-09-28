"""Client runner"""
from elements.paragraph import Paragraph
from elements.image_element import ImageElement
from elements.table_element import TableElement
from visitors.render_visitor import RenderVisitor
from visitors.spellchecker_visitor import SpellCheckerVisitor

def run_word_processor():
    table_data=[['Name','Age'], ['Ram','20'],['Shyam','18'],['John','33']]
    elements=[
        Paragraph("This is a visitor design pattern implementation"),
        ImageElement('visitor.png'),
        TableElement(table_data)
    ]
    # 👉 First dispatch = decision based on the element type (Paragraph, ImageElement, TableElement).

    render=RenderVisitor()
    spellchecker=SpellCheckerVisitor() 

    # 👉 Second dispatch = decision based on the visitor type.

    print(f"\n-------- Render Documnent -------")
    for element in elements:
        # First dispatch: which 'accept' method (based on element type)
        # Second dispatch: which 'visit_*' method (based on visitor type)
        element.accept(render)  # double dispatch

    print(f'\n******** Check Spellings *******')
    for element in elements:
        element.accept(spellchecker) #double dispatch



