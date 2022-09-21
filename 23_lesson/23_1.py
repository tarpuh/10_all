from docxtpl import DocxTemplate


def create_training_sheet(class_name, subject_name, tpl_name="tpl_name", *korteh):
    doc = DocxTemplate(tpl_name)
    korteh = sorted(korteh)
    L = list()
    i = 0
    for elem in korteh:
        i += 1
        dic = {'num': i, 'fio': elem[0], 'mark': elem[1]}
        L.append(dic)
        context = {'class_name': class_name,
                   'subject_name': subject_name,
                   'marks': L}
        doc.render(context)
        doc.save("generated_doc.docx")


create_training_sheet("3И", "Математика", "tpl.docx", ("Петров Петр", "5"), ("Иванов Иван", "5"),
                      ("Сергеев Сергей", "3"), ("Никитин Никита", "4"))