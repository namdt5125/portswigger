![image](https://github.com/user-attachments/assets/0f90b5c0-cc53-4adb-939f-b59d104e70bf)

Đây là giao diện sau khi đăng nhập bằng wiener:peter 

![image](https://github.com/user-attachments/assets/944abff0-fd2d-4b9f-a3c8-5af4e40e332e)

Khi tôi cố tình truy cập vào /admin thì nó chặn lại và không cho

![image](https://github.com/user-attachments/assets/b9db5c3b-4dd3-47fc-9be9-eb091e414013)

Bây giờ thì tôi sẽ đi lượn qua history xem có gì không 

![image](https://github.com/user-attachments/assets/05930bd5-f958-4509-87fc-ad4524e86481)

Mấy cái được highlight màu xanh lá là của extension jwt editor

![image](https://github.com/user-attachments/assets/7628ee77-3ea4-4511-8dc2-cf678d373773)

Dịch cái jwt ra thì tôi thấy đây là user wiener

![image](https://github.com/user-attachments/assets/f48789f7-a5c4-41cd-997e-e4e6002b39ea)

Tôi ném vào repeater và sửa lại thành administrator để vào thử 

![image](https://github.com/user-attachments/assets/871f5f31-b229-4727-965d-55c18e9e89ec)

Và hiện ra giao diện của admin, xóa user là xong 

![image](https://github.com/user-attachments/assets/2740e8ed-52ec-4c16-acbc-d8620f1d2fd5)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/e724e22f-7207-461e-9ad0-782cc2d52d4c)

![image](https://github.com/user-attachments/assets/d1ccb581-667c-41f7-b2e9-0c2e3643c7c0)

Tôi làm y hệt bài trước nhưng bài này bắt phải login cơ

![image](https://github.com/user-attachments/assets/7d6c643c-c64c-4f41-b4d2-0afc9338a95f)

Tôi thử intercept cơ mà cái này có csrf nên không làm gì được, 

![image](https://github.com/user-attachments/assets/47fa0437-0a10-4233-8194-da13912ac8c6)

Sau 1 lúc lay hoay thì tôi đọc lại đề bài, nó bảo là bypass via flawed signature verification, mà cái signature được mã hóa bằng RS256 ở cuối của jwt, ở cái đoạn đầu có ghi, tôi search google và đổi sang none rồi gửi xem nó như thế nào:

![image](https://github.com/user-attachments/assets/b7ee71d5-f793-485a-bd7f-f13dcea8a9e6)

![image](https://github.com/user-attachments/assets/b919feb6-7f29-4ae5-b3fc-c9afbbd77bf7)

Và xóa cả đoạn sau nữa, vì đoạn sau được mã hóa RS256, nó là cái chữ kí, nếu thuận toán là none thì đút thêm cái mã hóa vào làm gì, thế nên xóa từ dấu . trở đi

![image](https://github.com/user-attachments/assets/d90101ce-0562-4d78-8713-ceafd7308af6)

![image](https://github.com/user-attachments/assets/6333c73e-f1c7-419d-a066-a55341c00ab3)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/763b67e4-31ab-4fba-b8d6-db7d37674d9a)

![image](https://github.com/user-attachments/assets/c2f7db58-e423-472d-8a61-42776d0925e7)

Bài bảo dùng hashcat nên tôi dùng hashcat `hashcat.exe -a 0 -m 16500 ../target/target.txt ../target/rockyou.txt`, tôi dùng exe vì nó có gắn cái gpu của tôi vào nên chạy siêu nhanh, cái jwt thì ở trong file target.txt

![image](https://github.com/user-attachments/assets/8b0556e6-dabb-40bd-8989-d8c3fb3e6499)

Nó là `secret1`, giờ đến bước tạo cái jwt mới, trước tiên là encode cái `secret1` thành `c2VjcmV0MQ==`:

![image](https://github.com/user-attachments/assets/1fe4b686-8f74-4310-a22f-49a7148960ee)

Ấn vào new và dán cái base64 vào cái `k` 

![image](https://github.com/user-attachments/assets/ccc82656-3a79-4cac-ae3f-f3b9b60ea924)

Bấm ok

![image](https://github.com/user-attachments/assets/554c76e3-0a0f-450d-a1e3-d9f734054639)

Vậy là có 1 cái key, json web token sửa thành admin

![image](https://github.com/user-attachments/assets/abfe0cc6-0088-43a5-9fac-4be840d4809e)

Và bấm sign, chọn cái key vừa nãy tạo, kí vào 

![image](https://github.com/user-attachments/assets/31745a02-ebc6-4e96-a989-520e25006f9c)

![image](https://github.com/user-attachments/assets/7bb817fe-4726-4fd5-b203-40afd6d0a2c6)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/a3dddf76-6f6d-470c-91de-6b04d4979434)

![image](https://github.com/user-attachments/assets/1fe7ecf5-7d11-4f44-bc02-3cde854b3127)

![image](https://github.com/user-attachments/assets/39e1b6a3-6489-4612-9ae7-0ba29673d092)

Đầu tiên thì tôi xem cái jwt và ngồi thử mấy cái cách từ bài cũ thì đều không được, đề bài có bảo là  bypass via jwk header injection:

![image](https://github.com/user-attachments/assets/b44f55e0-b38d-4908-b698-c8a2e6901e21)

![image](https://github.com/user-attachments/assets/201859d3-5965-490f-a352-2c2bff2ca983)

Kết hợp với đề bài thì tôi nhảy sang JWT editor của burp, chọn tạo RSA key mới và tạo 1 cái<br>
Thông thường, máy chủ sẽ ký JWT bằng một khóa riêng tư (private key), và chỉ máy chủ có khóa này mới có thể tạo JWT hợp lệ và máy chủ sẽ dùng khóa công khai (public key) tương ứng để kiểm tra tính hợp lệ của chữ ký

![image](https://github.com/user-attachments/assets/abe633ab-2944-418e-a8fa-aa5a8a1a02dd)

Quay lại và sửa wiener thành admin

![image](https://github.com/user-attachments/assets/fe8ab4e7-c81b-40ed-8839-8396a14b7ae6)

![image](https://github.com/user-attachments/assets/57beab10-944d-4f1d-845b-269e978765e9)

![image](https://github.com/user-attachments/assets/1d61f943-cca9-464e-8d33-fe00d485a825)

Chọn embedded JWK và ném cái key tôi vừa tạo vào trong, vậy là đã có 1 cái JWT mới, do máy chủ trong bài 
 không kiểm tra nên nó tin tưởng public key bên trong JWT và dùng nó để xác thực chính JWT đó, thay vì sử dụng public key thực sự của máy chủ

![image](https://github.com/user-attachments/assets/154c1715-165e-4fbb-892b-2f2ce1ec277f)

![image](https://github.com/user-attachments/assets/8182c85c-d94f-4631-a2e9-4a396e3c4263)

Cuối cùng vẫn là do bên máy chủ tin tưởng JWT chứa public key mà không xác minh nguồn gốc của nó

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/7cf19d7c-b4af-4cbf-ae57-7aece08cd40d)

![image](https://github.com/user-attachments/assets/61092b59-ad95-4fd7-b603-d99b1f404b60)

Như mấy bài trước nhưng mà không có được, đề bài có nhắc đến jku. Trong JWT, jku (JWK Set URL) là một thuộc tính tùy chọn trong phần header của token. Nó chứa một URL trỏ đến một tập hợp các JWK, giúp bên xác thực lấy khóa công khai để kiểm tra chữ ký của JWT<br>
Và trong bài này nó không hề kiểm tra cái url nên có thể dùng exploit server để giả mạo 

![image](https://github.com/user-attachments/assets/394e5b53-fcd9-4e82-be67-0fe05aabb720)

Truy cập vào exploit server để lưu trữ khóa công khai trên exploit server sau khi tạo 1 cái RSA mới

![image](https://github.com/user-attachments/assets/b2a62705-ee1f-4e48-8595-6125d295f06f)

Đi copy và paste vào body trong exploit server

![image](https://github.com/user-attachments/assets/f89d9d48-0aeb-4bba-9f8e-415092c6c6b4)

![image](https://github.com/user-attachments/assets/fff9fb4c-b422-4409-adae-616919824682)

Nhớ đổi `Content-Type: application/json;`, sau đó đổi kid sang kid mà đã tạo(chuẩn bị sử dụng nó trong JWT giả mạo, bên máy chủ dùng kid để tra khóa công khai tương ứng trong danh sách JWK Set của nó để xác thực chữ ký), thêm jku vào trong json kèm với đường dẫn của exploit server 

![image](https://github.com/user-attachments/assets/228f0768-3dd2-4a7a-a855-0a0d5a70eaa6)

Chọn store, quay lại burp và ấn vào sign. Sau đó, khi JWT sử dụng khóa này, máy chủ sẽ xác thực JWT bằng khóa giả thay vì khóa thực sự của hệ thống

![image](https://github.com/user-attachments/assets/3a43206c-8c26-4fc5-9b06-13997355a3b8)

![image](https://github.com/user-attachments/assets/7e5c4e99-4274-4fbd-a818-18d452c8b27b)

![image](https://github.com/user-attachments/assets/521ac9c3-ca6e-49da-b45d-1a10c5e8dee6)

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/0a40a1f8-d9b0-4f36-962f-a91c63d89dec)

![image](https://github.com/user-attachments/assets/45b9c727-ac4a-41ee-9ec5-44795716276e)

Theo đề bài thì máy chủ dùng kid để xác định khóa cần dùng xác thực JWT, ý tưởng là sẽ để kid là khóa rỗng(NULL), tôi vào JWT editor để tạo 1 symmetric key mới

![image](https://github.com/user-attachments/assets/a61aabe5-3fe3-4b78-8bfe-ca3927437d70)

Đổi giá trị k thành `AA==`, tức là NULL encode sang base64, trong một khóa JWK đối xứng (symmetric key), k chính là khóa bí mật để ký và xác minh JWT, việc đổi sang NULL để tí nữa phù hợp với cái `/dev/null`

![image](https://github.com/user-attachments/assets/89ae528e-3447-4aa3-b212-93a3b7718b3d)

Sửa kid thành `../../../../../../../../../dev/null`, buộc máy chủ đọc `/dev/null` là khóa và sửa qua qua thành admin. việc sử dụng `/dev/null` trong kid làm JWT có thể xác thực mà không cần khóa thật

![image](https://github.com/user-attachments/assets/d208f7d1-db25-4686-8d9a-a3ccc3eba1a9)

Và bấm sign

![image](https://github.com/user-attachments/assets/a14a2516-602d-4afb-bc9f-ed1c4a2b04b9)

![image](https://github.com/user-attachments/assets/382c750c-b37f-4d36-a4cc-e99d69412b53)

Nói chung thì kid là xác định khóa bí mật và trỏ đến `/dev/null` để bypass xác thực, trong khi đó k thì là chứa khóa bí mật để xử lý JWT, đặt k = `AA==` để hợp lệ với cái `/dev/null` kia 

<h1>---------------------------------------------------------</h1>
<br>

![image](https://github.com/user-attachments/assets/8ffb125a-dab6-4221-82e1-a697aa49314b)

![image](https://github.com/user-attachments/assets/1a6c44c2-4c76-460d-9046-4641c8dbdc2c)

![image](https://github.com/user-attachments/assets/59cb7ca1-e4f5-4558-b00d-6d3cead61f86)

Theo lý thuyết thì tôi thử truy cập vào 2 cái dir này(vì hint bảo có cái public ở dạng X.509 PEM(PEM (Privacy-Enhanced Mail) là một định dạng tiêu chuẩn để lưu trữ và truyền tải khóa mật mã, chứng chỉ số, hoặc dữ liệu nhạy cảm bằng cách sử dụng Base64 để mã hóa dữ liệu nhị phân)) và tìm được, bước này nhằm lấy khóa công khai của máy chủ để lợi dụng trong phần sau:

![image](https://github.com/user-attachments/assets/7bb2d54e-a2d1-4d3a-ba23-d56287fc326c)

Tôi tạo 1 cái RSA mới và paste cái vừa copy ở jwks.json vào:

![image](https://github.com/user-attachments/assets/d54e34c0-7279-4b6f-be46-89ebb1a9ce03)

Do đề bảo nó là X.509 PEM nên copy ở dạng PEM và đem đi encode base64 

![image](https://github.com/user-attachments/assets/ee363de3-8257-4bba-911a-abe04b81b4e7)

![image](https://github.com/user-attachments/assets/d9853994-c9a0-4b8b-a21a-cc96b2b75809)

Tôi tạo 1 cái Symmetric Key mới và paste cái nội dung vừa copy vào k

![image](https://github.com/user-attachments/assets/732365ba-c6cc-46b6-8555-2e19b942986d)

Đổi sub thành admin và alg thành HS256 do khi chuyển thuật toán ký từ RS256 (bất đối xứng) sang HS256 (đối xứng), máy chủ sẽ dùng cùng một khóa để ký và kiểm tra chữ ký, việc đổi khóa công khai của máy chủ thành một khóa đối xứng để ký JWT, khiến máy chủ tin rằng chữ ký là hợp lệ

![image](https://github.com/user-attachments/assets/19bd87a3-0d4d-4be1-8055-20f4471b904e)

![image](https://github.com/user-attachments/assets/faab06ed-13d9-4801-a405-ffe02214b078)

Nói chung là lỗi ở cái RS256 và HS256, tôi có thể chuyển từ cái này sang cái kia và có thể dùng được cái mã khóa công khai nằm ở jwks.json để thay cho cái khóa bí mật

<h1>---------------------------------------------------------</h1>
<br>








































