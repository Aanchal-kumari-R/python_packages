''' Package:- Package are a way of structuring python's module namespace by using dotted(.) module names.A package can have 
one or more modules which means , a package is collection of modules and packages. A package can contain packages. Package is  
nothing but a directory/folder.''' 

'''Creating a Package:- Package is nothing but a directory or folder which must contain a special file called __init__.py. 
__init__.py file can be empty , it indicates that the directory it contain is a python package, so it can be imported the 
same way a module can be imported.'''
# Syntax 1:-----------------

# import Admin.service 
# Admin.service.admin_service() 

# import Admin.product 
# Admin.product.admin_product()  

# import Admin.Common.header 
# Admin.Common.header.admin_common_header()   

# import Admin.Common.footer 
# Admin.Common.footer.Admin_Common_Footer() 

# import Tech.profile 
# Tech.profile.tech_profile()  

# import Tech.work 
# Tech.work.tech_work() 

# Syntax 2 :----------------

# from Admin import service 
# service.admin_service() 

# from Admin import product 
# product.admin_product()  

# from Admin.Common import footer 
# footer.Admin_Common_Footer()  

# from Admin.Common import header 
# header.admin_common_header() 

# from User import profile 
# profile.user_profile() 

# from User import request 
# request.user_request() 

# Syntax 3 :------------------

# from Admin.service import admin_service 
# admin_service()  

# from Admin.product import admin_product 
# admin_product()  

# from Admin.Common.footer import Admin_Common_Footer 
# Admin_Common_Footer() 

# from Admin.Common.header import admin_common_header 
# admin_common_header()  

# from User.profile import user_profile 
# user_profile()  

# from User.request import user_request 
# user_request() 

# Syntax 4 :--------------------

# from Admin import product,service 
# product.admin_product() 
# service.admin_service()    

# from Admin.Common import header,footer 
# header.admin_common_header() 
# footer.Admin_Common_Footer() 


# Syntax 5 :--------------------------- 

# from Admin import *  
# service.admin_service() 
# product.admin_product() 

# subpackage  
# from Admin import *  
# from Admin.Common import *  
# service.admin_service() 
# product.admin_product() 
# header.admin_common_header() 
# footer.Admin_Common_Footer() 

from Tech import work 
work.tech_work()


