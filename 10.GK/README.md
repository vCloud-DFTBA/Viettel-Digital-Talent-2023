# Github tag:
- Tạo tag:
    ```
    git tag -a v1.0.0 -m "Release version 1.0.0"
    ```
- Push tag:
    ```
    git push origin v1.0.0
    ```
- Tag sẽ lấy commit gần nhất của nhánh hiện tại đang đứng (lấy ở local)
- Tag là duy nhất trong repository github

-Để xem danh sách tag từ remote repository:
    ```
    git ls-remote --tags origin
    ```

