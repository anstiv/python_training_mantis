from model.project import Project
import time


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'Manage')]").click()
        wd.find_element_by_xpath("//a[contains(text(),'Manage Projects')]").click()

    def open_create_project_page(self):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("inherit_global", project.IGC)
        self.change_field_value("view_state", project.view_status)
        self.change_field_value("description", project.description)
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def click_add_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def create_project(self, project):
        self.open_create_project_page()
        self.fill_form(project)
        self.click_add_project()
        self.project_cache = None
        #time.sleep(5)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            #for element in wd.find_elements_by_xpath("//div[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
            for element in wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:]:
                name = element.find_element_by_css_selector("td:nth-child(1)").text
                s = str(len(self.project_cache)+3)
                id_not_fetched = (element.find_element_by_xpath("//table[3]/tbody/tr[%s]/td[1]/a" % s).get_attribute("href"))
                id = id_not_fetched.replace(
                    "http://localhost/mantisbt-1.2.20/manage_proj_edit_page.php?project_id=", "")
                description = element.find_element_by_css_selector("td:nth-child(5)").text
                self.project_cache.append(Project(name=name, description=description, id=id))

        return list(self.project_cache)
