# 🏆 YouthDev Application Development with Generative AI Contest 2023
YouthDev-ADGAIC-2023


![Contest Logo](contest_logo.jpg)

## 🚀 Giới thiệu

Welcome to the Application Development with Generative AI Contest! This contest challenges participants to develop innovative applications using Generative AI techniques. Put your skills to the test and showcase your creativity in building AI-powered applications.

## 📝 Cài đặt thư viện
Trước khi sử dụng Ứng dụng Mermaid, hãy đảm bảo bạn có những điều sau:
•	Python đã được cài đặt trên máy tính của bạn (phiên bản 3.x được khuyến nghị).
•	Các gói Python cần thiết: pandas, tabula-py, camelot, graphviz. Bạn có thể cài đặt chúng bằng lệnh pip:
```
pip install pandas tabula-py camelot-py[cv] graphviz
```



## 💡 Chạy Chương trình

Để chạy Ứng dụng Mermaid, làm theo các bước sau:
1.	Mở cửa sổ dòng lệnh hoặc terminal.
2.	Điều hướng đến thư mục chứa tệp script (mermaid_app.py).
3.	Chạy script bằng lệnh sau:
```
python mermaid_app.py <đường_dẫn_tệp>
```
Thay thế <đường_dẫn_tệp> bằng đường dẫn đến tệp Excel hoặc PDF chứa dữ liệu học phần.
4.	Script sẽ tạo ra một biểu đồ Mermaid dựa trên tệp được cung cấp và hiển thị mã của biểu đồ trong cửa sổ console.


## 🎯 Các Hàm trong Chương trình

Ứng dụng Mermaid cung cấp các hàm sau:
**read_data(đường_dẫn_tệp)**
Hàm này đọc dữ liệu học phần từ tệp Excel hoặc PDF và trả về một pandas DataFrame.
•	đường_dẫn_tệp (str): Đường dẫn đến tệp đầu vào.
Trả về:
•	df (pandas DataFrame): DataFrame chứa dữ liệu học phần.
**generate_mermaid_diagram(data)**
Hàm này tạo ra một biểu đồ Mermaid dựa trên dữ liệu học phần.
•	data (pandas DataFrame): DataFrame chứa dữ liệu học phần.
Trả về:
•	diagram (str): Mã của biểu đồ Mermaid.
**get_node_color(tên_nút, color_map)**
Hàm này tạo ra một màu ngẫu nhiên cho nút dựa trên tiền tố tên của nút.
•	tên_nút (str): Tên của nút.
•	color_map (dict): Một từ điển lưu trữ ánh xạ màu cho các tiền tố nút.
Trả về:
•	color (str): Mã màu được tạo ra cho nút.
**main()**
Hàm chính của script. Nó xử lý các đối số dòng lệnh, đọc tệp đầu vào, tạo biểu đồ Mermaid và in ra console.


## Kết quả thực nghiệm

```
graph TD
    ENC101((ENC101)) -->|Tien Quyet| ENC102((ENC102))
    style ENC101 fill:#DA158A,stroke:#333,stroke-width:4px
    style ENC102 fill:#DA158A,stroke:#333,stroke-width:4px
    classDef ENC101Class fill:#DA158A,stroke:#333,stroke-width:4px
    class ENC101 ENC101Class
    classDef ENC102Class fill:#DA158A,stroke:#333,stroke-width:4px
    class ENC102 ENC102Class
    ENC102((ENC102)) -->|Tien Quyet| ENC103((ENC103))
    style ENC102 fill:#DA158A,stroke:#333,stroke-width:4px
    style ENC103 fill:#DA158A,stroke:#333,stroke-width:4px
    classDef ENC102Class fill:#DA158A,stroke:#333,stroke-width:4px
    class ENC102 ENC102Class
    classDef ENC103Class fill:#DA158A,stroke:#333,stroke-width:4px
    class ENC103 ENC103Class
    .......
    .......
    PHT317((PHT317)) -->|Tien Quyet| PHT318((PHT318))
    style PHT317 fill:#602A51,stroke:#333,stroke-width:4px
    style PHT318 fill:#602A51,stroke:#333,stroke-width:4px
    classDef PHT317Class fill:#602A51,stroke:#333,stroke-width:4px
    class PHT317 PHT317Class
    classDef PHT318Class fill:#602A51,stroke:#333,stroke-width:4px
    class PHT318 PHT318Class
```

