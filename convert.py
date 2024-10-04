import json
import os

# Получаем текущую директорию
current_dir = os.path.dirname(os.path.abspath(__file__))

# Чтение JSON-файла из текущего каталога
with open(os.path.join(current_dir, 'result.json'), 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создание .vcf файла в текущем каталоге
with open(os.path.join(current_dir, 'contacts.vcf'), 'w', encoding='utf-8') as vcf:
    for contact in data['contacts']['list']:
        # Создание карточки vCard
        vcf.write("BEGIN:VCARD\n")
        vcf.write("VERSION:3.0\n")
        if contact.get('first_name') or contact.get('last_name'):
            vcf.write(f"FN:{contact.get('first_name', '')} {contact.get('last_name', '')}\n")
            vcf.write(f"N:{contact.get('last_name', '')};{contact.get('first_name', '')};;;\n")
        if contact.get('phone_number'):
            vcf.write(f"TEL;TYPE=CELL:{contact['phone_number']}\n")
        if contact.get('date_unixtime'):
            vcf.write(f"BDAY:{contact['date_unixtime']}\n")
        vcf.write("END:VCARD\n\n")

print("Контакты успешно конвертированы в формат .vcf")
