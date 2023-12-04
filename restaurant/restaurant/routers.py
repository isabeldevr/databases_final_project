class MongoDBRouter(object):
     """
     A router to control all database operations on models in the MenuItem application.
     """
     def db_for_read(self, model, **hints):

          if model._meta.model_name == 'menuitem':
               return 'mongodb'
          return None

     def db_for_write(self, model, **hints):
          if model._meta.model_name == 'menuitem':
               return 'mongodb'
          return None

     def allow_relation(self, obj1, obj2, **hints):
          print(obj1._meta.model_name)
          if obj1._meta.model_name == 'menuitem' or \
             obj2._meta.model_name == 'menuitem':
             return True
          return None

     def allow_migrate(self, db, app_label, model_name=None, **hints):
          if model_name == 'menuitem':
               return db == 'mongodb'
          return None