![image](https://github.com/user-attachments/assets/0688f651-3604-44e7-8770-fb52e2c61ab5)

![image](https://github.com/user-attachments/assets/988b62fa-18d5-4dd1-95bd-446963de1d9b)

![image](https://github.com/user-attachments/assets/8f6584cb-3945-4913-872c-0db1cbf857d3)

![image](https://github.com/user-attachments/assets/206ca057-36f9-46e9-9a4f-cf391e18849e)

Nhớ tắt filter images trong burp đi:

![image](https://github.com/user-attachments/assets/92d6667a-bd2b-495a-b40d-5ab6bc571ceb)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/be5e6634-4cb2-4c3d-bd38-10cc930270d2)

![image](https://github.com/user-attachments/assets/8f32f21a-4083-4663-9704-c262a4080ec1)

Lần này nó nhận đường dẫn tuyệt đối thay vì đường dẫn tương đối như ban nãy

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/da8a7eeb-e6e5-484b-9185-20b98857319a)

![image](https://github.com/user-attachments/assets/c059b91f-88b4-4aaf-a31a-7141e7f85ee0)

`....////....////....////....////etc/passwd`, payload này hoạt động là do trong mã nguồn có sử dụng bộ lọc là khi có `..` hoặc `../` là nó tự động xóa đi, nhưng nó chỉ check 1 lần, không có lặp lại, thế nên `....////....////....////....////etc/passwd` 
biến thành `..///..///..///..///etc/passwd`, với cái dấu / kia thì không quan trọng vì có // hay /// hay thậm chí nhiều hơn thì nó vẫn giữ đúng chức năng của nó

<h1>---------------------------------------------------------</h1>
<br>























