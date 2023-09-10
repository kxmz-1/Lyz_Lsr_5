import os, json
template={
    'category':"",
    'source_app':"",
    "target_app":"",
    "test_function_id":""
}

target=('a2','a5','shop2','News')
def spliter(testcase):
    sp=testcase.index("_")
    return testcase[:sp],testcase[sp+1:]
for cat in target:
    accu=[]
    tot={}
    testcase=[]
    paths = os.walk(r'./generate'+'/'+cat)
    for path, dir_lst, file_lst in paths:
        for dir_name in dir_lst:
            if dir_name.count("_")==1:
                testcase.append(dir_name)
    print(testcase)
    for src in testcase:
        src_app,src_test=spliter(src)
        for ptgt in testcase:
            ptgt_app,ptgt_test=spliter(ptgt)
            if ptgt_app!=src_app:
                if src_test==ptgt_test:
                    now={}
                    now['category']=cat
                    now['source_app']=src_app
                    now['target_app']=ptgt_app
                    now['test_function_id']=src_test
                    accu.append(now)
                    print(now)
                    print(accu)
    tot['data']=accu
    
    with open(r'./dateset pairing'+'/'+cat+'_meta.json','w') as f:
        json.dump(tot,f,indent=4)