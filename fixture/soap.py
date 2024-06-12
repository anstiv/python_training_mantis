from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):

        client = Client(self.app.config["web"]["baseUrl"] + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        project_list = []
        client = Client(self.app.config["web"]["baseUrl"] + "/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(self.app.config['webadmin']['username'],
                                                                      self.app.config['webadmin']['password'])
            for row in projects:
                project_list.append(Project(id=row.id, name=row.name, description=row.description))
            return project_list
        except WebFault:
            return False

