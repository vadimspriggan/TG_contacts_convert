
# Telegram Contacts Converter

Этот скрипт позволяет конвертировать экспорт контактов из Телеграм в формат `.vcf`, который можно импортировать в книгу контактов смартфона.

## Зачем нужен этот скрипт?

Телеграм автоматически собирает все контакты, которые хоть раз были на вашем телефоне. Даже если человека нет в Телеграм, его контакт всё равно может быть сохранён в приложении. Это делает Телеграм отличным резервным источником контактов в случае, если ваш телефон сломался или вы потеряли все контакты.

Скрипт позволяет взять экспортированный из Телеграм файл с контактами в формате JSON и конвертировать его в формат `.vcf`, который поддерживается большинством смартфонов для импорта контактов.

## Как получить файл с контактами из Телеграм?

1. Откройте десктопную версию Телеграм.
2. Перейдите в **Настройки** -> **Расширенные**.
3. Прокрутите страницу вниз и нажмите на пункт **Экспортировать данные**.
4. В появившемся списке отметьте галочками только **Список контактов**, а в самом конце выберите **Машиночитаемый JSON**.
5. Нажмите **Экспорт**.
6. Скорее всего, потребуется подождать сутки, так как Телеграм защищается от мошенников, которые могли угнать аккаунт.
7. Через сутки Телеграм предложит скачать экспортированный файл, который будет называться `result.json`.

## Как использовать скрипт?

1. Скачайте файл `result.json` с контактами из Телеграм.
2. Поместите его в ту же папку, где находится данный скрипт (`covert.py`).
3. Запустите скрипт:
   ```sh
   python covert.py
   ```
4. После запуска скрипт создаст файл `contacts.vcf`, который можно будет переслать на телефон и импортировать в книгу контактов.

## Требования

- Python 3.x должен быть установлен на вашем компьютере.

## Пример использования

Запустите скрипт, убедившись, что файл `result.json` и сам скрипт находятся в одной папке:

```sh
python covert.py
```

После выполнения команды вы получите файл `contacts.vcf` в той же папке, что и скрипт. Этот файл теперь можно переслать на смартфон и импортировать контакты обратно в телефонную книгу.

## Лицензия

Этот проект распространяется на условиях лицензии MIT. Свободно используйте и изменяйте его в соответствии с вашими потребностями.

---

# Telegram Contacts Converter

This script allows you to convert Telegram's exported contacts into the `.vcf` format, which can be imported into your smartphone's contacts book.

## Why do you need this script?

Telegram automatically collects all contacts that have ever been on your phone. Even if the person is not in Telegram, their contact may still be saved in the app. This makes Telegram an excellent backup source of contacts if your phone breaks or you lose all your contacts.

The script allows you to take the exported contacts file from Telegram in JSON format and convert it into `.vcf` format, which is supported by most smartphones for importing contacts.

## How to get the contacts file from Telegram?

1. Open the desktop version of Telegram.
2. Go to **Settings** -> **Advanced**.
3. Scroll down and click on **Export Telegram Data**.
4. In the list that appears, check only **Contact List**, and at the very bottom, select **Machine-readable JSON**.
5. Click **Export**.
6. You may need to wait 24 hours, as Telegram protects against scammers who may have hijacked the account.
7. After 24 hours, Telegram will allow you to download the exported file named `result.json`.

## How to use the script?

1. Download the `result.json` file with contacts from Telegram.
2. Place it in the same folder as this script (`covert.py`).
3. Run the script:
   ```sh
   python covert.py
   ```
4. After running the script, it will create a `contacts.vcf` file, which can then be sent to your phone and imported into the contacts book.

## Requirements

- Python 3.x must be installed on your computer.

## Example usage

Run the script, ensuring that the `result.json` file and the script are in the same folder:

```sh
python covert.py
```

After executing the command, you will get a `contacts.vcf` file in the same folder as the script. This file can now be sent to your smartphone and imported into the phone's contact book.

## License

This project is distributed under the MIT License. Feel free to use and modify it according to your needs.
