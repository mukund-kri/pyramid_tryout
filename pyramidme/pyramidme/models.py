from mongoengine import Document, StringField


class Task(Document):
    title = StringField(required=True)


    @staticmethod
    def add(task):
        task = Task(title=task['title'])
        task.save()
        return task

    @staticmethod
    def remove(task_id):
        task = Task.objects.get(pk=task_id)
        task.delete()



