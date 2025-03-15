![image](https://github.com/user-attachments/assets/ec542df8-ec54-4369-a4b5-f14f2d310f87)

Đây là sau khi tôi log in với cred wiener:peter

![image](https://github.com/user-attachments/assets/a0edf15a-0c61-440b-a671-afad05fe7aad)

Đây là req sau khi log in, ở cái cookie, nó được encode bằng base64 và có thông tin user trong đó:

![image](https://github.com/user-attachments/assets/aecaec3d-99cd-4534-bab1-41d9f1312cfe)

`O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:0;}` nhìn qua thì trong cái { }, có s tôi nghĩ là đại diện cho String, số sau đó là độ dài của String, và b:0 là giá trị boolean, chính boolean thành 1 thì xuất hiện admin panel:

![image](https://github.com/user-attachments/assets/e38f9e32-2c4e-45ff-bbc9-4a2e139fe2ee)

![image](https://github.com/user-attachments/assets/ef297f58-6719-40fe-9ed5-04556d223afb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/63e82a38-bb0d-4ead-ba79-f48654f085a1)

Lần này có cái access_token nên tôi thử sửa username thành admin:

![image](https://github.com/user-attachments/assets/785b12a1-c036-408e-a2f4-52e51625acfe)

![image](https://github.com/user-attachments/assets/0d71731d-cc94-44a2-92a0-cd5bb3ebf022)

![image](https://github.com/user-attachments/assets/f0f6fc64-72eb-4464-bdce-d654fce3e446)

Tôi sửa token thành i:0 tức là đổi sang dạng integer với giá trị là 0, trong chuỗi serialized PHP object, i:0; có nghĩa là giá trị của thuộc tính access_token là một số nguyên (integer) có giá trị 0.

![image](https://github.com/user-attachments/assets/c6defdad-fa80-4035-9fd0-81ad80de66e5)

![image](https://github.com/user-attachments/assets/be19b556-3cf1-4891-b081-89720f101b17)

<h1>---------------------------------------------------------</h1>
<br>












