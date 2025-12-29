from task import Task
import json

class FileManager:
    def save_to_file(self, filename, data):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False
    
    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return []

class TaskManager(FileManager):
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        data = self.load_from_file(self.filename)
        self.tasks = [Task.from_dict(item) for item in data]
        if data:
            print("Данные загружены.")
    
    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        if self.save_to_file(self.filename, data):
            print("Данные сохранены.")
    
    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f'Задача "{title}" добавлена.')
    
    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                if task.is_done == "Выполнено":
                    print(f'Задача "{title}" уже выполнена.')
                else:
                    task.mark_done()
                    print(f'Задача "{title}" отмечена как выполненная.')
                return
        
        print(f'Задача "{title}" не найдена.')
        
        print(f'Задача "{title}" не найдена.')
    
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        
        for i, task in enumerate(self.tasks, 1):
            print(f'{i}. {task.title} - {task.is_done}')