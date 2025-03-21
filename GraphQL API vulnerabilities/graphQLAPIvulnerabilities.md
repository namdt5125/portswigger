![image](https://github.com/user-attachments/assets/61a44a82-60f8-4d7d-bc4d-919e7c05a8d2)

Đây là giao diện của trang web:

![image](https://github.com/user-attachments/assets/f3e9f9a8-8106-4623-b070-923ec5b090d3)

Đây là cái req của graphql:

![image](https://github.com/user-attachments/assets/e2c19e35-dca3-4ad0-9772-ea48faa0aa71)

Đây là GraphQL:

![image](https://github.com/user-attachments/assets/b4ae0033-94e7-44f5-830e-b33ae11fa4a8)

Tôi sửa thành `{"query": "{__schema{queryType{name}}}"}` và ấn gửi thì ra cái này:

![image](https://github.com/user-attachments/assets/00f77dcc-5e33-4b71-8fb9-507526b353fa)

Tôi chèn cái [Full introspection query](https://gist.github.com/franzejr/d0a178286d0e23d3ed50999288806068) vào GraphQL và ra cái này:

![image](https://github.com/user-attachments/assets/49859ddf-3ef0-425a-b4e4-67498b2a9fbb)

Tôi chuyển sang raw và paste vào trong [GraphQL Visualizer](https://nathanrandal.com/graphql-visualizer/):

![image](https://github.com/user-attachments/assets/53c0b49d-0a75-4bf3-8da0-eb7bf27c64f2)

![image](https://github.com/user-attachments/assets/11f1ab63-0d5e-4644-b583-0d1f0d953a36)

Cho vào đây để dễ nhìn hơn thay vì đọc từng cái 1 và có xuất hiện cái postPassword thuộc kiểu string, tôi thêm cái postPassword vào GraphQL nhưng kết quả trả lại là NULL:

![image](https://github.com/user-attachments/assets/0511d91b-aaf8-45ad-acb3-069b17c9e31c)

Nếu để ý mấy cái id trả về thì không có id là 3, tôi ấn bừa 1 bài post, lấy req và thay đổi id thành 3

![image](https://github.com/user-attachments/assets/d1caf60e-43f4-450e-9c32-e69db05e772f)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9bc7ae96-ee63-40d1-ac4e-40c3b4f803a5)

Khi tôi thử tính năng log in với cred là admin:admin kết quả trả về là json

![image](https://github.com/user-attachments/assets/e765cd4c-c419-487d-aabe-2c766a6c5089)

Thêm cái extension InQL vào và bấm analyze thì ra cái này:

![image](https://github.com/user-attachments/assets/002634d2-025d-4f94-acd9-e58437d2307a)

Và ở đây có getUser là lấy username và password dựa trên id của user:

![image](https://github.com/user-attachments/assets/cd9349b2-ba7a-4a78-a5f2-3a25e10519e9)

Vào trong repeater và sửa thành getUser, id=1:

![image](https://github.com/user-attachments/assets/2713b635-082c-4140-8db3-b4c08e2d9f99)

![image](https://github.com/user-attachments/assets/cd950ab2-85b0-4c91-8d91-fed4caeaafb1)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/def61e5d-89e4-4911-8a42-9d984297a9dc)

Lần này thì nó để ở dạng param trong body:

![image](https://github.com/user-attachments/assets/6c6d3edf-4bbe-4c1a-8f0a-17ad097d814c)

Tôi thử vào cái api thì hiện ra cái này:

![image](https://github.com/user-attachments/assets/f6a4607c-ea28-48eb-9f22-438ac7816e81)

Dựa vào kiến thức sgk mà PortSwigger có bảo thì tôi dùng `api/?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D`:

![image](https://github.com/user-attachments/assets/e3ac6570-1a22-4f8d-b403-d466c7d8ae16)

![image](https://github.com/user-attachments/assets/84605c3b-7053-41da-a8be-f8b83775bd2b)

Tôi thử IntrospectionQuery nhưng không được:

![image](https://github.com/user-attachments/assets/d88f617b-d858-485f-a29c-fdaf000215d2)

![image](https://github.com/user-attachments/assets/296054bf-ca11-430c-9fc9-af8228a1e106)

Nhưng khi xuống dòng ở __schema thì có kết quả:

![image](https://github.com/user-attachments/assets/0774856f-7f0d-4337-82a9-bbf6eb309bf7)

Copy mang ra cái [GraphQL Visualizer](https://nathanrandal.com/graphql-visualizer/) thì ra cái getUser và không thấy có password:

![image](https://github.com/user-attachments/assets/86cd7b44-fb72-4ed0-8ccb-a3fd405144af)

![image](https://github.com/user-attachments/assets/5bd5e43c-a057-4483-aed9-87356fd5e17a)

Vào cái response, chọn save 

![image](https://github.com/user-attachments/assets/f9da32a2-06ae-440b-8685-2d3d5dac3018)

Lúc đó target sáng lên, vào target thì có 2 cái req là getUser và DeleteOrganizationUserInput, đưa cái DeleteOrganizationUserInput vào repeater và send:

![image](https://github.com/user-attachments/assets/46567170-6ef9-4137-b875-41b657fd3c2c)

Cái này là xóa dựa trên id, tôi dùng cái getUser để tìm carlos thì là id 3

![image](https://github.com/user-attachments/assets/f97af478-700a-451a-aa95-58525330c70e)

Vào cái xóa và đổi id thành 3 là xong

![image](https://github.com/user-attachments/assets/ce0f5fee-cc9e-4f26-a3f4-330c47f81a99)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/6a7b8df0-002f-4101-b0d7-727f82f9fc73)

Đây là req sau khi login:

![image](https://github.com/user-attachments/assets/169dfd25-c478-430a-8fbc-78cbbd318402)

Tôi login với wiener:peter thì được:

![image](https://github.com/user-attachments/assets/2ce5b1ef-badb-45ee-ab17-b2eb48f5abda)

Tôi ném vào intruder để brute force password và xuất hiện `You have made too many incorrect login attempts. Please try again in 1 minute(s)`

![image](https://github.com/user-attachments/assets/80253b7d-f75f-46a5-bc1e-eb20cca94796)

Tôi chèn thêm cái IntrospectionQuery vào thì trả lại cái này:

![image](https://github.com/user-attachments/assets/ee1a341e-551c-4ee0-a290-d65dd4737fcf)

![image](https://github.com/user-attachments/assets/5e93568d-240c-4c1a-b8d8-b5e9b983dd37)

Và đây là cái GraphQL của bài:

![image](https://github.com/user-attachments/assets/0e63a486-d4cc-4644-a101-9d61251b4d60)

Ở hint có cho đoạn list of aliases corresponding, tôi đưa vào console và chạy, paste ra cái này:

![image](https://github.com/user-attachments/assets/e0af16ba-c2c5-44ca-b599-09ddc599ffeb)

![image](https://github.com/user-attachments/assets/cfab10c4-ade6-454e-9789-7c185b235553)

Đưa vào trong GraphQL, sửa lại 1 chút là ra:

![image](https://github.com/user-attachments/assets/f4e892bc-aca4-4ef9-a883-c5a2f7e157c1)

Tìm cái success là true, ra mật khẩu là monitor

![image](https://github.com/user-attachments/assets/b26b5b2e-7384-444b-b3ab-9752b1da22cc)

![image](https://github.com/user-attachments/assets/6bd8e520-0f6d-4e5d-bd6e-2601419c88d7)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/9b19389b-7895-432d-b0ec-6094d6b9b423)

Đây là req login với cred wiener:peter 

![image](https://github.com/user-attachments/assets/ced336d5-ec65-43f8-a056-a658a698cb7c)

Tôi dùng IntrospectionQuery thì cũng chỉ ra thế này:

![image](https://github.com/user-attachments/assets/4898cae3-710c-4815-975c-6fe94ee917bb)

Vào target thì thấy cái changeEmail:

![image](https://github.com/user-attachments/assets/a0f762c9-6f5f-42a6-81a5-72914c776740)

Thêm cái `Content-Type: application/x-www-form-urlencoded` vào bằng cách change method qua GET rồi lại về POST:

![image](https://github.com/user-attachments/assets/84691c59-d7bc-4ad9-934c-74d558976537)

Gửi đi thì nó bảo Query not present, thêm cái query vào và gửi, nó bảo thiếu variables:

![image](https://github.com/user-attachments/assets/e88ba5ea-6717-4f1f-bf73-f6cef6579a5e)

Thêm cái variables vào là ra:

![image](https://github.com/user-attachments/assets/c0b2a975-e815-4e96-895e-317efa65daba)

query và variables dựa trên cái này:

![image](https://github.com/user-attachments/assets/23910ab5-289c-41b3-8f33-ada92c868386)

Nếu để im như này mà tạo PoC thì lúc đưa vào exploit nó bị invalid variables thế nên phải encode cái query và variables:

![image](https://github.com/user-attachments/assets/08a93102-cdf0-42d6-93ef-42d92d8d4c5c)

![image](https://github.com/user-attachments/assets/cab2b672-12c6-4e3e-89f5-4816939ec753)

![image](https://github.com/user-attachments/assets/9d36a1c9-88ce-4ac2-a759-1b3942513238)



