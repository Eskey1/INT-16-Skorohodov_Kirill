import json


def parse_json(input_path, output_path):
    # Открываем файл с отчётом OWASP ZAP на чтение
    with open(input_path, 'r') as input_file:
        # Читаем содержимое этого файла
        report_data = json.load(input_file)
        vulnerabilities = []
        for site in report_data.get('site', []):
            for alert in site.get('alerts', []):
                vulnerability = {
                    'name': alert.get('name', ''),
                    'count': alert.get('count', 0)
                }
                vulnerabilities.append(vulnerability)

        # Создаем наш шаблон
        new_data = {
            'vulnerabilities': vulnerabilities
        }

        # Сохраняем преобразованные данные в новом файле
    with open(output_path, 'w') as output_file:
        # Сохраненяем данные в JSON-формате
        json.dump(new_data, output_file, indent=2)

input_path = "Your_Path/2023-12-17-ZAP-Report-.json"
output_path = "Your_path_to_output\Parse.json"

parse_json(input_path, output_path)