# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
     success = True
     old_groups = app.group.get_groups_list()
     app.group.create(Group(name="some name", header="some logo", footer="some footer"))
     new_groups = app.group.get_groups_list()
     assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    success = True
    app.group.create(Group(name="", header="", footer=""))




