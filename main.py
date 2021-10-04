#Simple to do app
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 

app = FastAPI()

class Item(BaseModel):
    id : int
    name :str
    status :bool


to_do_items = []
item1 = Item(name="hleb", id=1, status=False)
to_do_items.append(item1)

#create new item
@app.post("/createItem/")
def create_item(item: Item):
    to_do_items.append(item)
    return item

#get all items
@app.get("/getItems/")
def get_all_items():
    return to_do_items


#delete item
@app.delete("/deleteItem/{id}")
def delete_item(id:int):
    for item in to_do_items:
        if(item.id == id):
            to_do_items.remove(item)
            break


#mark item as done or undone
@app.put("/markAsDoneOrUndone{id}/")
def mark_as_done_or_undone(id:int):
    for item in to_do_items:
        if (item.id == id):
             if(item.status==False):
                 item.status = True
                 break
             else:
                 item.status = False
                 break
            
    
#update name of item
@app.put("/updateItem/{id}/")
def update_item(id:int, name:str):
    for item in to_do_items:
        if(item.id == id):
            item.name=name
            break


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=5000, log_level="info")
    
