from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    print("*** Менеджер задач ***")
    print("Команды: add, done, show, exit")
    
    while True:
        command = input("Введите команду: ").strip().lower()
        
        if command == "exit":
            manager.save_tasks()
            print("Программа завершена.")
            break
        
        elif command == "add":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.add_task(title)
            else:
                print("Ошибка: название задачи не может быть пустым.")
        
        elif command == "done":
            title = input("Введите название задачи: ").strip()
            if title:
                manager.mark_task_done(title)
            else:
                print("Ошибка: название задачи не может быть пустым.")
        
        elif command == "show":
            manager.show_tasks()
        
        else:
            print("Неизвестная команда.")
            print("Команды: add, done, show, exit")

if __name__ == "__main__":
    main()