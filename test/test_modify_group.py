from model.group import Group

def test_modify_group_name(app):
   old_groups = app.group.get_groups_list()
   app.group.modify_first_group(Group(name="new name"))
   new_groups = app.group.get_groups_list()
   assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    old_groups = app.group.get_groups_list()
    app.group.modify_first_group(Group(header="new header"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)

    
