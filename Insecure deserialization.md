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
