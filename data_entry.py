from pathlib import Path
import fitz
import pandas as pd

data_list = pd.read_excel('dataset.xlsx', sheet_name='Group A')

target_form = 'ChapterMembershipApplication.pdf'

doc = fitz.open(target_form)

# page 2
target_page = doc[1]

year_in_school = ['Sophomore', 'Junior', 'Senior', 'Graduate']

# iterate each row in data_list df
for indx, row in data_list.iterrows():
    for indx2, field in enumerate(target_page.widgets()):        
        if indx2 in (10, 11, 12, 13):
            field.field_value = False
            field.update()

        if indx2 == 2:
            field.field_value = row['Name']
            field.update()
        
        if indx2 == 3:
            field.field_value = row['Home Address']
            field.update()

        if indx2 == 5:
            field.field_value = row['School Address']
            field.update()

        if indx2 == 7:
            field.field_value = row['Phone Number']
            field.update()
        
        if indx2 == 8:
            field.field_value = row['School Email']
            field.update()

        if indx2 == 9:
            field.field_value = row['Personal Email']
            field.update()

        if indx2 == 10 and row['Year in School'] == 'Sophomore':
            print('Sohpomore checked')
            field.field_value = True
            field.update()
        else:
            field.field_value = False
            field.update()

        if indx2 == 11 and row['Year in School'] == 'Junior':
            print('Junior checked')
            field.field_value = True
            field.update()
 

        if indx2 == 12 and row['Year in School'] == 'Senior':
            print('Senior checked')
            field.field_value = True
            field.update()
   
        
        if indx2 == 13 and row['Year in School'] == 'Graduate':
            print('Graduate checked')
            field.field_value = True
            field.update()
       

        if indx2 == 14:
            field.field_value = str(row['Anticipated Year of Graduation'])
            field.update()
            
        if indx2 == 15:
            field.field_value = str(row['Current Overall GPA'])
            field.update()

        if indx2 == 16:
            field.field_value = str(row['English Hours Completed'])
            field.update()

        if indx2 == 17:
            field.field_value = str(row['Current English GPA'])
            field.update()

    doc.save('./applications/application_{0}.pdf'.format(row['Name']))