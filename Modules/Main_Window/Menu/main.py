# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:

from Modules.Settings.Default_folders.main  import DefaultFolders
from Modules.Settings.Extensions.extensionmanager     import ExtensionManager
from Modules.Settings.App_variables.main             import Variables
from Modules.Project.New.projectnew                   import ProjectNew
from Modules.Softwares.main                      import SoftwareManager
from Modules.Softwares.main                      import SoftwaresBrowser
from PyQt5.QtWidgets                                  import *

class MainMenu(QMenuBar):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__()

        #modules
        self.module_path_vars    = Variables()
        self.module_extensions   = ExtensionManager()
        self.module_def_folders  = DefaultFolders()
        self.module_new_project  = ProjectNew()
        self.module_soft_manager = SoftwareManager()
        self.module_soft_browser = SoftwaresBrowser()

        #menus
        self.menu_settings  = QMenu('Settings')
        self.menu_softwares = QMenu('Softwares')
        self.menu_project   = QMenu('Projects')

        #actions
        self.action_soft_browser = QAction('Browser', self.menu_softwares)
        self.action_soft_manager = QAction('Manager', self.menu_softwares)
        self.action_proj_new     = QAction('New project', self.menu_project)
        self.action_def_folders  = QAction('Default folders', self.menu_settings)
        self.action_paths        = QAction('Paths', self.menu_settings)
        self.action_extensions   = QAction('Extension manager', self.menu_settings)


        #ADD ACTIONS
        self.menu_settings.addAction(self.action_paths)
        self.menu_settings.addAction(self.action_extensions)
        self.menu_settings.addAction(self.action_def_folders)
        self.menu_project.addAction(self.action_proj_new)
        self.menu_softwares.addAction(self.action_soft_manager)
        self.menu_softwares.addAction(self.action_soft_browser)


        #ADD MENUS
        self.addMenu(self.menu_project)
        self.addMenu(self.menu_softwares)
        self.addMenu(self.menu_settings)


        #CONNECTS
        self.action_soft_browser.triggered.connect(self.module_soft_browser.show)
        self.action_soft_manager.triggered.connect(self.module_soft_manager.show)
        self.action_paths.triggered.connect(self.module_path_vars.show)
        self.action_proj_new.triggered.connect(self.module_new_project.show)
        self.action_extensions.triggered.connect(self.module_extensions.show)
        self.action_def_folders.triggered.connect(self.module_def_folders.show)