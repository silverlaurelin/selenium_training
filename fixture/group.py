from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_filed("group_name", group.name)
        self.change_filed("group_header", group.header)
        self.change_filed("group_footer", group.footer)

    def change_filed(self, filed_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filed_name).click()
            wd.find_element_by_name(filed_name).clear()
            wd.find_element_by_name(filed_name).send_keys(text)

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0) :
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None



    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()



    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_group_by_index(self,index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
       # open modification from
        wd.find_element_by_name("edit").click()
        # fil group form
        self.fill_group_form(new_group_data)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def  get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))

        return list(self.group_cache)





