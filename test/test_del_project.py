from model.project import Project
from random import randrange


def test_delete_some_project_soap(app):
    if app.project.count() == 0:
        app.project.create_project(Project(name="test"))
    old_projects = app.soap.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.soap.get_project_list()
    old_projects[index:index+1] = []
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_delete_some_project(app):
    if app.project.count() == 0:
        app.project.create_project(Project(name="test"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects[index:index+1] = []
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
