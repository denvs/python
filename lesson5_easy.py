import os

#функции для normal
def my_chdir(path):
	try:
		os.chdir(path)
		return 'Переход в папку завершён'
	except FileNotFoundError:
		return 'Папка не найдена'

def my_list(path):
	return '\n'.join(os.listdir(path))

def my_rmdir(path):
	try:
		os.removedirs(path)
		return 'Папка удалена'
	except FileNotFoundError:
		return 'Папка не найдена'

def my_mkdir(path):
	try:
		os.mkdir(path)
		return 'Папка создана'
	except FileExistsError:
		return 'Директория уже существует'

if __name__ == '__main__':

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

	path = os.getcwd()
	print(path)
	for i in range(1, 10):
		try:
			os.mkdir(f'{path}\dir_{i}')
		except FileExistsError:
			print('Такая директория уже существует')
	for i in range(1, 10):
		try:
			os.rmdir(f'{path}\dir_{i}')
		except FileNotFoundError:
			print('Такая директория не существует')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

	list_dir = [obj for obj in os.listdir() if os.path.isdir(obj)]
	print('\n'.join(list_dir))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

	import sys
	from shutil import copyfile

	path = sys.argv[0]
	name, ext = os.path.splitext(path)
	copy_path = f'{name}_copy{ext}'
	try:
		copyfile(path, copy_path)
	except:
		print('Не могу сделать копию файла')
