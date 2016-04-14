
from model.group import Group

def test_delete_firs_group(app):
    if app.group.count() == 0:
      app.group.create(Group(name="some name", header="some logo", footer="some footer"))
    app.group.delete_first_group()
