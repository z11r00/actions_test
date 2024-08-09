import json  
import os  
  
# 创建一个包含一些数据的字典  
data = {  
    'name': 'John Doe',  
    'age': 30,  
    'is_student': False,  
    'courses': ['Math', 'Science', 'Literature'],  
    'address': {  
        'street': '1234 Elm St',  
        'city': 'Somewhere',  
        'zip': '12345'  
    }  
}  
  
# 定义文件路径  
file_path = 'rocdatas/202408/data.json'  
  
# 确保目录存在  
directory = os.path.dirname(file_path)  
if not os.path.exists(directory):  
    os.makedirs(directory)  
  
# 将字典写入到JSON文件中  
with open(file_path, 'w', encoding='utf-8') as f:  
    json.dump(data, f, ensure_ascii=False, indent=4)  
  
print('JSON文件已生成。')