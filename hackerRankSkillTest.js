class NotesStore{
    constructor(){
        this.arr=[];
    }
    addNote(state,name){
        if(name===''){
            throw 'Error: Name cannot be empty';
        }
        if(state==='completed'||state==='active'||state==='others'){
            if(state==='completed'){
                this.arr.push({completed: name});
            }

            if(state==='active'){
                this.arr.push({active: name});
            }

            if(state==='others'){
                this.arr.push({others: name});
            }
        }else{
            throw `Error: Invalid state ${state}`;
        }
    }
    getNotes(state){
        let myname = [], a, b;
        if(state==='completed' || state==='active' || state==='others'){
            for(a of this.arr){
                for(b in a){
                    if(b===state)
                    myname.push(a[b])
                }
            }
        }else{
            throw `Error: Invalid state ${state}`;
        }
        return myname;
    }
}