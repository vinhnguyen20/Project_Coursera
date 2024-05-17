import pandas as pd

# Tạo một DataFrame đơn giản
data = {'Type': ['Mammal', 'Mammal', 'Mammal', 'Bird', 'Bird'],
        'Name': ['Cat', 'Dog', 'Elephant', 'Parrot', 'Penguin'],
        'Value': [10, 20, 15, 5, 8]}
df = pd.DataFrame(data)

# Sử dụng groupby để nhóm theo cột 'Type' và áp dụng các hàm tổng hợp
result_df = df.groupby('Type').agg({
    'Name': ', '.join,   # Nối tất cả các tên trong mỗi nhóm
    'Value': 'sum'       # Tổng giá trị trong mỗi nhóm
}).reset_index()

# In kết quả
print(result_df)
