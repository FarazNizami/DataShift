from pathlib import Path
import fitz

target_form = 'ChapterMembershipApplication.pdf'

doc = fitz.open(target_form)

target_page = doc[1]

font_rgb = (0, 137, 210)
font_color = tuple(value / 255 for value in font_rgb)

for indx, field in enumerate(target_page.widgets()):        

    # index checking        
    if field.field_type == fitz.PDF_WIDGET_TYPE_TEXT:  # if the field is a text field
        field.field_value = '{0}_{1}'.format(indx, field.field_type)  # insert the text into the field
        field.update()
    elif field.field_type == fitz.PDF_WIDGET_TYPE_CHECKBOX:
        field.field_value = True
        field.update()  # Update the field with the new value
        target_page.insert_text(field.rect.tl, "This is the index: {0}".format(indx), fontsize=12, color=font_color)

doc.save('application_index.pdf')