[Live Editor](https://mermaid.live/view#pako:eNrNm1FP20gQx78Kcl9AAuTZXe-u83AShaJKd7Q9wdOJl4i4gAoJCkFXDvrdb-2dhHE8qbCHOPBiY-_-_-sfo_XMWDwlF5NRkQySy-nw7mrr7Oh8vBV-Pn05hBS2t-NxZ2drb--P57PrYrz198NjMXuOAxQOUDs7cdr97PGmwMlb369vbgYfPh1nxzrfvZ9NJz-KwQetNZ7v_Xs9ml0NzN3PxlzVdu7FzfD-_qj4jtaH5a-dNOZrJzqcg5I6KKpDkBOiPHKNAzSDXAmQaxnydQCpO2ipg6Y6BDkhyiM3OMAwyLUAuZEhXweQuoOROhiqE--e_vkXQLa9HY8M8uqGxQG2jjxOwgWBP_bpx1cjj3pt5y6ARGsKpJ3GfO1Eh3OwUgdLdeLdw5NvkLoQxXjCQC_vWBxhl-IcZ-GaDg6tOno99SjYdu6CCXpTKO1EFqunSoyJlXpYQ3VewFOqTexfT0GlYUB1bGK3XalXejjX-6PjY9WW-lqAvDhUC6QO7VY5f0Kig8jDBZ1FojpbgbxMbOJxCXk1qe2CXuYucp4OyCtrIZCwdqLDONQzow4O4QmJDolyh1HuVmwu8-3HMZuLdd33FifbW6yTRrmjOoyDePPCvcstbyxOIVG1ArlP4wDPbCxOdUfuUxFyp6RAFNVhHHwqdAhPSHTaRDkid-kbR3n63qNcitylVKcNchzg3Bsjd-8dudTBOarTBnmGyLM3Rp69d-SZFHlGdUjG4jFj8auQk82-kbH4jhlLp_dAPWPx0ozFU52-3hZVLQBYD3HNrZODL1XZH49MOQTdojzq4dyPHtzhQetqCKTFEFCdJYe4QOrQbpXzJyQ6r49y7XX1NwnHN43yoPe-ozwsUPZHLZ-Q6JAkkaTdAfne8-lkfLn1eTi-QuIKiatGkIdrm0rLg7WUh6I6vaXlS-V8g_jXU61i7RmOjRgP17rXnpJyv7KWxXi5dqKzwXK_SVwjcc0Q192Jt-8U1IlrKXFNdfrqJzAbeYM4xPvh2CQOXkDci4iDcB8v1050-npTVBccEncriOdIPGeI5wLiTkY8lxLPqQ5H3EmJO6rzm4Z5492ZYh1UnjTfnmn7akbUbq-9P1NppVItnyr12JdnuuYN9hbRW4a8zTb1qSJYC7HbjOr0-p2iXvU3iXsk7hniXkDcyYh7KXFPdfpqKyz3Z9ncHDA3ByY3h031b4O1NDcHqtNn_5a2ZzniDok7hriDTbVvg7WQuAOq02f7lrYKWeIWiVuGuN1UKzFYS4lbqtNnK_G39Wf5QgeDWQsYJmuBjX1xLr2lSQuYmlJvVWjzc1wz0rG35TQT6VoQ6UoW6dLOk9NUp7cObpmyW6yJ7Ir3J-aInskRfdY9zLUVhbmX5og-ozpcTWSlNZGlOiRjwazcr6qIqjI0nnB7Sy5IWoQFUb0S7bS35DUlLm-R5ubeUJ1XRnrZAjLY4TJMh8sIqn8r63AZaYfLUJ2-Iv3b5zNdfvyJR-ZTRXUjwwFLm0uchAtyKoP8-NXIo17buQsg0ZoCaacxXzvR4RwyqUNGdQhyQpRHbnGAZZBnAuRWhnwdQOoOVupgqQ5B7pCoW4Xc4wDPIHcC5F6G3EmBOKrDOXipg6c6BDkhyiPPcUDOIPcC5LkM-TqA1B1yqUNOdV6QQxqJQroCOQAOgCZySLsjBxAhh1QIJKyd6HAOIHUAqkOQE6I8coUDFIMcBMiVDPk6gNQdlNRBUR2CXCNRvQo5pjTLZX-cJEBuZMi1FIimOpyDNCcCQ3UIckKUR44pDTBJIgiSRJAliWsBUneQ5kSQUR2CHHNAsKuQY0oDjkFuBcidDLk0hQNLdTgHaU4EjuoQ5IQojxxTGmCSRBAkiSBLEtcCpO4gzYnAU51kN7ktprfD61EySJ7KsefJ7Kq4Lc6TQTgdDac_zpPz8a8wbvgwm5w-ji-SwWz6UOwmD3ej4aw4uh5eToe384vF6Ho2mZ7E_-6t_sl3N7kbjv-ZTBZDwq_J4Cn5mQxA2X1twRptrMtTbbPd5DFcNn5fWZ-F2kHbPAOT_dpN_qsU0n2fOevA6NyacGLsr_8BcQcw0A)

```mermaid
graph TD
    ENC101 --> ENC102
    ENC102 --> ENC103
    ENC103 --> ENC104
    SKL115 --> SKL116
    CMP1074 --> CMP164
    CMP164 --> COS120
    COS135 --> COS101
    CMP167 --> CMP174
    CMP172 --> CMP180
    CMP167 --> CMP170
    CMP167 --> CMP177
    CMP167 --> CMP175
    COS138 --> CMP172
    CMP101 --> MAN104
    COS138 --> CMP383
    PHT304 --> PHT305
    PHT305 --> PHT306
    PHT307 --> PHT308
    PHT308 --> PHT309
    PHT310 --> PHT311
    PHT311 --> PHT312
    PHT313 --> PHT314
    PHT314 --> PHT315
    PHT316 --> PHT317
    PHT317 --> PHT318
```
## ❓ Questions and Support

<<<<<<< HEAD
Join Zalo Group: https://zalo.me/g/dyqsii775

For any questions or any support, please contact me via: hieuliem201@hutech.edu.vn or visit https://www.facebook.com/hieuliempham.

=======
For any questions or any support, please contact me via: hieuliem201@hutech.edu.vn or visit https://www.facebook.com/hieuliempham.
>>>>>>> c2e09b3c8ca083a6e6ee387c6005cd2da7cdee13

![Contest Logo](contest_logo.jpg)
