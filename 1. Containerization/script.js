fetch("/studentdb")
.then(res => {
    return res.json();
})
.then(studentdb => {
    let placeholder = document.querySelector("#data");
    let out = "";
    studentdb.forEach(student => {
        if(student["Chuyên ngành"] == "NULL") student["Chuyên ngành"] = 'Không xác định';
        out += `
            <tr>
                <td> ${student.STT}</td>
                <td> ${student["Họ và tên"]}</td>
                <td> ${student["Năm sinh"]}</td>
                <td> ${student["Giới tính"]}</td>
                <td> ${student["Trường"]}</td>
                <td> ${student["Chuyên ngành"]}</td>
            </tr>
        `
    })
    placeholder.innerHTML = out;
})
.catch(error => console.log(error));
