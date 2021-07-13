class DroptosObject():
    def __init__(self, tag, string):
        self.tag = tag
        self.string = string

    def show_object(self):
        info = f'{self.tag}: {self.string}'
        print(info)


tags = {
    "bm": "Bookmark",
    "t": "Task"
}

new_droptos = (
    ["t", "Арендовать VDS для нового проекта"],
    ["bm", "https://github.com/stargot"],
    ["bm", "https://docs.djangoproject.com/en/3.1/topics/class-based-views/mixins/"],    
    ["bm", "https://testdriven.io/blog/django-async-views/"],
    ["bm", "https://www.youtube.com/c/postnauka/videos"],
)

for i in new_droptos:
    for key, value in tags.items():
        if key == i[0]:
            tag = value
    string = i[1]
    obj = DroptosObject(tag, string)
    obj.show_object()
