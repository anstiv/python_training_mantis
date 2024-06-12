from model.project import Project
import random
import string


def test_create_project_soap(app):
    old_projects = app.soap.get_project_list()
    project = Project(name=random_string("name", 10), description=random_string("description", 20))
    app.project.create_project(project)
    new_projects = app.soap.get_project_list()
    app.session.logout()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_create_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name=random_string("name", 10), description=random_string("description", 20))
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    app.session.logout()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
