from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username="administrator", password="root"):
        client = Client("https://www.mantisbt.org/bugs/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_projects_list(self, username, password):
        name_projects = []
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(username, password)
        for element in projects:
            name = element.name
            description = element.description
            name_projects.append(Project(name=name, description=description))
        return list(name_projects)

