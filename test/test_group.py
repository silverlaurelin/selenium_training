# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
     success = True
     app.group.create(Group(name="some name", header="some logo", footer="some footer"))


def test_add_empty_group(app):
    success = True
    app.group.create(Group(name="", header="", footer=""))




