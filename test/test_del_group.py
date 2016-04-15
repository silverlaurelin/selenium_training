
from model.group import Group

def test_delete_firs_group(app):

    if app.group.count() == 0:
      app.group.create(Group(name="some name", header="some logo", footer="some footer"))
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups