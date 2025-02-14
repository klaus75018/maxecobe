from django.contrib.auth.models import User
from openai import OpenAI

client = OpenAI()

#Add New fils in VS
#def AddNewFile(thread_id, username, new_file, new_file_title, new_file_overview)


#MAJ SjsonDB
def mise_a_jour_informations_projet(sujet, children, attributes, username, project_name, thread_id, etude_name):
    
    import json
    mondic = {"sujet":sujet, "children":children, "attributes":attributes}
    mypath = f"aiecobe/json_files/{username}_{project_name}_{etude_name}.json"
    with open(mypath, "r") as main_json:
        print("je suis dans le with")
        main_dic = json.load(main_json)
        myliste = recherche_sujet(main_dic, mondic, 0, 0)
        new_dic = myliste[2]
        main_json.close()
    with open(mypath, "w") as new_json: 
        print("je suis dans le with2")
        json.dump(new_dic,new_json,indent=4)
        new_json.close()   
    print("je suis avant la mise a jour")
    AddNewJsonDB(project_name, thread_id, username, mypath)
    return "Mise à jour terminée"

    

def recherche_sujet(main_dic, added_data, x, y):
    pop = 0
    if added_data["sujet"] != main_dic["sujet"]:
        if main_dic["children"] != []:
            for i in main_dic["children"]:
                myliste = recherche_sujet(i, added_data, x+1, y+1)
                print(f"ma liste est {myliste}")
                i = myliste[2]
                x = myliste[0]
                y = myliste[1]
                if x!=y:
                    pop = 1
                    break
            
            if x == 0 and y == 0:
                main_dic["children"].append(added_data)
                
            pop = 1
  
        else:
            if x == 0 and y == 0:
                main_dic["children"].append(added_data)
                
                return [x, y, main_dic]
            else:
                return [x-1, y-1, main_dic]
    
    else:
       
        if added_data["children"] != []:
            for child in added_data["children"]:
                main_dic["children"].append(child)
                print(f"main_dic = {main_dic}")
  
        if added_data["attributes"] != []:
            for attribute in added_data["attributes"]:
                main_dic["attributes"].append(attribute)
                print(f"main_dic = {main_dic}")

        return [x-1, y, main_dic]
    if pop == 1:
       return [x-1, y-1, main_dic] 
    
  

def AddNewJsonDB(project_name, thread_id, username, jsonDB):
    project = FindProject(project_name, username)

    MAJ_DB(thread_id, jsonDB, project)
    

####################################################################

def FindProject(project_name, username):
    user = User.objects.get(username=username)
    myproject = user.project_set.get(name = project_name)
    myproject.save()
    return myproject


def MAJ_DB(thread_id, jsonDB, project):
    print("je suis dans MAJ_DB")
    ModifyOurDB(jsonDB, project, thread_id)
    ModifyVectorStoreDB(thread_id, jsonDB, project)

def ModifyOurDB(jsonDB, project, thread_id):
    project.etude_set.all().get(thread_id=thread_id).json_db = jsonDB
    project.save()

def ModifyVectorStoreDB(thread_id, jsonDB, project):
     print("je suis dans ModifyVectorStoreDB")
     json_file_DB_id = FindJsonDBVSId(project, thread_id)
     print(f"json_file_DB_id = {json_file_DB_id}")
     VS_id = FindVSId(project, thread_id)
     print(f"VS_id = {VS_id}")
     EraseVSOldDB(json_file_DB_id, VS_id)
     print("je suis avant le upload1")
     new_db_id = UploadAndIntegrateNewFile(VS_id, jsonDB, json_file_DB_id)
     print("je suis avant le update")
     UpdateOurDBDBId(project, new_db_id, thread_id)






def FindVSId(project, thread_id):
    id = project.etude_set.get(thread_id = thread_id).vs_id
    return id

def FindJsonDBVSId(project, thread_id):
    id = project.etude_set.all().get(thread_id=thread_id).json_db_id
    return id



def EraseVSOldDB(file_id, VS_id):
    from openai import OpenAI
    client = OpenAI()
    print("je suis dans EraseVSOldDB")
    deleted_vector_store_file = client.beta.vector_stores.files.delete(
        vector_store_id=VS_id,
        file_id=file_id
    )
    client.files.delete(file_id)



def UploadAndIntegrateNewFile(VS_id, myfile, file_id):
    from openai import OpenAI
    client = OpenAI()
    files_id_list = []
    vector_store_files = client.beta.vector_stores.files.list(
                            vector_store_id=VS_id
                            )
    for vsfile in vector_store_files.data:
        if vsfile.id != file_id:
            files_id_list.append(vsfile.id)
    
    
    file_paths = [myfile]
    file_streams = [open(path, "rb") for path in file_paths]

    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=VS_id, file_ids=files_id_list, files=file_streams
    )
    file_list2 = []
    vector_store_files = client.beta.vector_stores.files.list(
                            vector_store_id=VS_id
                            )
    for vsfile in vector_store_files.data:
        file_list2.append(vsfile.id)

    return file_list2[0]



def UpdateOurDBDBId(project, new_db_id, thread_id):
    etude = project.etude_set.all().get(thread_id=thread_id)
    etude.json_db_id = new_db_id

    etude.save()     


     




 