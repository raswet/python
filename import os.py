import os

FILE_NAME = "C:/Users/swer/Documents/hh_vacancies.csv"

# Проверяем существование файла
file_exists = os.path.exists(FILE_NAME)
print(f"File exists: {file_exists}")

# Проверяем существование каталога
directory = os.path.dirname(FILE_NAME)
directory_exists = os.path.exists(directory)
print(f"Directory exists: {directory_exists}")
