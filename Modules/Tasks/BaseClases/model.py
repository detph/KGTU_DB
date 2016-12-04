from DataBase.access_model import DBAccessModel





class ModelTask(DBAccessModel):

    #inits
    def __init__(self, DB, parent=None):
        super(ModelTask, self).__init__(
            app_db=DB,
            parent=parent,
            table=DBAccessModel.TableTasks
        )
