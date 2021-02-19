from model.project import Project
import random


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(name='test_mantis', description='test_mantis'))
    old_projects = app.soap.get_projects_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.soap.get_projects_list("administrator", "root")
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(new_projects, key=Project.sortname) == sorted(old_projects, key=Project.sortname)

