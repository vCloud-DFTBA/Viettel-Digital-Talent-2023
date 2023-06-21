function createTableCell(text) {
    var cell = document.createElement('td');
    cell.textContent = text;
    cell.classList.add('centered-cell');
    return cell;
}

function getStudents(){
fetch('api')
    .then(response => response.json())
    .then(data => {
        var studentTable = document.getElementById('studentTable');
        var tbody = studentTable.getElementsByTagName('tbody')[0];
        tbody.innerHTML = '';

        data.forEach(mentee => {
            var row = document.createElement('tr');

            row.appendChild(createTableCell(mentee.full_name));
            row.appendChild(createTableCell(mentee.birth_year));
            row.appendChild(createTableCell(mentee.gender));
            row.appendChild(createTableCell(mentee.university));
            row.appendChild(createTableCell(mentee.major));
            tbody.appendChild(row);
        });
    });
}



getStudents()