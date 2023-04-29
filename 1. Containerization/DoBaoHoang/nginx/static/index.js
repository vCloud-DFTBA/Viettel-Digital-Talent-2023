let tableBody = document.getElementById("attendees");
let tableHead = document.getElementById("headTable");

const cols = ["Họ và tên", "Năm sinh", "Giới tính", "Đại học", "Chuyên ngành"];
cols.forEach(col_name => {
    let col = document.createElement("th");
    col.innerHTML = `${col_name}`;
    col.setAttribute("scope", "col");
    tableHead.appendChild(col);
});

function appendCell(parent, val) {
    let cell = document.createElement("td");
    cell.innerHTML = `${val}`;
    parent.appendChild(cell);
};


fetch('/profiles')
    .then(resp => resp.json())
    .then(data => {
        data.attendees.forEach(attendee => {
            let row = document.createElement("tr");
            appendCell(row, attendee.name);
            appendCell(row, attendee.birth_year);
            appendCell(row, attendee.gender);
            appendCell(row, attendee.university);
            appendCell(row, attendee.major);
            tableBody.appendChild(row)
        });
    })