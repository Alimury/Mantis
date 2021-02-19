from model.project import Project
from generator.project import random_string



def test_add_project(app):
    app.session.login("administrator", "root")
    project = Project(name=random_string("test_1", 10), description=random_string("test_2222", 10))
    old_projects = app.soap.get_projects_list("administrator", "root")
    app.project.create(project)
    new_projects = app.soap.get_projects_list("administrator", "root")
#    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(old_projects, key=Project.id_or_max)


