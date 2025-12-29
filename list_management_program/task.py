import json

class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = "Не выполнено"
    
    def mark_done(self):
        self.is_done = "Выполнено"
    
    def to_dict(self):
        return {
            "title": self.title,
            "is_done": self.is_done
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"])
        task.is_done = data["is_done"]
        return task